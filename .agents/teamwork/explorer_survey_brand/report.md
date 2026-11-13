# Auditoría Exhaustiva de Identidad de Marca, Activos Visuales y Consistencia de Diseño
**Proyecto:** Envíos DosRuedas (Mar del Plata)  
**Repositorio:** `ccc` (`d:\repositorios\ccc`)  
**Fecha de Auditoría:** 13 de Noviembre de 2026  
**Rol Auditor:** Brand & Visual Assets Spec Miner  
**Alcance:** Documentación de marca (`.superdesign/`, `disenos/`, `docs/`, `contexto/`), configuración de estilos y tokens (`contexto/globals.css`), activos visuales (`public/`, `diseno-envios/`, `disenos/`), y las 16 páginas estáticas en `envios/`.

---

## 1. Resumen Ejecutivo

La presente auditoría realiza una prospección y análisis exhaustivo de la identidad de marca, los activos gráficos y la coherencia visual en el repositorio de **Envíos DosRuedas**, contrastando las especificaciones canónicas de diseño ("Sistema Lúcido" / "DosRuedas Electric Dispatch") con su implementación real en las páginas estáticas de `envios/` y los recursos locales en `public/`.

### Diagnóstico General
1. **Identidad Canónica Sólida pero Fragmentada:** Existe una especificación de marca sumamente madura y detallada en `contexto/globals.css`, `.superdesign/website/enviosdosruedas.com/design.md` y `disenos/envios-design.md`, fundamentada en la **"Ley de Tres Colores"** (Azul Eléctrico `#0950F6`, Amarillo Vial `#FFEC01`, Blanco Puro `#FFFFFF`) y un sistema tipográfico de 4 familias (Anton Display, Bebas Neue Subtítulos, Outfit Lectura/UI, Geist Mono Telemetría).
2. **Dependencia Crítica de CDN Remoto (Vulnerabilidad de Activos):** El 100% de las imágenes, fotografías, capturas y mapas utilizados en las 16 páginas de `envios/` (31 URLs únicas) apuntan a un bucket externo de Supabase (`vgbujcuwptvheqijyjbe.supabase.co`). En entornos sin conexión externa o ante la baja del bucket, el sitio colapsa visualmente con imágenes rotas.
3. **Activo Oficial Local Huérfano:** En `public/logo_nuevo.webp` existe el logotipo oficial en alta fidelidad (640x640 px, WebP con transparencia, 36.4 KB), pero **ninguna** de las páginas del repositorio lo referencia. Todas cargan un hash remoto de Supabase.
4. **Página Duplicada Crítica con Pérdida de Contenido:** `envios/terminos-y-condiciones.html` es un clon binario exacto (SHA-256 idéntico) de `envios/logistica-dosruedas.html`. El contenido legal de Términos y Condiciones no existe en el repositorio; fue sobreescrito por la página de seguimiento.
5. **Corrupción Masiva de Caracteres (Mojibake):** Las 16 páginas en `envios/` sufren una severa corrupción de codificación UTF-8 / Latin-1 (más de 2.400 ocurrencias de caracteres corrompidos como `EnvÃos`, `CotizÃ¡`, `LogÃ­stica`, `Ãšltima Milla`), afectando atributos `alt`, titulares `<h1>`-`<h3>`, botones y metadatos.
6. **Ineficiencia Extrema de Almacenamiento y Carga:** Las fuentes locales en `public/fuentes/` ocupan **13.2 MB** en formato TrueType (`.ttf`) sin compresión WOFF2. Más de 12 MB corresponden a variantes estáticas individuales nunca cargadas por `@font-face`. Adicionalmente, cada página HTML duplica un bloque `<style>` de **154 KB**, generando archivos de entre 226 KB y 512 KB por página.

---

## 2. Auditoría de Especificaciones y Documentación de Marca

Se localizaron y auditaron 7 fuentes de especificación de marca en el repositorio:

| Archivo / Fuente | Tipo de Documento | Propósito / Alcance |
| :--- | :--- | :--- |
| `contexto/globals.css` | Configuración Tailwind CSS v4 (`@theme`) | **Fuente canónica operativa.** Tokens oficiales de color, tipografía, sombras teñidas, double-bezel y motion. |
| `.superdesign/website/enviosdosruedas.com/brand.json` | Extracción DOM y Metadatos de Producción | Auditoría scraping del sitio oficial https://www.enviosdosruedas.com/. Metadatos SEO, Schema.org LD+JSON. |
| `.superdesign/website/enviosdosruedas.com/tokens.json` | Auditoría de Tokens Computados en Producción | Conteo de píxeles, colores dominantes (46.6% blanco, 28.4% azul, 1% amarillo) y familias tipográficas. |
| `.superdesign/website/enviosdosruedas.com/design.md` | Especificación de Sistema ("Fleet-blue impact grotesk") | Prosa + tokens YAML `superdesign-alpha`. Componentes, layout de 1280px, padding de 112px, guardrails. |
| `.superdesign/tmp/manual-de-marca-outline.json` | Outline de Manual de Marca Completo v1.0 | 9 diapositivas estructuradas (Identidad, Logotipo, Paleta, Tipografía, Composición, UI, Voz, Servicios, Guardrails). |
| `disenos/envios-design.md` | Especificación de Sistema ("DosRuedas Electric Dispatch") | Tokens YAML + prosa alineada con `contexto/globals.css` y la estética de logística urbana. |
| `design-philosophy.md` / `sistema-lucido.pdf` | Manifiesto Teórico ("Sistema Lúcido") | Filosofía de diseño: arquitectura viva, espacio como respiración estructurada, tarjeta double-bezel, sombras teñidas. |

