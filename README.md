# BlackRoad-Interactive RoadCode

Canonical RoadCode workspace and automation hub for BlackRoad-Interactive.

## What Lives Here

- RoadCode landing page and deploy surface
- org-specific operator workflows
- automation entrypoints for GitHub, Gitea, Slack, and Cloudflare

## Deploy

This repo ships a static site from site/ to Cloudflare Pages.

- Pages URL: https://blackroad-interactive-roadcode.pages.dev
- Expected project name: blackroad-interactive-roadcode

## Operator Notes

- Default branch: main
- Workflow: .github/workflows/roadcode-pages.yml
- Site entrypoint: site/index.html
