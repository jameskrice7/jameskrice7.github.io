"""Run after `quarto render site`. Uses only the Python standard library."""
from pathlib import Path
import hashlib,json,sys,urllib.parse,html.parser,collections
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'site/_site'
errors=[]
def hash_file(path):
    data=path.read_bytes()
    if path.suffix.lower() not in ['.pdf','.png','.jpg','.jpeg','.gif','.ico','.woff','.woff2','.ttf','.eot','.zip']:
        try:
            data.decode('utf-8')
            data=data.replace(b'\r\n',b'\n')
        except UnicodeDecodeError:pass
    return hashlib.sha256(data).hexdigest()
manifest=json.loads((ROOT/'migration/original-files.json').read_text(encoding='utf-8'))
for name,digest in manifest.items():
    p=ROOT/name
    if not p.exists() or hash_file(p)!=digest:
        errors.append('Original file changed or missing: '+name)
def resolve(url,base='/'):
    u=urllib.parse.urlparse(urllib.parse.urljoin('https://jameskrice7.github.io'+base,url))
    if u.netloc!='jameskrice7.github.io':return None
    path=OUT/urllib.parse.unquote(u.path).lstrip('/')
    if path.is_dir():path=path/'index.html'
    return path
live=json.loads((ROOT/'migration/live-urls.json').read_text())
for url in set(live):
    if not resolve(url).is_file():errors.append('Missing live URL: '+url)
asset_count=0
for name,digest in manifest.items():
    if name.startswith(('files/','images/','assets/','talkmap/')) and not name.endswith(('.md','.qmd')):
        p=OUT/name
        if not p.exists() or hash_file(p)!=digest:errors.append('Asset changed or missing: '+name)
        asset_count+=1
content=json.loads((ROOT/'migration/content-map.json').read_text(encoding='utf-8'))
body_count=0
for item in content:
    p=resolve(item['url'])
    if not p.is_file():errors.append('Content page missing: '+item['source'])
    if item['source'].split('/')[0] in ['_publications','_working_papers','_talks','_writing','_training','_service_and_leadership','_portfolio','_posts']:
        original=(ROOT/item['source']).read_text(encoding='utf-8-sig').split('---',2)[2].strip()
        converted=ROOT/'site'/item['url'].strip('/')/'index.qmd'
        if original not in converted.read_text(encoding='utf-8'):
            errors.append('Content body changed: '+item['source'])
        body_count+=1
class Links(html.parser.HTMLParser):
    def __init__(self):super().__init__();self.urls=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if (tag in ['a','link'] and k=='href') or (tag in ['img','script','iframe'] and k=='src'):
                if v:self.urls.append(v)
broken=[]
for p in OUT.rglob('*.html'):
    if any(x in p.relative_to(OUT).parts for x in ['site_libs','assets','talkmap']):continue
    parser=Links();parser.feed(p.read_text(encoding='utf-8'))
    base='/'+p.relative_to(OUT).as_posix()
    for url in parser.urls:
        if url.startswith(('#','mailto:','tel:','data:','javascript:')):continue
        dest=resolve(url,base)
        if dest is not None and not dest.is_file():broken.append({'page':base,'target':url})
# Legacy template demonstration pages can contain example links; record separately.
legacy=['/markdown/','/archive-layout-with-content/','/portfolio/','/posts/','/terms/','/markdown_generator/']
preexisting=[b for b in broken if any(b['page'].startswith(p) for p in legacy)]
actionable=[b for b in broken if b not in preexisting]
errors.extend('Broken link: '+str(b) for b in actionable)
report={'original_files_verified':len(manifest),'live_urls_verified':len(set(live)),'static_assets_verified':asset_count,'content_pages_verified':len(content),'unmodified_content_bodies_verified':body_count,'legacy_example_link_issues':preexisting,'errors':errors}
(ROOT/'migration/verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
sys.exit(bool(errors))