### La Identidad Canónica Definida

#### A. Paleta Cromática: La Ley de Tres Colores
* **Azul Eléctrico / Vibrante (`#0950F6` / `--color-brand-blue-500`):**
  * **Tope máximo de oscuridad del sistema.** No se permite ningún color más oscuro que `#0950F6` para texto sobre fondo blanco (`--color-brand-ink`).
  * Rampa de 6 pasos canónicos:
    * `50` (`#E6EEFE`): Superficie suave, capa exterior de bezel (`/80`), hover ghost.
    * `100` (`#BACEFD`): Borde sutil estructural, divisores de tarjeta, líneas de progreso.
    * `200` (`#8EAFFB`): Hover de borde de tarjeta, anillos radio, trazos SVG.
    * `300` (`#628FF9`): Borde de input en reposo, hover de bezel.
    * `400` (`#3570F8`): Iconos, texto grande muted (≥24px), hover de fondos azules.
    * `500` (`#0950F6`): Primario canónico, titulares `H1`/`H2`, foco, botones principales, navbar y footer.
* **Amarillo Vial (`#FFEC01` / `--color-brand-yellow-500`):**
  * **Señal de alta visibilidad, nunca superficie.** Cobertura máxima restringida a ≤15% de la superficie visual.
  * Rampa de 7 pasos:
    * `50` (`#FFFDE6`): Fondo de opción seleccionada.
    * `100` (`#FFFAB8`): Halos y badge.
    * `200` (`#FFF78A`): Borde de opción activa.
    * `300` (`#FFF45C`): Detalle mono sobre azul.
    * `400` (`#FFF12E`): Estado hover de CTA primario.
    * `500` (`#FFEC01`): CTA primario en píldora, cláusula destacada en titular display, precio sobre azul, franja superior de footer (6px).
    * `600` (`#E6D400`): Estado pressed/active del CTA.
* **Blanco Puro (`#FFFFFF` / `--color-white`):**
  * Lienzo base único (`bg-brand-white`), superficie interior de tarjetas y texto sobre azul (`text-white`).
* **Verde WhatsApp / Mint MarDelivery (`#2ECC85`):**
  * Estrictamente delimitado a botones de chat WhatsApp y módulos del ecosistema MarDelivery (QR gastronómico). Queda **prohibido** su uso como color decorativo de marca general.
* **Neutralización de Paletas Prohibidas:**
  * En `contexto/globals.css`, Tailwind v4 anula (`initial`) todas las familias `neutral`, `stone`, `gray`, `zinc`, `slate`, `emerald`, `teal`, `lime` y `blue` por defecto, forzando cero tolerancia a grises descontextualizados.

#### B. Sistema Tipográfico Oficial (4 Familias)
1. **Display:** `Anton SC` (primario) / `Anton` (fallback).
   * Uso: Titulares hero y números de impacto en mayúsculas (`uppercase`), interlineado ultra cerrado (`0.85 - 0.92`), tracking negativo (`-0.05em` / `-2.2px`).
   * **Firma visual obligatoria:** Exactamente una cláusula corta (2 a 3 palabras) encerrada en una píldora amarilla (`bg-brand-yellow-500 text-brand-blue-500 rounded-full px-4 sm:px-5 py-1`).
2. **Subtítulos y Eyebrows:** `Bebas Neue`.
   * Uso: Kickers de sección, etiquetas de categoría de servicio, badges y cabeceras de tabla (`18px - 32px`, tracking positivo `0.05em` a `0.8px`).
3. **Cuerpo de Lectura y UI:** `Outfit` (primario) / `IBM Plex Sans` (fallback).
   * Uso: Párrafos de lectura (`16px - 18px`, peso 300/400), navegación, etiquetas de formulario y controles UI.
4. **Telemetría y Datos:** `Geist Mono`.
   * Uso: Códigos de seguimiento (`EDR00003071MDQ`), horarios de corte (`13:00 hs`, `20:00 hs`), precios y cifras tabulares (`tabular-nums`).

#### C. Componentes y Firmas Geométricas
* **Tarjeta Double-Bezel:** Firma estructural del "Sistema Lúcido". Consta de una carcasa exterior en `brand-blue-50/80` (`#E6EEFE`), borde `brand-blue-100` (`#BACEFD`), radio `24px` (`rounded-2xl`) y relleno `p-2`, que abraza una tarjeta interior blanca (`#FFFFFF`) con radio `16px` (`rounded-xl`), sombra interior suave y reborde sutil.
* **Botón CTA en Píldora Completa (`rounded-full` / `9999px`):**
  * Primario: Fondo `#FFEC01`, texto `#0950F6`, resplandor `--shadow-cta-glow: 0 0 28px rgba(255,236,1,0.45), 0 8px 24px rgba(9,80,246,0.18)`.
  * Secundario: Fondo `#0950F6`, texto `#FFFFFF`.
  * Outline: Borde `rgba(255,255,255,0.45)`, fondo transparente, texto `#FFFFFF`.
