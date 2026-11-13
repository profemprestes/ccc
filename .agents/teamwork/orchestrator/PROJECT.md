# Project: Auditoría Integral Envíos DosRuedas

## Architecture
- **Target Repository**: `d:\repositorios\ccc`
- **Reference Production Site**: `https://www.enviosdosruedas.com/`
- **Evaluated Layers**:
  1. Brand & Visual Design: Design tokens in `contexto/globals.css`, brand specifications in `.superdesign/` and `disenos/`, visual assets in `public/`, `diseno-envios/`, `disenos/`.
  2. Code & Technical Quality: 16 HTML pages in `envios/`, inlined CSS, scripts, DOM structure, accessibility (WCAG), SEO meta tags, performance indicators.
  3. Content & Usability: Contact endpoints, WhatsApp CTAs, pricing, terms & conditions, FAQ, forms, navigation.
  4. Live Site Parity & Infrastructure: Next.js on Vercel Edge (`gru1`), DNS/SSL/HTTP headers, routes, redirects, sitemap.xml, missing pages.

## Feature / Asset Inventory
| # | Asset / Area | Description | Milestone | Source |
|---|--------------|-------------|-----------|--------|
| 1 | `contexto/globals.css` | 370 lines Tailwind v4 tokens (Sistema Lúcido, Ley de Tres Colores, double-bezel) | M1 | Survey Code/Brand |
| 2 | `envios/*.html` (16 pages) | Static HTML DOM clones (home, contacto, cotizar, logistica, mardelivery, etc.) | M1 | Survey Code |
| 3 | `public/logo_nuevo.webp` | Official 640x640 WebP logo (orphaned, 0 references in code) | M1 | Survey Brand |
| 4 | `public/fuentes/` | 86 TTF font files totaling 13.2 MB (60 unused static weights totaling 12 MB) | M1 | Survey Brand |
| 5 | `diseno-envios/` | Hyperframes config referencing missing assets folder; unstyled index.html | M1 | Survey Brand |
| 6 | `disenos/envios-design.md` | DosRuedas Electric Dispatch specification & design tokens | M1 | Survey Brand |
| 7 | `.superdesign/` | Brand manual outline, brand.json, design.md | M1 | Survey Brand |
| 8 | Universal Click Killswitch | Trailing script with `e.preventDefault()` breaking all navigation & WhatsApp links | M1 | Survey Code |
| 9 | Duplicate & Missing Legal Page | `terminos-y-condiciones.html` is binary clone of `logistica-dosruedas.html` (real legal text missing locally) | M1 | Survey Code/Live |
| 10| Duplicate `html.html` | 500 KB redundant copy of `home.html` | M1 | Survey Code |
| 11| Malformed filename | `nossobresobre-nosotros.html` duplicate prefix | M1 | Survey Code/Brand |
| 12| CSS Bloat (2.14 MB) | 121-193 KB of compiled Tailwind CSS inlined in each HTML page (45.4% of total size) | M1 | Survey Code |
| 13| Supabase Image Dependency | 100% of images (31 unique hashes) point to remote Supabase `clone-assets` bucket | M1 | Survey Brand/Live |
| 14| Missing Interactivity | `#mobile-menu-toggle-opt` references nonexistent `#mobile-navigation-dialog`; forms lack actions | M1 | Survey Code |
| 15| Live Production Infrastructure | Next.js App Router on Vercel Edge (`gru1`), Let's Encrypt TLSv1.3 SSL, HSTS, strict CSP | M1 | Survey Live |
| 16| Production Missing Pages | `/cobertura/`, `/guias/envios-flex-mar-del-plata/`, `/servicios/` active in prod but missing locally | M1 | Survey Live |
| 17| Production Sitemap & SEO | Sitemap URLs lack trailing slashes (forcing 308 redirects); phantom URLs; `/servicios/envios-flex/` 404 | M1 | Survey Live |
| 18| Scraper & Extension Artifacts | `data-sd-id` (393-950 per file), Bitwarden `bis_skin_checked="1"`, `cursor:pointer` on body | M1 | Survey Code |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Comprehensive Audit Report & Rubric Generation | Synthesize all survey findings into master audit document `INFORME_AUDITORIA_ENVIOS_DOSRUEDAS.md` and root `PROJECT.md` | Survey Complete | IN_PROGRESS |
| M2 | Multi-Reviewer & Adversarial Challenge | Dispatched reviewers (`teamwork_reviewer`) & challengers (`teamwork_challenger`) verify accuracy, completeness, empirical proofs, and acceptance criteria | M1 | PLANNED |
| M3 | Forensic Integrity Audit & Gate Pass | Forensic Auditor (`teamwork_auditor`) validates authenticity of all data, commands, hashes, and findings | M2 | PLANNED |

## Interface Contracts
- **Input Documents**: `ORIGINAL_REQUEST.md`, Survey reports (`explorer_survey_code/report.md`, `explorer_survey_brand/report.md`, `explorer_survey_live/report.md`).
- **Output Artifact**: `INFORME_AUDITORIA_ENVIOS_DOSRUEDAS.md` (root) adhering to Markdown structure:
  - 1. Resumen Ejecutivo
  - 2. Alcance y Metodología
  - 3. Rúbrica Estructurada de Auditoría (Punto por punto: Criterio, Ponderación, Puntuación 1-5, Justificación empírica)
  - 4. Diagnóstico Detallado por Áreas (Marca, Código/Técnica, Contenido/Funcionalidad, Producción/Paridad)
  - 5. Matriz Completa de Hallazgos e Inconsistencias (ID, Severidad, Dimensión, Ubicación exacta, Problema, Recomendación)
  - 6. Plan de Recomendaciones Priorizadas y Hoja de Ruta (P0 a P3)

## Code Layout
- Root: `INFORME_AUDITORIA_ENVIOS_DOSRUEDAS.md`, `PROJECT.md`
- State metadata: `.agents/teamwork/`
