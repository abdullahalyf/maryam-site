# Notes for coding agents
- Content lives in `personal/profile.yaml`, `content/blog/` and `personal/`. Do not hard-code copy in templates.
- Style `bloom` is in `themes/folio/assets/css/styles/bloom.css`. Keep the rules: one accent colour (dusty rose) only for buttons/links, hairlines not boxes, one CSS-only entrance animation, respect `prefers-reduced-motion`.
- Never invent facts about Maryam. Empty value = hidden section.
- Build check: `hugo --gc --minify` must give zero ERROR/WARN.