* **Navbar:** Barra horizontal a sangre completa (*full-bleed*), altura `72px - 85px`, esquinas estrictamente rectas (`border-radius: 0px`), fondo sólido `#0950F6`. **Guardrail estricto:** Prohibido redondear o separar la barra de navegación del borde superior.
* **Sistema de Elevación y Sombras:** Todas las sombras deben teñirse exclusivamente con el azul primario (`rgba(9, 80, 246, alpha)`) o el resplandor amarillo (`rgba(255, 236, 1, alpha)`). Quedan terminantemente prohibidas las sombras negras o grises neutras (`rgba(0,0,0,...)`).

### Divergencias Detectadas entre Especificaciones
* **Altura de Navbar:** `design.md` indica `85px`, mientras que `envios-design.md` especifica `72px`. `contexto/globals.css` utiliza padding `py-4` dinámico.
* **Botón Navbar CTA:** `design.md` declara `background: "rgba(0, 0, 0, 0.2)"` (uso de negro translúcido), lo cual entra en contradicción con el guardrail de `globals.css` ("NUNCA grises/negras").
* **Color Hover del Amarillo:** `design.md` usa `#FFF12D`, mientras `envios-design.md` y `globals.css` especifican `#FFF12E` (`brand-yellow-400`).

---

## 3. Inventario y Catálogo de Activos Visuales

### 3.1 Activos Locales en el Repositorio

| Ruta del Archivo | Formato | Tamaño | Dimensiones / Detalle | Estado / Observación |
| :--- | :--- | :--- | :--- | :--- |
| `public/logo_nuevo.webp` | WebP (VP8X + Alpha) | 36.454 bytes (~35,6 KB) | 640 x 640 px | **ACTIVO HUÉRFANO.** Isotipo circular oficial con fondo transparente. SHA-256: `D174F79AB7B0579B10CD1B6D105BFB38D2504D35C1EBD6E1A5EE1EAC5285C047`. No se utiliza en ninguna página de `envios/`. |
| `public/fuentes/Anton/` | TTF | 161.588 bytes | Regular (Variable 0) | Tipografía display. Incluye `OFL.txt`. |
| `public/fuentes/Anton_SC/` | TTF | 154.020 bytes | Regular (Small Caps) | Tipografía display para titulares. Incluye `OFL.txt`. |
| `public/fuentes/Bebas_Neue/` | TTF | 57.676 bytes | Regular | Tipografía condensada para subtítulos. Incluye `OFL.txt`. |
| `public/fuentes/Outfit/` | TTF | 608.204 bytes (12 archivos) | Variable: 110.572 bytes; 9 estáticos: ~55 KB c/u | Tipografía sans principal. Los 9 archivos estáticos en `static/` son redundantes y no se usan en `@font-face`. |
| `public/fuentes/Geist_Mono/` | TTF | 2.228.672 bytes (22 archivos) | 2 Variables: 356.688 bytes; 18 estáticos: ~104 KB c/u | Tipografía monospace. Los 18 archivos en `static/` no se usan en `@font-face`. |
| `public/fuentes/IBM_Plex_Sans/` | TTF | 10.647.851 bytes (46 archivos) | 2 Variables: 1.126.856 bytes; 42 estáticos: ~225 KB c/u | Tipografía sans fallback. **Desperdicio masivo:** 42 variantes estáticas en `static/` ocupan 9,5 MB sin uso. |
| `sistema-lucido.pdf` | PDF | 232.269 bytes (~226 KB) | Documento A4 generado | Generado por `generate_philosophy_pdf.py` con ReportLab. |
| `diseno-envios/` | HyperFrames | N/A | Directorio de animación video | La carpeta `"assets"` declarada en `hyperframes.json` no existe. `index.html` es un scaffold vacío con colores `#000` y `#fff`. |
| `Drepositoriosccc/` | Directorio corrupto | 0 bytes | Nombre con dos puntos escapados | Directorio vacío generado por un error de script/escape de ruta. Debe ser eliminado. |

### 3.2 Inventario de Activos Remotos en Producción (Supabase CDN)
Las páginas en `envios/` y `disenos/envios.html` contienen **31 recursos remotos únicos** alojados en el bucket `https://vgbujcuwptvheqijyjbe.supabase.co/storage/v1/object/public/clone-assets/`.

