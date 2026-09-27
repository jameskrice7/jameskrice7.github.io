"""Preserve the legacy feed and refresh seminar availability after rendering."""
from pathlib import Path
import json,re,html,xml.etree.ElementTree as ET
SITE=Path(__file__).resolve().parent
OUT=SITE/'_site'
(OUT/'.nojekyll').touch()
ns='http://www.w3.org/2005/Atom'
ET.register_namespace('',ns)
def element(parent,name,value):
    e=ET.SubElement(parent,'{'+ns+'}'+name);e.text=value;return e
feed=ET.Element('{'+ns+'}feed')
element(feed,'title','James Kennon Rice')
element(feed,'id','https://jameskrice7.github.io/')
element(feed,'updated','2026-09-27T00:00:00Z')
ET.SubElement(feed,'{'+ns+'}link',{'href':'https://jameskrice7.github.io/feed.xml','rel':'self'})
records=json.loads((SITE.parent/'migration/content-map.json').read_text(encoding='utf-8'))
for record in records:
    if not record['source'].startswith('_posts/'):continue
    entry=ET.SubElement(feed,'{'+ns+'}entry')
    url='https://jameskrice7.github.io'+record['url']
    element(entry,'title',record['meta']['title']);element(entry,'id',url)
    element(entry,'updated',str(record['meta']['date'])+'T00:00:00Z')
    ET.SubElement(entry,'{'+ns+'}link',{'href':url})
    author=ET.SubElement(entry,'{'+ns+'}author');element(author,'name','James Kennon Rice')
ET.ElementTree(feed).write(OUT/'feed.xml',encoding='utf-8',xml_declaration=True)
for page in (OUT/'teaching').rglob('*.html'):
    text=page.read_text(encoding='utf-8')
    def refresh(match):
        path=html.unescape(match.group(1))
        available=(OUT/path.lstrip('/')).is_file()
        detail=f'<a href="{html.escape(path,quote=True)}" download>Download slides ↗</a>' if available else '<span>Coming soon</span>'
        return f'<div class="week" data-slide-path="{html.escape(path,quote=True)}"><strong>{match.group(2)}</strong>{detail}</div>'
    text=re.sub(r'<div class="week" data-slide-path="([^"]+)"><strong>([^<]+)</strong>.*?</div>',refresh,text,flags=re.S)
    page.write_text(text,encoding='utf-8')
