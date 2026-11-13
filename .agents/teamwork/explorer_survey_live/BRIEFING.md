# BRIEFING — 2026-11-13T08:15:00Z

## Mission
Audit the live production website https://www.enviosdosruedas.com/ and contrast it with local repository assets (envios/, public/).

## 🔒 My Identity
- Archetype: explorer
- Roles: Live Site & Production Parity Explorer
- Working directory: d:\repositorios\ccc
- State folder: d:\repositorios\ccc\.agents\teamwork\explorer_survey_live
- Original parent: 1eedd68c-0ce9-4485-989e-8431de805c8e
- Milestone: live-site-and-parity-audit

## 🔒 Key Constraints
- Read-only investigation — do NOT implement
- Write only to .agents/teamwork/explorer_survey_live/
- Never place source code or tests in .agents/teamwork/

## Current Parent
- Conversation ID: 1eedd68c-0ce9-4485-989e-8431de805c8e
- Updated: 2026-11-13T08:15:00Z

## Investigation State
- **Explored paths**:
  - Live production URLs (all 19 sitemap URLs + redirects + protected endpoints /admin, /revisar)
  - SSL certificate and HTTP headers (Vercel, Next.js App Router, Turbopack, CSP, HSTS)
  - Local repository assets: 16 HTML files in `envios/`, font assets in `public/fuentes/`, `public/logo_nuevo.webp`
  - Visual design and Superdesign metadata in `.superdesign/` and `diseno-envios/`
- **Key findings**:
  1. Production is Next.js on Vercel with Turbopack, App Router, SSR/ISR prerendering, and clean self-hosted assets.
  2. Local files in `envios/` are NOT raw Next.js code; they are static DOM clone exports generated via Superdesign (evidenced by hundreds of `data-sd-id` attributes and Bitwarden `bis_skin_checked` markers).
  3. Critical corruption: `envios/terminos-y-condiciones.html` is an exact binary duplicate of `envios/logistica-dosruedas.html` (SHA256 D82177D1...); real production terms are missing locally.
  4. Orphan duplicate: `envios/html.html` is an unminified duplicate export of `home.html` (512 KB vs 410 KB).
  5. Missing live pages: `/cobertura/` (238 KB), `/guias/envios-flex-mar-del-plata/` (105 KB), and `/servicios/` (213 KB) exist live in 200 OK production but have NO corresponding file in `envios/`.
  6. External Supabase asset vulnerability: All 31 images across `envios/*.html` point to an external Supabase bucket (`clone-assets`). No image assets exist locally in `public/` (except `logo_nuevo.webp`).
  7. SEO/Sitemap flaws: All `sitemap.xml` URLs lack trailing slashes, forcing 308 redirects on every hit. `/servicios/plan-emprendedores` and `/servicios/envios-contrareembolso` are phantom URLs that 308 redirect.
- **Unexplored areas**: None. Comprehensive live audit and parity comparison complete.

## Key Decisions Made
- Performed deep automated crawl using Python and curl outside sandbox (`BypassSandbox: true`).
- Extracted and cross-compared metadata, titles, canonicals, pricing, forms, WhatsApp links, and asset sources.

## Artifact Index
- DISPATCH.md — incoming instructions
- BRIEFING.md — persistent situational awareness
- progress.md — task heartbeat
- audit_full_data.json — complete raw JSON dataset of live and local audit
- report.md — comprehensive survey report
- handoff.md — 5-component handoff document