| Hash del Activo (Supabase) | Formato | Páginas que lo Utilizan | Descripción / Texto Alternativo Detectado |
| :--- | :---: | :--- | :--- |
| `488abaaa02c40bfde312a7a42dbef04d6361c03854ffa1e3435baa00e6ddaf6e` | `.webp` | Todas las 16 páginas (37 instancias) | **Logotipo Oficial Envíos DosRuedas** (usado en header y footer). |
| `2b31cc642af2459c180d4e63071872f60a398901827fb31fd1ac039f4a94d514` | `.webp` | `home.html`, `html.html` | Ilustración isométrica de Mar del Plata con ruta amarilla y pin de destino. |
| `7ac9627ab4c1493288e639e1ba5fa8698e6c13ee5d4064a08acaf3d3e17548d7` | `.webp` | `home.html`, `html.html` | Chip gráfico flotante / servicio 1. |
| `fef21ecc47bdc829f5488bfae44cd9c6b168d9db640b8c1efafd7f8ce78f036b` | `.webp` | `home.html`, `html.html` | Chip gráfico flotante / servicio 2. |
| `651acca40e62495d8ce0db0ffde7dfa5726e9be890580581470cd69522503582` | `.webp` | `home.html`, `html.html` | Gráfico de trazabilidad y ruteo. |
| `cb6aa669760a0ae4715e88c223185fc2a01fb663e67c55f007f0436b0b2d54dd` | `.webp` | `home.html`, `html.html` | Gráfico de panel para repartidores. |
| `f0245164e4f1b4d32c11631d76f4c749c8f68c57d39264af73ab3327585dc2ac` | `.webp` | `contacto.html` | Teléfono y sobre: "Escribinos hoy". |
| `59340c1f5dcf60b8cc337545111f82653bedbb8cee26db3c3011f2ef105f9e39` | `.webp` | `nosotrosnuestras-redes.html` | Smartphone con apps Instagram, Facebook y WhatsApp abiertas. |
| `6116d00de8c6ef57707343f2140edb0905a223e4a787b5bab2090286f39978f7` | `.webp` | `nosotrosnuestras-redes.html` | Mockup post Facebook ("Solución para tus envíos"). |
| `fb5557cebe3cf0f54032ff13b2252a458787a970d85ea8d5f02f5d7478355648` | `.webp` | `nosotrosnuestras-redes.html` | Mockup post Instagram ("Servicio confiable en Mar del Plata"). |
| `e2902730b8852831199d2bc057dcfbbbd073313f8e88734808f9b95b5322612d` | `.webp` | `nosotrosnuestras-redes.html` | Mockup post Facebook ("Confianza y responsabilidad"). |
| `5521785ea86e0e1b68ea8840262e15d09f87353892798a6a2c05271bb2c7a0d9` | `.webp` | `nosotrosnuestras-redes.html` | Mockup post Instagram ("Pilares fundamentales"). |
| `5430aafab04ca1a437549704c779271eff0f6c47c9bc63dadb6c5d1c5093f0c3` | `.webp` | `nosotrosnuestras-redes.html` | Mockup post Instagram ("Tu confianza es nuestro motor"). |
| `88ef7824cd95f2970ee3fb709e4768d96deecda61636259f9073a8ba5887fd92` | `.webp` | `nosotrospreguntas-frecuentes.html` | Ilustración gráfica de preguntas frecuentes. |
| `d0eb1ada8550b4d1ad31721692f4e9c114d133315307df1d171fc341df34e61c` | `.webp` | `serviciosdeposito-fulfillment.html` | Fotografía del local físico en Friuli 1972 con toldo azul y paquetería. |
| `9ce3c1dfbf429413dc095429c556e41c47df493b360ff0c3bc836add6225b5ea` | `.webp` | `serviciosenvios-express.html` | Fotografía de cadete motorizado con mochila térmica. |
| `cf194a610a99745be451b0b0d46033b8fbf2f642860c7eacc924c00e872962a1` | `.webp` | `serviciosenvios-express.html` | Detalle operativo de entrega rápida. |
| `30557ba6fe...` a `9248b35eb1...` (9 hashes) | `.png` | `cotizar.html` (9 imágenes) | **Teselas raster de OpenStreetMap (Leaflet tiles).** Resolución 256x256 px fijadas estáticamente. |
| `b7acee2c5e...` | `.svg` | `contacto.html`, `nosotrosnuestras-redes.html` | Isotipo vectorial de Instagram. |
| `26d0cc863a...` | `.svg` | `contacto.html`, `nosotrosnuestras-redes.html` | Isotipo vectorial de Facebook. |
| `4223e01da2...` | `.svg` | `nosotrosnuestras-redes.html` | Isotipo vectorial de WhatsApp. |
| `58837558b0...` | `.svg` | 5 páginas de servicios y legales (9 usos) | Icono decorativo de red / portal. |
| `98ab5296b4...` | `.svg` | `serviciosenvios-lowcost.html` | Gráfico vectorial de tarifa económica. |

---

## 4. Análisis Comparativo: Tokens vs 16 Páginas en `envios/`

### 4.1 Métricas de Archivos y Componentes

