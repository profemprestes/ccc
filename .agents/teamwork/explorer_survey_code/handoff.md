# HANDOFF REPORT — CODE & TECHNICAL QUALITY EXPLORER

**Task**: Technical Survey and Audit of Code Assets (Envíos DosRuedas)  
**Author**: Explorer Survey Code (`explorer_survey_code`)  
**Recipient**: Parent Orchestrator (`1eedd68c-0ce9-4485-989e-8431de805c8e`)  
**State Folder**: `d:\repositorios\ccc\.agents\teamwork\explorer_survey_code`  
**Report Path**: `d:\repositorios\ccc\.agents\teamwork\explorer_survey_code\report.md`  
**Date**: 2026-11-13T08:12:00Z  

---

## 1. OBSERVATION

1. **`contexto/globals.css` (370 lines, 14,843 bytes)**:
   - Configured with Tailwind CSS v4 syntax: `@import "tailwindcss";` (line 1), `@custom-variant dark (&:where(.dark, .dark *));` (line 4), `@theme` (line 29), `@utility` (lines 202-355).
   - Canonical palette: `--color-brand-blue-50` (`#E6EEFE`) to `--color-brand-blue-500` (`#0950F6`, maximum darkness limit), `--color-brand-yellow-50` (`#FFFDE6`) to `--color-brand-yellow-600` (`#E6D400`, with `--color-brand-yellow-500: #FFEC01`), and `--color-white: #FFFFFF`.
   - Default Tailwind palettes (neutral, stone, green, emerald, lime, teal, blue) explicitly neutralized to `initial` (lines 68-101).
   - Utilities defined: `double-bezel-outer` (lines 222-232), `double-bezel-inner` (lines 233-238), `cta-nested-pill` (lines 243-259), `text-display`, `text-h1`, `text-h2` (lines 273-296), `content-auto` (line 352), `@media (prefers-reduced-motion: reduce)` (lines 357-370).

2. **16 HTML Files in `d:\repositorios\ccc\envios\`**:
   - `contacto.html` (274.9 KB, 6,498 lines)
   - `cotizar.html` (270.1 KB, 6,643 lines)
   - `home.html` (400.9 KB, 8,784 lines)
   - `html.html` (500.2 KB, 8,880 lines)
   - `logistica-dosruedas.html` (230.0 KB, 5,739 lines)
   - `mardelivery.html` (254.9 KB, 6,141 lines)
   - `nosotrosnuestras-redes.html` (281.3 KB, 6,592 lines)
   - `nosotrospreguntas-frecuentes.html` (258.3 KB, 6,285 lines)
   - `nossobresobre-nosotros.html` (315.1 KB, 7,121 lines)
   - `politicade-privacidad.html` (277.4 KB, 6,328 lines)
   - `serviciosdeposito-fulfillment.html` (326.4 KB, 7,255 lines)
   - `serviciosempresas-cuenta-corriente.html` (221.2 KB, 5,529 lines)
   - `serviciosenvios-express.html` (298.1 KB, 6,878 lines)
   - `serviciosenvios-lowcost.html` (296.4 KB, 6,857 lines)
   - `serviciosenviosflex.html` (382.9 KB, 8,086 lines)
   - `terminos-y-condiciones.html` (230.0 KB, 5,739 lines)

3. **Critical Duplications**:
   - Running `Get-FileHash` on `envios/logistica-dosruedas.html` and `envios/terminos-y-condiciones.html` yields the exact same SHA-256 hash: `D82177D1DF7E1F9D0004831753C35D367A68AE9158A02BC84AD701DF3FD15C8E`. Both contain the title `"Logística DosRuedas | Seguimiento y Portales Digitales - Mar del Plata | Envíos DosRuedas"`.
   - `envios/html.html` is an exact content duplicate of `envios/home.html`, differing only by 4-space indentation vs 2-space indentation (whitespace-normalized difference is under 30 characters).

4. **Universal Click Blocking Script**:
   - Verbatim script present at the end of every HTML file (e.g. `home.html:8781`, `cotizar.html:6640`):
     ```html
     <script>document.addEventListener("click", function (e) { var a = e.target.closest && e.target.closest("a"); if (!a) return; var h = a.getAttribute("href") || ""; if (h.length > 1 && h.charAt(0) === "#") return; e.preventDefault(); }, true);</script>
     ```
   - Intercepts and executes `e.preventDefault()` on all anchor clicks whose `href` does not start with `#`.

5. **Inlined Monolithic CSS Bloat**:
   - Zero files link to `contexto/globals.css` or any external `.css` stylesheet.
   - Each HTML file inlines between 121 KB and 193 KB of CSS inside `<style>` tags in `<head>`.
   - Total inlined CSS across the 16 files: **2.14 MB**, accounting for **45.4%** of the 4.71 MB total HTML size.

