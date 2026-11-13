# Project: Auditoría Integral Envíos DosRuedas

## Architecture
- **Target Repository**: `d:\repositorios\ccc`
- **Reference Production Site**: `https://www.enviosdosruedas.com/`
- **Evaluated Layers**:
  1. **Brand & Visual Design**: Design tokens in `contexto/globals.css`, brand specifications in `.superdesign/` and `disenos/`, visual assets in `public/`, `diseno-envios/`, `disenos/`.
  2. **Code & Technical Quality**: 16 HTML pages in `envios/`, inlined CSS, scripts, DOM structure, accessibility (WCAG), SEO meta tags, performance indicators.
  3. **Content & Usability**: Contact endpoints, WhatsApp CTAs, pricing, terms & conditions, FAQ, forms, navigation.
  4. **Live Site Parity & Infrastructure**: Next.js App Router on Vercel Edge (`gru1`), DNS/SSL/HTTP headers, routes, redirects, sitemap.xml, missing pages.

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
- **Input Documents**: `ORIGINAL_REQUEST.md`, Survey reports (`explorer_survey_code/report.md`, `explorer_survey_brand/report.md`, `explorer_survey_live/report.md`, `explorer_survey_live/audit_full_data.json`).
- **Primary Deliverable**: `d:\repositorios\ccc\INFORME_AUDITORIA_ENVIOS_DOSRUEDAS.md` structured into:
  - 1. Resumen Ejecutivo (Visión general, puntuación global y por dimensión 1.0 a 5.0, vulnerabilidades críticas P0).
  - 2. Alcance, Metodología e Inventario de Activos (Inventario exhaustivo de archivos, hashes SHA-256, herramientas y métodos).
  - 3. Rúbrica Estructurada de Auditoría (4 dimensiones ponderadas, evaluación punto por punto con puntaje 1-5 y justificación empírica).
  - 4. Diagnóstico Detallado por Áreas (Marca, Código/Técnica, Contenidos/Usabilidad/Conversión, Producción/Infraestructura/SEO).
  - 5. Matriz Completa de Hallazgos e Inconsistencias (IDs H-01 a H-xx, severidades P0-P3, ubicación exacta, causa raíz, recomendación concreta).
  - 6. Plan de Recomendaciones Priorizadas y Hoja de Ruta de Remediación (P0 Inmediato 24-48h, P1 Corto Plazo 1-2 semanas, P2 Mediano Plazo 1 mes, P3 Largo Plazo).

## Code Layout
- Root Deliverables:
  - `d:\repositorios\ccc\INFORME_AUDITORIA_ENVIOS_DOSRUEDAS.md` (Master Audit Report)
  - `d:\repositorios\ccc\PROJECT.md` (Project definition & architecture)
- Evaluated Codebase:
  - `contexto/globals.css` (Tailwind CSS v4 design tokens)
  - `envios/` (16 HTML static page dumps)
  - `public/` (Visual assets: logo_nuevo.webp and public/fuentes/)
  - `diseno-envios/` (Hyperframes animation project)
  - `disenos/` (Design documents and envios.html)
  - `.superdesign/` (Design extraction metadata and tokens)
- State & Coordination Metadata:
  - `.agents/teamwork/` (Agent working folders, progress, handoffs)