| Página HTML | Peso (Bytes) | Líneas CSS Inline | SVG Inline | Imágenes Remotas | Estado de Consistencia Visual |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `contacto.html` | 281.519 | ~4.800 | 73 | 5 | Conforme con tokens. Sufre 116 mojibakes. |
| `cotizar.html` | 276.615 | ~4.850 | 60 | 11 | Mapa falso compuesto por 9 PNGs estáticos. 134 mojibakes. |
| `home.html` | 410.547 | ~5.800 | 110 | 6 | Conforme a estructura de diseño. 280 mojibakes. |
| `html.html` | 512.198 | ~5.900 | 110 | 6 | **CLON REDUNDANTE de `home.html`** (difiere solo en indentación). |
| `logistica-dosruedas.html` | 235.560 | ~4.500 | 56 | 2 | Página operativa de seguimiento EDR. 106 mojibakes. |
| `mardelivery.html` | 260.987 | ~4.700 | 80 | 2 | Conforme. Implementa token `#2ECC85` adecuadamente. 133 mojibakes. |
| `nosotrosnuestras-redes.html` | 288.034 | ~4.850 | 69 | 8 | Conforme en paleta. Muestra mockups de redes sociales. 110 mojibakes. |
| `nosotrospreguntas-frecuentes.html` | 264.544 | ~4.750 | 70 | 2 | Conforme. Acordeones interactivos. 102 mojibakes. |
| `nossobresobre-nosotros.html` | 322.675 | ~5.050 | 78 | 2 | **NOMBRE MALFORMADO** (`nossobresobre`). Contenido de historia de marca. 169 mojibakes. |
| `politicade-privacidad.html` | 284.052 | ~4.650 | 77 | 2 | Conforme en estructura legal. 160 mojibakes. |
| `serviciosdeposito-fulfillment.html` | 334.251 | ~5.000 | 113 | 2 | Conforme. Incluye foto real de Base Friuli. 160 mojibakes. |
| `serviciosempresas-cuenta-corriente.html`| 226.483 | ~4.400 | 51 | 2 | Conforme a B2B. 96 mojibakes. |
| `serviciosenvios-express.html` | 305.242 | ~4.950 | 103 | 3 | Conforme. Franja de 3 horas. 158 mojibakes. |
| `serviciosenvios-lowcost.html` | 303.509 | ~4.950 | 96 | 2 | Conforme. Reparto económico en el día. 158 mojibakes. |
| `serviciosenviosflex.html` | 392.043 | ~5.250 | 131 | 2 | Conforme. Mercado Envíos Flex. 231 mojibakes. |
| `terminos-y-condiciones.html` | 235.560 | ~4.500 | 56 | 2 | **ERROR CRÍTICO: COPIA EXACTA DE `logistica-dosruedas.html`**. Contenido de términos inexistente. |

### 4.2 Evaluación de Elementos Visuales frente a Tokens

1. **Paleta Cromática y Superficies:**
   * **Cumplimiento:** Las 16 páginas aplican fielmente las clases Tailwind de la paleta oficial: `bg-brand-blue-500`, `text-brand-blue-500`, `bg-brand-yellow-500`, `text-brand-ink`, `border-brand-blue-100`.
   * **Ritmo de Sección:** Se respeta la alternancia modular de bandas completas (`#0950F6` en hero y footer, intercalando `#FFFFFF` y `#E6EEFE` en cuerpo central).
   * **Inconsistencia:** En los estilos incrustados de todas las páginas persisten declaraciones nativas que definen sombras en `#000000` (`--drop-shadow-sm: 0 1px 2px #00000026`) y el botón CTA del navbar utiliza fondo `rgba(0, 0, 0, 0.15)` o `#0003`, violando la regla de "cero negro".
2. **Tipografía y Jerarquía:**
   * **Cumplimiento:** La jerarquía tipográfica visualmente respeta las proporciones canónicas: titulares masivos en mayúsculas (`Anton`), subtítulos condensados (`Bebas Neue`), cuerpo legible (`Outfit`) y metadatos (`Geist Mono`).
   * **Inconsistencia en Carga:** La regla `@font-face` usa `url("../public/fuentes/...")`. Esto funciona únicamente cuando el servidor web sirve desde la raíz del repositorio; si se sirve la carpeta `envios/` como docroot, todas las fuentes fallan (404) y el sitio retrocede a fuentes genéricas del sistema.
3. **Logotipos e Isotipos:**
   * Todas las páginas muestran el isotipo circular en el navbar y en el footer, pero cargándolo mediante la URL de Supabase `.../488abaaa02c40bfde312a7a42dbef04d6361c03854ffa1e3435baa00e6ddaf6e.webp` con dimensiones de visualización `40x40 px` o `16x16 px`.
   * El archivo local `public/logo_nuevo.webp` (640x640 px) está completamente desaprovechado.
4. **Iconografía:**
   * 100% de la iconografía de interfaz está resuelta mediante **SVGs inline con clases de Lucide Icons**.
   * Conteo de iconos dominantes: `arrow-up-right` (121), `check` (95), `arrow-right` (84), `chevron-down` (64), `shield-check` (57), `clock` (56), `phone` (51), `zap` (49), `map-pin` (48), `package` (46), `store` (40), `check-circle-2` (38).
   * Los SVGs inline heredan perfectamente el color de texto (`stroke="currentColor"`), lo que garantiza coherencia cromática instantánea con los tokens de azul y amarillo.

---

## 5. Matriz de Hallazgos, Inconsistencias y Puntos Críticos