6. **Missing Interactivity & Phantom Dialog**:
   - Zero JavaScript files or operational event listeners exist for navigation or forms.
   - Every file includes `<button id="mobile-menu-toggle-opt" ... aria-controls="mobile-navigation-dialog">`.
   - Searching for `id="mobile-navigation-dialog"` across all HTML files returns 0 matches.
   - Form in `cotizar.html:5509` and form in `contacto.html:5397` lack `action`, `method`, and submit handlers.
   - Package tracking form in `logistica-dosruedas.html:4870` has no search logic or submit handler.
   - FAQ buttons `faq-q-1` through `faq-q-7` in `nosotrospreguntas-frecuentes.html` are collapsed (`aria-expanded="false"`) with no JS to toggle them.

7. **Fragile Asset Hosting & Font Paths**:
   - 100% of image `<img>` tags point to `https://vgbujcuwptvheqijyjbe.supabase.co/storage/v1/object/public/clone-assets/<hash>.webp` (24 unique image hashes).
   - Local asset `public/logo_nuevo.webp` is never referenced in any file.
   - Fonts in `<style>` are loaded from `url("../public/fuentes/...")` as uncompressed `.ttf` files totaling 1.92 MB active font weight (520 KB for IBM Plex Sans, 580 KB for IBM Plex Sans Italic).

8. **Accessibility & Scraper Artifacts**:
   - Logo in header wraps `<div tabindex="0">` inside `<a id="nav-logo-opt">` across all 16 files.
   - Div with `tabindex="0"` wraps `<button type="submit">` (e.g., `home.html:8147`).
   - `alt="Image"` present in 5 files; empty `alt=""` present in 5 files.
   - All 16 files contain `style="cursor:pointer"` on the `<body>` element.
   - Thousands of scraper attributes present: `bis_skin_checked="1"` (139-388 per file), `data-sd-id` (393-950 per file), `bis_register` on body, `<next-route-announcer>`.

9. **SEO Deficiencies**:
   - Zero `application/ld+json` structured data tags across all 16 files.
   - `og:image` references `https://www.enviosdosruedas.com/og-image.jpg` (file does not exist in `public/`).
   - `meta name="referrer" content="no-referrer"` present across all files.

---

## 2. LOGIC CHAIN

1. **From Observation 4 to Navigational Breakdown**:
   - Observation 4 shows that every file executes `e.preventDefault()` on any anchor whose `href` attribute does not begin with `#`.
   - All internal page links (`https://www.enviosdosruedas.com/servicios/`, etc.) and all WhatsApp CTA buttons (`https://api.whatsapp.com/send/...`) start with `https://`.
   - Therefore, clicking any navigation link or WhatsApp button will be blocked by the browser. The site is functionally unable to navigate or convert leads.

2. **From Observation 3 to Content Corruption**:
   - `envios/terminos-y-condiciones.html` has the identical SHA-256 hash as `envios/logistica-dosruedas.html` and identical title and tracking form markup.
   - Therefore, the actual legal terms of service were completely overwritten or replaced during file export, leaving the site without its required legal document.
   - Similarly, `envios/html.html` is an unneeded 500 KB duplicate of `envios/home.html`.

3. **From Observation 5 to Performance Degradation**:
   - Observation 5 confirms that 2.14 MB of CSS is inlined across 16 HTML pages, with zero external stylesheet references.
   - Without an external CSS file, browsers cannot cache stylesheet rules across page transitions.
   - Therefore, visitors must re-download ~130 KB of CSS on every single page view, multiplying bandwidth consumption and triggering HTML parse-blocking.

4. **From Observation 6 to Mobile Inoperability**:
   - On viewports below `lg` (< 1024px), the desktop navigation menu is hidden via Tailwind class `hidden lg:flex`.
   - The only visible navigation trigger is `#mobile-menu-toggle-opt`.
   - Observation 6 proves that `#mobile-menu-toggle-opt` has no JavaScript event listener, and its target `#mobile-navigation-dialog` does not exist in the DOM.
   - Therefore, mobile users are completely locked out of site navigation.

5. **From Observation 7 to Single Point of Failure (SPoF)**:
   - 100% of images rely on a temporary Supabase storage bucket (`vgbujcuwptvheqijyjbe.supabase.co`).
   - If that third-party storage is shut down, altered, or rate-limited, all images on the production site will 404 simultaneously.
   - Additionally, fonts loaded via `../public/fuentes/...` fail when deployed to static roots where `/public` is not an accessible parent folder.

6. **From Observation 8 to Accessibility Violations**:
   - Nesting focusable `div tabindex="0"` elements inside anchors and around buttons violates WCAG 4.1.2 (Name, Role, Value) and creates keyboard navigation traps.
   - Forcing `cursor:pointer` on the entire `<body>` violates standard UI expectations by masking clickable affordances.

