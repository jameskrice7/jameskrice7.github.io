# Quarto migration: review and launch

This branch adds a Quarto website in `site/`. The 385 original files remain unchanged at the repository root, and the full Git history is retained. The source snapshot is commit `63130fd45e37b8d2ed7650f86b8938a50e620661`.

## Preview

Install Quarto 1.10.18, then run:

```sh
quarto preview site
```

To build and check preservation:

```sh
quarto render site
python migration/verify.py
```

The GitHub workflow builds a downloadable preview artifact on this branch and on pull requests. It does not deploy to the live website.

## What was migrated

- 6 publications, 7 working papers, 32 talks, 5 writing entries, 2 teaching dashboards, 10 training entries, and 1 service entry.
- 2 portfolio examples and 5 sample blog posts, plus the original utility pages.
- Biography, affiliations, contact/profile links, CV, all three writing portfolio PDF embeds, and weekly seminar download links.
- Original page metadata is retained under `legacy` in each migrated content page and in `migration/content-map.json`.
- Existing drafts remain in the original `_drafts/` directory and are not published.
- Original assets are copied without modification. The verification script checks file hashes, all 128 distinct sitemap URLs, and internal file links.

## Existing issues handled

Two sample blog posts had the same permalink, `/posts/2012/08/blog-post-4/`. The live site serves the future sample at that address, so it retains that address. The previously shadowed 2015 post has a separate address, `/posts/2015/08/blog-post-4/`, so both texts are available. The extensionless `_writing/writing_4` article is also migrated.

Old extensionless article paths resolve through directory indexes (GitHub Pages adds the trailing slash). Capitalization is preserved. Declared legacy aliases such as `/resume`, `/md/`, and `/nmp.html` have redirect pages.

The research headline and short introduction on the homepage are proposed editorial copy. Original biography and scholarly text remain available. Original CV dates, publication statuses, and calls for papers were preserved rather than independently fact-checked.

## Editing after migration

- Homepage: `site/index.qmd`; global design: `site/styles.css`; homepage design: `site/home.css`.
- Navigation and site settings: `site/_quarto.yml`.
- Articles: `site/publications/<original-name>/index.qmd` and equivalent collection directories.
- Publication, talk, writing, and CV lists are editable page content. When adding a new item, update its relevant index and CV as appropriate.
- Teaching PDFs: `site/files/teaching/<course>/seminar-materials/slides/week-NN.pdf`. The post-render script detects available files and changes the matching dashboard placeholder to a download link.
- Original root Jekyll files are retained as the migration archive; edit the Quarto files for the new site.

## Launch

1. Review the preview, especially the homepage wording and mobile layout.
2. Re-check the live repository for intervening commits before merging. Import any new content into Quarto first.
3. Copy `migration/deploy-quarto.yml.example` to `.github/workflows/deploy-quarto.yml`.
4. Merge the migration into `master` and set repository **Settings → Pages → Source → GitHub Actions**.
5. Run the publish workflow and check the live homepage, a publication, a teaching download, and the CV.

The hostname remains `jameskrice7.github.io`. The source files, history, and build remain in the same repository.

## Rollback

Disable the Quarto publish workflow and restore the previous GitHub Pages source configuration. For an exact old-site recovery, create a branch at the snapshot commit above and publish Jekyll from that branch. Do not delete the repository or force-push its history. A separate full-history Git bundle was also saved locally with the migration deliverables.

The preservation check is a migration guard, not a fact-check of external sites or a guarantee of search-engine ranking. Re-run it before cutover; check live redirects after deployment.