| ID | Gravedad | Categoría | Ubicación Exacta | Descripción del Hallazgo | Impacto / Riesgo |
| :---: | :---: | :---: | :--- | :--- | :--- |
| **H-01** | **Crítica** | Pérdida de Contenido / Integridad | `envios/terminos-y-condiciones.html` | El archivo es un clon idéntico (SHA-256 `D82177D1...`) de `logistica-dosruedas.html`. Título: *"Logística DosRuedas \| Seguimiento y Portales Digitales"*. | El sitio web carece por completo de la página legal de Términos y Condiciones. Riesgo regulatorio y de defensa del consumidor en Mar del Plata. |
| **H-02** | **Crítica** | Disponibilidad de Activos | Las 16 páginas en `envios/*.html` (31 URLs) | Todas las imágenes, fotos de sucursal, isotipos y gráficos se consumen desde Supabase (`vgbujcuwptvheqijyjbe.supabase.co`). | Si el bucket expira, se elimina o el usuario navega offline / intranet, el 100% de los elementos visuales se rompen. |
| **H-03** | **Alta** | Activo Huérfano | `public/logo_nuevo.webp` | Logotipo oficial de alta resolución (640x640 px, 36.4 KB) presente en el repositorio pero con 0 referencias en todo el código fuente. | Desconexión entre los activos locales y la implementación real; dependencia innecesaria de la nube para el activo más crítico de la marca. |
| **H-04** | **Alta** | Calidad Editorial / Encoding | Las 16 páginas en `envios/*.html` | Más de 2.400 instancias de caracteres españoles corrompidos por mojibake (`EnvÃos`, `CotizÃ¡`, `LogÃ­stica`, `Ãšltima`, `Mar del Plata: El motor de tu Ãºltima milla`). | Impacto destructivo en credibilidad de marca, profesionalismo y SEO (Google indexa términos rotos). |
| **H-05** | **Alta** | Navegación e Hipervínculos | Cabeceras y pies de página en las 16 páginas | Todos los enlaces de navegación (`href`) apuntan a URLs absolutas de producción (`https://www.enviosdosruedas.com/...`) en lugar de rutas relativas locales. | Imposibilita la navegación interna en entornos locales, de staging o previsualización: cualquier clic desvía al usuario fuera del entorno local. |
| **H-06** | **Media** | Nomenclatura de Archivos | `envios/nossobresobre-nosotros.html` | Nombre de archivo corrompido con prefijo duplicado (`nossobresobre-nosotros.html`) derivado de un scraping defectuoso de `/nosotros/sobre-nosotros/`. | Inconsistencia en la arquitectura de archivos del proyecto y riesgo de errores 404 al enlazar. |
| **H-07** | **Media** | Redundancia de Archivos | `envios/html.html` | Archivo de 512 KB que duplica casi textualmente el contenido de `envios/home.html`, variando únicamente en espacios de indentación. | Confusión en el mantenimiento, duplicación innecesaria de más de medio megabyte en el repositorio. |
| **H-08** | **Media** | Optimización de Medios | `public/fuentes/` | Directorio de 13.2 MB con 86 archivos TTF. 12 MB corresponden a 60 archivos estáticos en subcarpetas `static/` que nunca se referencian en el CSS. Cero uso de WOFF2. | Exceso de peso en el repositorio y tiempos de transferencia web 4 veces más lentos de lo óptimo para tipografías. |
| **H-09** | **Media** | Duplicación de Código / Performance | Las 16 páginas en `envios/*.html` | Cada página contiene un bloque `<style>` de 154 KB con el framework Tailwind embebido en lugar de vincular a un archivo común (`contexto/globals.css`). | Bloat masivo: 2,5 MB de CSS duplicado en el repositorio; el navegador no puede cachear los estilos entre cambios de página. |
| **H-10** | **Baja** | Higiene de Repositorio | Raíz del proyecto: `Drepositoriosccc/` | Carpeta vacía con dos puntos no escapados en el sistema de archivos de Windows. | Basura residual de tooling que ensucia el árbol de trabajo. |
| **H-11** | **Baja** | Componente Falso | `envios/cotizar.html` | El mapa de Mar del Plata está simulado mediante 9 teselas fijas PNG de Leaflet de 256x256 px en lugar de un mapa interactivo o una ilustración vectorial limpia. | Apariencia frágil; las teselas fijas se pixelan o desalinean en viewports no estándar. |
| **H-12** | **Baja** | Divergencia de Tokens | Estilos inline en `envios/*.html` vs `contexto/globals.css` | El botón de llamada del navbar define fondo translúcido negro (`rgba(0,0,0,0.15)` / `#0003`) y variables `--drop-shadow-sm: #00000026`. | Contraviene la regla formal de "cero tintes negros o grises" especificada en `globals.css` y `design-philosophy.md`. |

---

## 6. Tablas de Prospección de Especificación (Protocolo Specification Miner)

### Features Discovered (Características y Especificaciones Descubiertas)