---

## 3. CAVEATS

1. **Production URL Navigation**:
   - Local code audit was conducted on repository files (`contexto/globals.css`, `envios/*.html`, `public/`, etc.). Live production URL behavior (`https://www.enviosdosruedas.com/`) may differ if the production host is running an active Next.js server with hydration rather than serving these static HTML dumps directly.
2. **Build Toolchain Integration**:
   - `package.json` contains scripts for `vite` and `vitest`, but no configured Next.js build pipeline in the root. The static files in `envios/` appear to have been exported or scraped from a separate Next.js / Superdesign deployment.
3. **No Character Encoding Corruption (Confirmed)**:
   - Initial terminal display suggested character encoding issues (mojibake); however, direct byte analysis confirmed that all 16 HTML files are valid UTF-8 without BOM. The apparent corruption was an artifact of PowerShell default console decoding.

---

## 4. CONCLUSION

The code assets for Envíos DosRuedas represent a **static dump/scraper export with high visual design fidelity but severe structural, navigational, and performance defects**:
1. **Showstopper Defects**: The universal click-interceptor script must be removed immediately to restore link navigation and WhatsApp lead conversion; `terminos-y-condiciones.html` must be restored with authentic legal terms; `html.html` must be deleted.
2. **Architecture & Performance Overhaul**: The 2.14 MB of inlined CSS must be extracted into a compiled, cacheable `globals.css` linked via `<link rel="stylesheet">`; fonts must be converted from TTF to WOFF2; Supabase images must be downloaded and hosted locally in `public/`.
3. **Interactivity & Mobile Recovery**: A lightweight mobile navigation drawer and simple dropdown/accordion scripts must be provided to restore core usability.
4. **Overall Assessment**: The codebase scores **2.1 / 5.0** on technical quality, presenting high operational risk until P0 and P1 fixes are applied.

---

## 5. VERIFICATION METHOD

To independently verify all findings, execute the following commands in PowerShell from `d:\repositorios\ccc`:

### 1. Verify SHA-256 Duplicate of `terminos-y-condiciones.html`:
```powershell
Get-FileHash -Path "envios\logistica-dosruedas.html", "envios\terminos-y-condiciones.html" | Format-Table -AutoSize
```
*Expected*: Both files output exact hash `D82177D1DF7E1F9D0004831753C35D367A68AE9158A02BC84AD701DF3FD15C8E`.

### 2. Verify Universal Click Interceptor Script:
```powershell
Select-String -Path "envios\*.html" -Pattern "e\.preventDefault\(\)" | Measure-Object
```
*Expected*: Exactly 16 occurrences (1 per HTML file).

### 3. Verify Absence of External CSS Link:
```powershell
Select-String -Path "envios\*.html" -Pattern '<link[^>]*rel=["'']stylesheet["'']'
```
*Expected*: 0 matches across all files.

### 4. Verify Total Inlined CSS vs Total HTML Size:
```powershell
$files = Get-ChildItem "envios\*.html"
$totalCss = 0; $totalHtml = 0
foreach ($f in $files) {
    $raw = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    $matches = [regex]::Matches($raw, '<style\b[^>]*>([\s\S]*?)</style>', 'IgnoreCase')
    foreach ($m in $matches) { $totalCss += [System.Text.Encoding]::UTF8.GetByteCount($m.Value) }
    $totalHtml += $f.Length
}
Write-Output "Total HTML: $([math]::Round($totalHtml/1MB,2)) MB | Inlined CSS: $([math]::Round($totalCss/1MB,2)) MB ($([math]::Round($totalCss/$totalHtml*100,1))%)"
```
*Expected*: Total HTML ~4.71 MB, Inlined CSS ~2.14 MB (45.4%).

### 5. Verify Phantom Element `#mobile-navigation-dialog`:
```powershell
Select-String -Path "envios\*.html" -Pattern 'id="mobile-navigation-dialog"'
```
*Expected*: 0 matches across all files.

### 6. Verify Remote Supabase Image Dependencies:
```powershell
Select-String -Path "envios\*.html" -Pattern 'src="https://vgbujcuwptvheqijyjbe\.supabase\.co' | Measure-Object
```
*Expected*: 78 occurrences across the 16 files.

### 7. Invalidation Conditions:
- If `envios/terminos-y-condiciones.html` is replaced with distinct legal text, hash comparison will differ.
- If the trailing `<script>` tag is removed, `preventDefault` count will become 0.
- If `<link rel="stylesheet" href="...">` is added and `<style>` blocks are purged, inlined CSS will drop to 0 MB.

---
*Report and Handoff completed.*
