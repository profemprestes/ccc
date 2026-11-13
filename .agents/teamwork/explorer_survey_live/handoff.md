# Handoff Report — Live Site & Production Parity Audit

- **Agent**: Live Site & Production Parity Explorer
- **Date**: 2026-11-13T08:20:00Z
- **Working Directory**: `d:\repositorios\ccc`
- **State Folder**: `d:\repositorios\ccc\.agents\teamwork\explorer_survey_live`
- **Report Path**: `d:\repositorios\ccc\.agents\teamwork\explorer_survey_live\report.md`
- **Raw Data Artifact**: `d:\repositorios\ccc\.agents\teamwork\explorer_survey_live\audit_full_data.json`

---

## 1. Observation

1. **Production Infrastructure and HTTP Response**:
   - Command: `curl.exe -ILs https://www.enviosdosruedas.com/`
   - Observed Headers:
     - `Server: Vercel`
     - `X-Vercel-Id: gru1::...`
     - `X-Nextjs-Prerender: 1`
     - `Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://maps.googleapis.com https://*.googletagmanager.com https://www.googletagmanager.com https://*.google-analytics.com https://*.googleadservices.com https://*.doubleclick.net https://googleads.g.doubleclick.net https://analytics.ahrefs.com https://unpkg.com; ... form-action 'self' https://api.whatsapp.com; ...`
     - `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`
     - `Vary: rsc, next-router-state-tree, next-router-prefetch, next-router-segment-prefetch`
   - DNS Resolution: `64.29.17.65`, `64.29.17.1`.
   - SSL Certificate: Issued by Let's Encrypt (`CN=YR1`), subject `*.enviosdosruedas.com`, SAN `*.enviosdosruedas.com, enviosdosruedas.com`, valid Oct 14 17:14:14 2026 GMT to Jan 12 17:14:13 2027 GMT, TLSv1.3 (`TLS_AES_128_GCM_SHA256`).

2. **Public URLs and Redirects**:
   - `https://www.enviosdosruedas.com/robots.txt` returned HTTP 200 (458 bytes), declaring `Disallow: /api/`, `Disallow: /admin/`, `Disallow: /revisar` and `Sitemap: https://www.enviosdosruedas.com/sitemap.xml`.
   - `https://www.enviosdosruedas.com/revisar/` and `/admin/` return HTTP 401 Unauthorized.
   - `https://www.enviosdosruedas.com/sitemap.xml` returned HTTP 200 with 19 `<loc>` entries.
   - All entries in `sitemap.xml` lack trailing slashes (e.g. `/contacto`), while server enforces `trailingSlash: true`, returning `HTTP/1.1 308 Permanent Redirect` to the trailing-slash URL (`/contacto/`).
   - `/servicios/plan-emprendedores` returned `308 Permanent Redirect` -> `/servicios/empresas-cuenta-corriente/`.
   - `/servicios/envios-contrareembolso` returned `308 Permanent Redirect` -> `/servicios/`.
   - `/servicios/enviosflex` returned HTTP 200 OK, but `/servicios/envios-flex/` returned HTTP 404 Not Found.
   - `/servicios/` returned HTTP 200 OK (213.535 bytes) but is absent from `sitemap.xml`.
   - `/cobertura/` returned HTTP 200 OK (238.048 bytes).
   - `/guias/envios-flex-mar-del-plata/` returned HTTP 200 OK (105.275 bytes).

3. **Local File Hashes and Corruption**:
   - Command: `Get-FileHash envios/logistica-dosruedas.html, envios/terminos-y-condiciones.html`
   - Observed SHA256:
     - `envios/logistica-dosruedas.html`: `D82177D1DF7E1F9D0004831753C35D367A68AE9158A02BC84AD701DF3FD15C8E`
     - `envios/terminos-y-condiciones.html`: `D82177D1DF7E1F9D0004831753C35D367A68AE9158A02BC84AD701DF3FD15C8E`
   - Both files have identical size (235.560 bytes) and identical content (Title: "Logística DosRuedas | Seguimiento y Portales Digitales - Mar del Plata | Envíos DosRuedas").
   - Live URL `https://www.enviosdosruedas.com/terminos-y-condiciones/` returned HTTP 200 (122.706 bytes), Title: "Términos y Condiciones | Envíos DosRuedas", H1: "Términos y Condiciones".

4. **DOM Attributes and Provenance of `envios/`**:
   - In all 16 files under `envios/*.html`, every file contains hundreds of `data-sd-id="..."` attributes (range: 393 in `serviciosempresas-cuenta-corriente.html` to 950 in `home.html` and `html.html`) and Bitwarden extension markers `bis_skin_checked="1"` (range: 139 to 388).
   - In live production HTML, `data-sd-id` count is 0 and `bis_skin_checked` count is 0.
   - `envios/html.html` has 512.198 bytes, identical Title and H1 to `home.html` (410.547 bytes), and contains expanded DOM indentation and attributes.

5. **Asset Dependencies**:
   - Across all 16 files in `envios/*.html`, there are 31 unique `<img src="...">` URLs. All 31 URLs point to:
     `https://vgbujcuwptvheqijyjbe.supabase.co/storage/v1/object/public/clone-assets/<hash>.(webp|png|svg)`.
   - In local directory `public/`, only 1 image exists: `public/logo_nuevo.webp` (36.454 bytes). All other files under `public/` are font files under `public/fuentes/`.
   - On live production, images are served from local relative paths: `/logo-envios-simplified.webp`, `/heroes/inicio-mapa.webp`, `/cards/fondo_*.webp`.