| # | Categoría | Feature / Especificación | Descripción Canónica | Inputs / Parámetros | Outputs / Comportamiento | Error / Restricciones | Descubierto Vía |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Color** | Ley de Tres Colores | Paleta rígida basada en Azul Eléctrico, Amarillo Vial y Blanco Puro. | `--color-brand-blue-500: #0950F6`, `--color-brand-yellow-500: #FFEC01`, `--color-white: #FFFFFF` | Contraste máximo, jerarquía limpia, identidad industrial vibrante. | Prohibido usar negro o grises neutros para cuerpo de texto. | `contexto/globals.css`, `manual-de-marca-outline.json` |
| 2 | **Color** | Ración Estricta de Amarillo | El amarillo `#FFEC01` funciona únicamente como señal/llamado de atención. | Selectores CTA, cláusulas display destacadas, badges de estado. | Cobertura ≤ 15% del viewport; resplandor `--shadow-cta-glow`. | Prohibido usar `#FFEC01` como fondo de sección o página completa. | `disenos/envios-design.md`, `design.md` |
| 3 | **Color** | Aislamiento de Verde WhatsApp | El color `#2ECC85` está reservado exclusivamente para mensajería y MarDelivery. | Botones de WhatsApp, chips de estado activo. | Color verde menta brillante con texto oscuro `#031811`. | Prohibido usar verde como acento de marca general o en botones estándar. | `contexto/globals.css`, `disenos/envios-design.md` |
| 4 | **Tipografía** | Display Cláusula en Bloque | Titulares masivos con una frase corta encerrada en cápsula amarilla. | `font-display`, `text-3xl` a `text-5xl`, tracking `-0.05em`, leading `0.9`. | Letras mayúsculas compactas; píldora amarilla con texto azul sobre 2-3 palabras. | No aplicar la píldora a oraciones completas ni párrafos. | `.superdesign/website/enviosdosruedas.com/design.md` |
| 5 | **Tipografía** | 4 Familias Especializadas | Separación funcional de fuentes: Anton, Bebas Neue, Outfit, Geist Mono. | Familias tipográficas mapeadas a tokens `@theme`. | Display (Anton), Subtítulos (Bebas), Lectura (Outfit), Telemetría (Geist Mono). | Prohibido mezclar fuentes display en cuerpo de texto. | `contexto/globals.css`, `generate_philosophy_pdf.py` |
| 6 | **Componente** | Tarjeta Double-Bezel | Contenedor de dos capas que otorga profundidad sin sombras negras. | Contenedor exterior `brand-blue-50/80` con radio 24px + contenedor interior blanco 16px. | Efecto de bisel flotante con sombras teñidas en azul (`--shadow-float`). | No usar radios arbitrarios que rompan el escalonamiento 24px/16px. | `contexto/globals.css`, `design-philosophy.md` |
| 7 | **Componente** | Navbar Full-Bleed | Barra superior fija a pantalla completa sin bordes redondeados. | `bg-brand-blue-500`, altura fija 72px/85px, `py-4`, radio `0px`. | Barra de navegación sólida que transitions a translúcida en scroll. | Prohibido redondear esquinas o dejar márgenes laterales en el navbar. | `.superdesign/website/enviosdosruedas.com/design.md` |
| 8 | **Elevación** | Sombras Teñidas Canónicas | Todas las sombras se calculan a partir de `#0950F6` con distintos niveles de opacidad. | Clases `--shadow-xs` a `--shadow-antigravity-deep` (alpha 0.03 a 0.22). | Elevación luminosa que se funde con los fondos azulados sin ensuciar el lienzo. | Prohibido usar sombras negras convencionales (`#000` o `rgba(0,0,0,x)`). | `contexto/globals.css`, `design-philosophy.md` |
| 9 | **Voz y Tono** | Copywriting Rioplatense | Redacción en segunda persona informal argentina ("vos"). | Verbos conjugados: "Cotizá", "Escribinos", "Seguí", "Olvidate". | Trato cercano, resolutivo y comercialmente ágil de Mar del Plata. | Evitar lenguaje neutro distante ("Cotice", "Tú") o promesas vagas. | `manual-de-marca-outline.json`, `envios-design.md` |
| 10| **Identidad** | Isotipo Local | Logotipo de alta resolución disponible en repositorio. | Archivo `public/logo_nuevo.webp` (640x640 px). | Isotipo vectorial rasterizado de alta definición. | Se encuentra huérfano; el sitio depende de un CDN remoto. | Inspección física en `public/logo_nuevo.webp` |

### Edge Cases (Casos Límite y Comportamientos Observados)

| # | Feature / Área | Input / Condición Evaluada | Comportamiento Observado en el Repositorio | Veredicto / Impacto |
| :-: | :--- | :--- | :--- | :--- |
| E1 | Carga de Activos Gráficos | Ejecución en entorno local offline / sin internet. | Todas las imágenes (`<img src="https://vgbujcuwptvheq... >`) fallan con error de conexión. | **Falla Crítica:** El sitio local queda sin logotipo ni fotografías. |
| E2 | Páginas Legales | Navegación a `terminos-y-condiciones.html`. | Carga la página de seguimiento de paquetes con código EDR y panel de comercios. | **Falla Crítica:** Contenido de términos inexistente. |
| E3 | Renderizado de Textos | Apertura de cualquier página en navegador estándar UTF-8. | Se renderizan caracteres dañados (`EnvÃos DosRuedas`, `CotizÃ¡ tu envÃ­o`). | **Falla Alta:** Textos degradados por doble codificación. |
| E4 | Carga de Tipografías | Servir el proyecto teniendo como raíz la carpeta `envios/`. | La ruta `../public/fuentes/...` intenta resolver fuera del root web y retorna 404. | **Falla Media:** Fallback a Arial y fuentes genéricas. |
| E5 | Enlaces de Navegación | Clic en cualquier enlace del menú o footer en entorno local. | Redirige inmediatamente a los servidores de producción de `www.enviosdosruedas.com`. | **Falla Media:** Expulsa al evaluador/usuario del entorno de desarrollo. |
| E6 | Accesibilidad Motriz / Reducción | Activación de `prefers-reduced-motion: reduce`. | `globals.css` desactiva animaciones (`0.01ms`) y quita pulsos de anillos. | **Conforme:** Buena previsión en tokens globales. |
| E7 | Cotizador con Mapa | Redimensionamiento de pantalla en `cotizar.html`. | Las 9 teselas fijas PNG se desajustan al estar ancladas por `translate3d` absolutos. | **Falla Baja:** Mapa estático frágil ante cambios de layout. |

---

## 7. Rúbrica de Auditoría: Evaluación Punto por Punto

