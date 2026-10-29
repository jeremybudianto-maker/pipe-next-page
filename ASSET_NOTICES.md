# Asset review — private portfolio archive

Jeremy authorized a private archive of this source and its included assets. Public reuse remains unestablished. The current source has no general project license. This document records observed attribution and open review items; it does not grant rights or determine whether a particular use is permitted.

| Asset | Evidence | Publication review |
| --- | --- | --- |
| `oracle.webp` | Source credits identify The Oracle Comes: art by Barz, original story by Teensy; © Barz, Teensy / DYNA BOOKS. Source: https://taiwan-comic-city.taicca.tw/book?id=246&lang=en | Confirm redistribution and screenshot rights, or replace with original/cleared imagery. |
| `dayoff.webp` | Source credits identify Day Off by Dailygreens (每日青菜); © Dailygreens / Rusuban Studio. Source: https://taiwan-comic-city.taicca.tw/book?id=47&lang=en | Confirm redistribution and screenshot rights, or replace with original/cleared imagery. |
| `hero.webp`, `team.webp`, `history.webp`, `artist.webp` | Local source metadata labels these user-supplied illustrations. | Confirm creator, creation process, ownership, and permission to publish. Visual appearance alone does not establish provenance. |
| `inter-latin-400-700.woff2` | Bundled `inter-OFL.txt` contains the SIL Open Font License; `build.py` embeds that license into the HTML. | Preserve the supplied font license when redistributing the font or export. |
| `docs/images/*.png` | Existing local screenshots of the application. | Screenshots reproduce included artwork and covers. Keep them private until public image reuse is cleared. |

The generated `dist/index.html` includes all six image files as base64 data. Removing images from `assets/` alone does not remove them from an existing export. Rebuild and inspect the export after replacing assets.

The original `assets/user-art-sources.json` records absolute temporary clipboard paths. Use this summary for portfolio attribution; do not publish the raw path-bearing metadata. Original `.openai/hosting.json` records a hosting project ID and deployment configuration and should be omitted from the new portfolio repository.

The team chapter displays named presentation roles. Confirm that this is intended public content and clarify team contributions before publishing. Do not present a classroom or concept team as a verified operating company.