6. **Interactive Elements and Contact Data**:
   - Primary WhatsApp phone across all pages: `+54 9 223 660-2699` (`542236602699`).
   - Tel link: `tel:+542236602699`.
   - Mail link: `mailto:matiascejas@enviosdosruedas.com`.
   - Live `/cotizar/` has interactive inputs (`guia-origen-input`, `guia-destino-input`, `nombre`, `telefono`, `producto`) and button "Ver las dos tarifas".
   - Live `/logistica-dosruedas/` has tracking code input and buttons `EDR-4820-MDQ`, `EDR-999-OK`, `MELI-FLEX-MDQ`.
   - Live `/mardelivery/` links to food delivery QR / digital menu platform.
   - External platforms linked: `https://www.logisticadosruedas.com/` and `https://shopdosruedas.com`.

---

## 2. Logic Chain

1. From Observation 1 (`Server: Vercel`, `X-Nextjs-Prerender: 1`, Next.js RSC headers, Turbopack script bundles), the live production site is an active Next.js App Router application hosted on Vercel.
2. From Observation 4 (`data-sd-id` ranging from 393 to 950 in local files, but 0 in live production; Bitwarden `bis_skin_checked` in local files; and git history containing `.superdesign/website/enviosdosruedas.com/`), the local files in `envios/*.html` are not the original Next.js source code, but DOM captures exported from a Superdesign visual editing session in a browser.
3. From Observation 3 (exact SHA256 match between `logistica-dosruedas.html` and `terminos-y-condiciones.html`), an export or file management accident overwrote the local Terms and Conditions file with the Logistics tracking page, destroying local legal terms that exist in live production.
4. From Observation 2 (`/cobertura/`, `/guias/envios-flex-mar-del-plata/`, and `/servicios/` responding with 200 OK and heavy page sizes in live production), these 3 active pages were never exported to `envios/`, resulting in an incomplete local repository.
5. From Observation 5 (all 31 images in `envios/*.html` pointing to Supabase `clone-assets`, with 0 corresponding files in `public/`), the local HTML files have a fragile third-party dependency. If the Supabase bucket is deleted, all local pages will suffer complete image breakage.
6. From Observation 2 (sitemap URLs lacking trailing slashes while Vercel enforces `trailingSlash: true`), all crawlers incur an extra 308 redirect hop for every URL. Additionally, phantom URLs (`plan-emprendedores`, `envios-contrareembolso`) and the missing hyphen redirect for `/servicios/envios-flex/` create SEO inefficiencies.

---

## 3. Caveats

- **Next.js Source Code**: The original Next.js source project (e.g. `package.json`, `app/`, `components/`, API routes) is not present in this git repository (`ccc`), which only contains static reference files, Tailwind v4 design tokens, and the exported HTML clones.
- **Backend / Authentication**: The credentials or backend logic behind `/admin/` and `/revisar/` (returning 401 Unauthorized) were not inspected beyond verifying HTTP status and response headers, as access is restricted.

---

## 4. Conclusion

The live site `https://www.enviosdosruedas.com/` is a production-grade, secure Next.js site running on Vercel. However, the local repository contains significant parity defects:
1. `envios/terminos-y-condiciones.html` is corrupted (duplicated from `logistica-dosruedas.html`).
2. Three active live routes (`/cobertura/`, `/guias/envios-flex-mar-del-plata/`, `/servicios/`) are completely missing locally.
3. All local images depend on a remote Supabase temporary bucket (`clone-assets`) and are absent from `public/`.
4. `envios/html.html` is an unminified orphan duplicate of `home.html`.
5. Production `sitemap.xml` contains trailing-slash redirect inefficiencies and phantom URLs.

Restoration of `terminos-y-condiciones.html`, extraction of the 3 missing pages, localizing all images into `public/`, and updating `sitemap.xml` are required to achieve parity and repository integrity.

---

## 5. Verification Method

To independently verify all findings and parity comparisons:

1. **Verify Corrupted Duplicate in Local Repository**:
   ```powershell
   Get-FileHash envios/logistica-dosruedas.html, envios/terminos-y-condiciones.html
   ```
   *Expected Result*: Identical SHA-256 hash `D82177D1DF7E1F9D0004831753C35D367A68AE9158A02BC84AD701DF3FD15C8E`.

2. **Verify Real Terms and Conditions in Live Production**:
   ```powershell
   curl.exe -s https://www.enviosdosruedas.com/terminos-y-condiciones/ | Select-String -Pattern '<title>(.*?)</title>'
   ```
   *Expected Result*: `<title>Términos y Condiciones | Envíos DosRuedas</title>`.

3. **Verify Live-Only Pages Missing Locally**:
   ```powershell
   curl.exe -ILs https://www.enviosdosruedas.com/cobertura/
   curl.exe -ILs https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata/
   curl.exe -ILs https://www.enviosdosruedas.com/servicios/
   ```
   *Expected Result*: All return `HTTP/1.1 200 OK` (Content-Length > 100 KB). None exist in `envios/`.

4. **Verify Supabase Image Dependency in `envios/`**:
   ```powershell
   Select-String -Path 'envios/*.html' -Pattern 'https://vgbujcuwptvheqijyjbe.supabase.co' | Measure-Object
   ```
   *Expected Result*: 31+ occurrences across all HTML files.

5. **Verify Trailing Slash Redirection in Sitemap**:
   ```powershell
   curl.exe -ILs https://www.enviosdosruedas.com/contacto
   ```
   *Expected Result*: `HTTP/1.1 308 Permanent Redirect` with `Location: /contacto/`.