| Criterio de Auditoría | Ponderación | Puntaje (1-5) | Diagnóstico Justificado |
| :--- | :---: | :---: | :--- |
| **1. Definición Teórica y Reglas de Marca** | 20% | **5 / 5** | Excelente nivel de detalle en `design-philosophy.md`, `globals.css` y `manual-de-marca-outline.json`. Reglas claras, fundamentos estéticos rigurosos y restricciones formales explícitas. |
| **2. Coherencia Cromática y de Estilos** | 20% | **4 / 5** | Gran fidelidad en la aplicación de la paleta canónica (Azul, Amarillo y Blanco) y los componentes double-bezel. Penalizado levemente por filtraciones de negros translúcidos en botones de navegación. |
| **3. Gestión y Disponibilidad de Activos Visuales** | 25% | **1 / 5** | **Deficiente.** El 100% de las imágenes son remotas en un CDN externo; el logotipo local de 640x640 px está huérfano; la carpeta de assets de HyperFrames está vacía; 13.2 MB de fuentes TTF sin optimizar. |
| **4. Integridad del Código y Nomenclatura** | 20% | **2 / 5** | **Bajo.** 2.400+ errores de mojibake, clon idéntico erróneo en `terminos-y-condiciones.html`, clon redundante `html.html`, archivo malformado `nossobresobre-nosotros.html` y enlaces absolutos de producción. |
| **5. Arquitectura Técnica y Rendimiento CSS** | 15% | **2 / 5** | **Bajo.** 154 KB de CSS Tailwind duplicados en línea en las 16 páginas en lugar de un enlace compartido a `globals.css`. Fuentes en formato `.ttf` sin compresión `.woff2`. |
| **CALIFICACIÓN GLOBAL PONDERADA** | **100%** | **2.8 / 5.0** | **Diagnóstico:** Identidad y diseño visual de altísima calidad conceptual, pero con una ejecución técnica y empaquetado de archivos severamente degradado por scraping defectuoso y dependencia externa. |

---

## 8. Plan de Recomendaciones Accionables y Priorizadas

### Fase 1: Correcciones Críticas Inmediatas (P0)
1. **Restaurar `envios/terminos-y-condiciones.html`:**
   * Obtener el texto real de los Términos y Condiciones desde la web de producción oficial (`https://www.enviosdosruedas.com/terminos-y-condiciones/`) y reemplazar el archivo erróneo que actualmente contiene la página de seguimiento.
2. **Localización de Recursos Gráficos (Desconexión de Supabase):**
   * Descargar las 31 imágenes remotas y guardarlas en `public/images/` con una convención de nombres descriptiva (ej. `logo-dosruedas.webp`, `hero-mapa-mdq.webp`, `sucursal-friuli.webp`).
   * Actualizar todas las etiquetas `<img>` de las páginas de `envios/` para que apunten a rutas relativas locales seguras (`../public/images/...` o `/images/...`).
3. **Vincular el Logotipo Oficial Local:**
   * Reemplazar la URL remota del logo en cabeceras y pies de página por `../public/logo_nuevo.webp` o una versión escalada optimizada.
4. **Saneamiento Masivo de Mojibake / Codificación UTF-8:**
   * Ejecutar un script de reemplazo y normalización de codificación sobre los 16 archivos HTML para corregir de raíz las 2.400 secuencias rotas (`EnvÃos` → `Envíos`, `CotizÃ¡` → `Cotizá`, etc.).

### Fase 2: Normalización de Enlaces y Arquitectura de Archivos (P1)
5. **Relativizar la Navegación Interna:**
   * Reemplazar los enlaces absolutos `https://www.enviosdosruedas.com/...` en menús y footers por enlaces relativos a las páginas HTML locales (ej. `./cotizar.html`, `./contacto.html`, `./serviciosenvios-express.html`).
6. **Corregir Nomenclatura y Eliminar Duplicados:**
   * Renombrar `envios/nossobresobre-nosotros.html` a `envios/sobre-nosotros.html`.
   * Eliminar el archivo redundante `envios/html.html`.
   * Eliminar la carpeta corrupta residual `Drepositoriosccc/` de la raíz.
7. **Modularización y Caché del CSS:**
   * Extraer el bloque inline de 154 KB presente en cada archivo a una hoja de estilos compartida (o compilar `contexto/globals.css` hacia `public/css/styles.css`) y referenciarla mediante `<link rel="stylesheet" href="../public/css/styles.css">`. Esto reducirá el tamaño de las páginas de ~350 KB a menos de 40 KB cada una.

### Fase 3: Optimización de Rendimiento y Medios (P2)
8. **Optimización Tipográfica (WOFF2 + Subsetting):**
   * Convertir las tipografías variables de `public/fuentes/` a formato `.woff2`.
   * Eliminar los más de 60 archivos estáticos no utilizados en las subcarpetas `static/` de IBM Plex Sans y Geist Mono, reduciendo el peso de fuentes de **13.2 MB a menos de 400 KB**.
9. **Sustitución del Mapa Estático en `cotizar.html`:**
   * Reemplazar las 9 teselas PNG capturadas por una ilustración vectorial SVG estilizada de Mar del Plata con los puntos de cobertura o por un contenedor Leaflet inicializado dinámicamente.
10. **Completar Scaffold de `diseno-envios` (HyperFrames):**
    * Configurar los tokens de color (`#0950F6`, `#FFEC01`) y tipografía en `diseno-envios/index.html` para que las composiciones de video reflejen fielmente la identidad de marca de Envíos DosRuedas.
