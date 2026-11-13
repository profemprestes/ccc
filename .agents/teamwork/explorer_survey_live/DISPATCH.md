## 2026-11-13T07:53:55Z
From: 1eedd68c-0ce9-4485-989e-8431de805c8e (parent)
Role: Live Site & Production Parity Explorer
Working directory: d:\repositorios\ccc
State folder: d:\repositorios\ccc\.agents\teamwork\explorer_survey_live

Mission:
Inspect and audit the live production website https://www.enviosdosruedas.com/ and contrast it with the local repository assets:
1. Navigate and explore the live website https://www.enviosdosruedas.com/ (use available browser automation, curl/powershell web requests, devtools, or search tools).
2. Discover and map all active public URLs, subpages, and navigation paths on the production site.
3. Test functional and interactive elements in production: WhatsApp contact buttons/links, phone links, contact forms, navigation links, social media links, tracking/quote calculators if any.
4. Contrast live pages and resources with the local static pages in `envios/` and assets in `public/`:
   - Are the local pages deployed 1:1, or is production different (e.g., WordPress, Next.js, or older/newer version)?
   - Which pages exist in the repo that are missing or different on the live site?
   - Identify content mismatches, pricing/service discrepancies, outdated copy, broken links, SSL/security or response issues on the live site.
5. Record findings with full URLs, status codes, and comparisons against local file counterparts.

Deliverables:
- Maintain `progress.md` with timestamps in your state folder.
- Write your comprehensive survey report to `d:\repositorios\ccc\.agents\teamwork\explorer_survey_live\report.md`.
- Write your structured `handoff.md` in your state folder following the Handoff Protocol.
- When finished, send a completion message to parent with the summary and report path.
