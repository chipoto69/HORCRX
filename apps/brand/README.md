# `@horcrx/brand`

Static wrapper for the inherited HORCRX brand canon.

- `index.html` symlinks to `packages/design-system/applications/landing.html`
- `preview/` symlinks to `packages/design-system/preview/`
- `assets/`, `fonts/`, and `colors_and_type.css` symlink to the inherited design system so the original files stay canonical

Serve locally from this directory with:

```sh
pnpm --filter @horcrx/brand dev
```
