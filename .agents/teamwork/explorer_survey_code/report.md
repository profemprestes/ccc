# INFORME DE AUDITORÍA TÉCNICA Y RELEVAMIENTO DE CÓDIGO
## Envíos DosRuedas — Repositorio y Páginas Web (`contexto/globals.css` y `envios/`)

**Fecha de relevamiento**: 13 de Noviembre de 2026  
**Auditor**: Code & Technical Quality Explorer (`explorer_survey_code`)  
**Directorio auditado**: `d:\repositorios\ccc`  
**Entorno de ejecución**: Windows (PowerShell) / Node.js & Vite / Tailwind CSS v4

---

## 1. RESUMEN EJECUTIVO

Se ha realizado una inspección minuciosa, línea por línea y archivo por archivo, de los activos de código fuente del proyecto **Envíos DosRuedas**, abarcando:
1. El archivo central de configuración de diseño y estilos: `contexto/globals.css`.
2. Las páginas web contenidas en el directorio `envios/` (16 archivos HTML detectados, que corresponden a 15 páginas canónicas del sitio más 1 archivo redundante).
3. Los recursos complementarios en `public/`, `disenos/`, `scripts/` y `tests/`.

### Veredicto Técnico General
El proyecto presenta una **identidad visual sólida y altamente diferenciada** basada en la filosofía "Sistema Lúcido" y tokens de Tailwind CSS v4 (paleta canónica azul eléctrico `#0950F6`, amarillo vial `#FFEC01` y blanco `#FFFFFF`, tarjetas "double-bezel" y botones "cta-nested-pill"). Sin embargo, la implementación actual en el directorio `envios/` evidencia un **estado de captura estática/scraping desarticulado de producción**, lo que introduce **bloqueos críticos de funcionamiento, navegación, accesibilidad y rendimiento**.

### Hallazgos Críticos Más Urgentes (P0 / Showstoppers):
1. **Kill-Switch Universal de Navegación y Conversión**: En **los 16 archivos HTML** existe un script al final del documento que intercepta todos los clics y ejecuta `e.preventDefault()` sobre cualquier enlace que no sea un ancla `#`. Esto **bloquea por completo la navegación entre páginas y todos los botones de contacto y cotización hacia WhatsApp**.
2. **Duplicación Crítica y Contenido Perdido en Términos y Condiciones**: El archivo `envios/terminos-y-condiciones.html` es un **duplicado idéntico byte a byte (SHA256 idéntico)** de `envios/logistica-dosruedas.html`. El texto legal de términos y condiciones fue completamente sobreescrito y no existe en el repositorio.
3. **Archivo Redundante**: `envios/html.html` (500.2 KB) es un duplicado idéntico en contenido de `envios/home.html` (400.9 KB), existiendo únicamente una diferencia de formateo de sangría (4 espacios vs 2 espacios).
4. **Hipertrofia de CSS Embebido (2.14 MB de CSS Duplicado)**: Ningún archivo HTML enlaza a `contexto/globals.css` mediante `<link rel="stylesheet">`. En su lugar, cada archivo embebe entre 121 KB y 193 KB de CSS compilado dentro de etiquetas `<style>` en el `<head>`. Esto representa **45.4% del peso total de los archivos HTML**, forzando al navegador a re-descargar y re-procesar megabytes de CSS en cada navegación sin poder usar la caché HTTP del navegador.
5. **Falta Total de Interactividad Funcional (0% JS Operativo)**: No existe lógica JavaScript para:
   - El menú móvil (el botón `#mobile-menu-toggle-opt` apunta a un diálogo `#mobile-navigation-dialog` que **no existe en el DOM** de ningún archivo).
   - Los dropdowns de navegación superior ("Servicios", "Plataformas", "Nosotros").
   - El acordeón de Preguntas Frecuentes (solo la pregunta 0 está expandida; las preguntas 1 a 7 son inaccesibles).
   - Los formularios de Cotización (`cotizar.html`) y Contacto (`contacto.html`), que carecen de `action`, `method` y manejador de envío.
   - El rastreador en vivo de paquetes (`logistica-dosruedas.html`), cuyos botones de prueba y campo de entrada son meros elementos visuales sin backend ni fetch.
6. **Dependencia Externa Crítica en Imágenes**: El 100% de las imágenes en las páginas web apuntan a un bucket externo no institucional de Supabase (`https://vgbujcuwptvheqijyjbe.supabase.co/storage/v1/object/public/clone-assets/...`). Si ese bucket es eliminado o restringido, todas las imágenes del sitio se romperán.
7. **Fuentes TTF no optimizadas y rutas relativas rotas**: Se referencian fuentes en formato `.ttf` sin comprimir (1.92 MB de peso activo) mediante rutas relativas `../public/fuentes/...`, lo cual causará error 404 inmediato si el sitio se despliega teniendo `envios/` o `public/` como raíz del servidor web.
8. **Cursor Global Forzado a "pointer"**: En los 16 archivos, la etiqueta `<body>` posee el atributo `style="cursor:pointer"`, provocando que toda la pantalla muestre una mano de enlace interactivo sobre párrafos, fondos y textos neutros.

---

## 2. RELEVAMIENTO DETALLADO DE `contexto/globals.css`

El archivo `d:\repositorios\ccc\contexto\globals.css` cuenta con **370 líneas de código** y **14,843 bytes**. Está estructurado bajo la sintaxis oficial de **Tailwind CSS v4** (`@import "tailwindcss";`, `@custom-variant`, `@theme`, `@utility`).

### 2.1. Arquitectura de Diseño y Paleta Canónica ("Ley de Tres Colores")
El archivo formaliza rigurosamente la identidad "Sistema Lúcido":
- **Azul Vibrante (Primario Canónico)**: 6 pasos (50 a 500). Tope de oscuridad absoluto fijado en `#0950F6` (`--color-brand-blue-500`).
  - `--color-brand-blue-50`: `#E6EEFE` (fondo suave, bezel exterior /80, hover ghost).
  - `--color-brand-blue-100`: `#BACEFD` (borde estructural, divisores).
  - `--color-brand-blue-200`: `#8EAFFB` (borde tarjeta hover, trazos SVG).
  - `--color-brand-blue-300`: `#628FF9` (borde input reposo).
  - `--color-brand-blue-400`: `#3570F8` (íconos, texto muted ≥24px).
  - `--color-brand-blue-500`: `#0950F6` (color institucional, títulos H1/H2, foco, botones principales).
- **Amarillo Vial (Señalética y Acción)**: 7 pasos (50 a 600). Regla explícita en línea 43: *"Señal, nunca superficie. ≤15% cobertura."*
  - `--color-brand-yellow-50`: `#FFFDE6` a `--color-brand-yellow-400`: `#FFF12E`.
  - `--color-brand-yellow-500`: `#FFEC01` (CTA primario, pasos activos, detalles de precio).
  - `--color-brand-yellow-600`: `#E6D400` (estado pressed).
- **Blanco**: `--color-white`: `#FFFFFF` (lienzo único).
- **Neutralización de Paletas No Permitidas**: Líneas 68-102 configuran a `initial` las escalas completas de `neutral`, `stone`, `green`, `emerald`, `lime`, `teal` y `blue` por defecto de Tailwind, garantizando que el compilador no genere clases fuera de la paleta institucional.

### 2.2. Tipografía Oficial
Configurada en las líneas 106-125:
- **Display**: `--font-display: var(--font-display, "Anton SC"), "Anton", sans-serif;`
- **Subheading**: `--font-subheading: var(--font-subheading, "Bebas Neue"), sans-serif;`
- **Lectura / Sans**: `--font-sans: var(--font-sans, "Outfit"), "IBM Plex Sans", sans-serif;`
- **Datos / Mono**: `--font-mono: var(--font-mono, "Geist Mono"), monospace;` (con `font-variant-numeric: tabular-nums`).

### 2.3. Sistema de Sombras Teñidas (Tinted Shadows)
En concordancia con el principio de diseño *"sombras nunca grises/negras"*, las variables de elevación utilizan composiciones de azul (`rgba(9, 80, 246, ...)`) y amarillo (`rgba(255, 236, 1, ...)`):
- `--shadow-float`: `0 25px 50px -12px rgba(9, 80, 246, 0.15)`
- `--shadow-antigravity-deep`: `0 24px 64px rgba(9, 80, 246, 0.22)`
- `--shadow-cta-glow`: `0 0 28px rgba(255, 236, 1, 0.45), 0 8px 24px rgba(9, 80, 246, 0.18)`

### 2.4. Utilidades Personalizadas Oficiales (`@utility`)
- `double-bezel-outer` y `double-bezel-inner`: Firma geométrica que crea tarjetas con doble marco concéntrico translúcido con efecto hover reactivo.
- `cta-nested-pill` y `cta-nested-icon`: Estructura de botón pastilla con icono circular anidado que se desplaza horizontalmente en hover.
- `text-display`, `text-h1`, `text-h2`: Tipografías fluidas con `clamp()`, `line-height: 0.85-0.9` y `text-wrap: balance`.
- `kinetic-font-stretch`: Efecto hover con `transform: scaleX(1.08)` para microinteracciones de marca.
- `content-auto`: Optimización moderna con `content-visibility: auto; contain-intrinsic-size: auto none auto 650px;`.
- Keyframes y animaciones: `animate-floaty`, `animate-shuttle`, `animate-pulse-ring`, `animate-roundtrip`, `animate-grow-x`, `animate-marquee-left`.
- Accesibilidad en animación: Regla exhaustiva `@media (prefers-reduced-motion: reduce)` en líneas 357-370 que deshabilita animaciones y transiciones para usuarios sensibles al movimiento.

### 2.5. Diagnóstico de Integración de `globals.css`
**Desconexión Total con el Directorio `envios/`**:
A pesar de la excelente calidad técnica intrínseca de `contexto/globals.css`, **ninguna página de `envios/` hace referencia a este archivo**. En cambio, el CSS fue procesado y pegado directamente en bloques `<style>` de más de 5,800 líneas dentro de cada archivo HTML. Esto rompe el ciclo de integración continua y desacopla la fuente de verdad de los archivos de visualización.

---

## 3. CATÁLOGO EXHAUSTIVO DE LAS PÁGINAS WEB EN `envios/`

El directorio `d:\repositorios\ccc\envios` contiene **16 archivos `.html`**. A continuación se presenta el catálogo completo con métricas objetivas extraídas del código:

| Archivo | Peso (KB) | Líneas | Título (`<title>`) | Encabezado Principal (`<h1>`) | URL Canónica | Secciones / IDs Clave | Propósito del Documento |
| :--- | :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| `contacto.html` | 274.9 | 6,498 | Contacto y Pedidos en Mar del Plata \| Envíos DosRuedas | "Escribinoste respondemos" | `/contacto/` | `contact-hero`, `carrusel-redes` | Canal directo de comunicación, datos de base Friuli 1972, formulario comercial y links a WhatsApp. |
| `cotizar.html` | 270.1 | 6,643 | Cotizá tu Envío en Moto \| Envíos DosRuedas | "COTIZÁ TU ENVÍOY COMPARÁ" | `/cotizar/` | Hero, cotizador comparativo, pasos de despacho | Cotizador interactivo comparando tarifas Express vs LowCost con campos de retiro y entrega. |
| `home.html` | 400.9 | 8,784 | Mensajería en moto en Mar del Plata \| Envíos DosRuedas | "Mensajería en moto en Mar del Plata: El motor de tuúltima milla. Somos la solución a tus envíos" | `https://www.enviosdosruedas.com/` | Hero, servicios, cobertura (5 radios), testimonios, FAQ preview, WhatsApp CTA | Página principal institucional que centraliza la propuesta de valor, servicios, cobertura y accesos. |
| `html.html` | 500.2 | 8,880 | Mensajería en moto en Mar del Plata \| Envíos DosRuedas | "Mensajería en moto en Mar del Plata: El motor de tuúltima milla. Somos la solución a tus envíos" | `https://www.enviosdosruedas.com/` | Idénticas a `home.html` | **Archivo redundante/artefacto de copia**. Es un duplicado idéntico a `home.html` con sangría de 4 espacios. |
| `logistica-dosruedas.html` | 230.0 | 5,739 | Logística DosRuedas \| Seguimiento y Portales Digitales - Mar del Plata \| Envíos DosRuedas | "Seguí tu paquete en tiempo real e ingresá a tu panel operativo" | `/logistica-dosruedas/` | `rastreo`, `portales` | Portal de tracking con código EDR y accesos a paneles comerciales, cadetes y soporte. |
| `mardelivery.html` | 254.9 | 6,141 | MarDelivery \| Carta Digital, Pedidos QR y Cadetería en Mar del Plata \| Envíos DosRuedas | "Potenciá tu local comercial y gastronómico con MarDelivery" | `/mardelivery/` | Hero, funciones gastronómicas, planes | Servicio para gastronomía y comercios: menú QR, pedidos por WhatsApp y cadetería por turnos. |
| `nosotrosnuestras-redes.html` | 281.3 | 6,592 | Nuestras Redes y Comunidad \| Envíos DosRuedas | "Comunidad enlínea" | `/nosotros/nuestras-redes/` | Hero comunidad, feed redes, canales | Hub social con enlaces a Instagram, Facebook, WhatsApp comercial y novedades operativas. |
| `nosotrospreguntas-frecuentes.html` | 258.3 | 6,285 | Preguntas Frecuentes (FAQ) \| Envíos DosRuedas | "¿Tenés dudas?acá la respondemos" | `/nosotros/preguntas-frecuentes/` | `faq-hero`, `faq-categories` | Centro de ayuda con acordeones de preguntas sobre cobertura, Flex, tarifas y horarios. |
| `nossobresobre-nosotros.html` | 315.1 | 7,121 | Sobre Nosotros y Trayectoria \| Envíos DosRuedas | "Más que cadetería,somos logísticade confianza" | `/nosotros/sobre-nosotros/` | Historia, valores, equipo, cifras | Historia de la empresa (7+ años en MDQ), valores operativos, flota y compromiso de entrega. |
| `politicade-privacidad.html` | 277.4 | 6,328 | Política de Privacidad \| Envíos DosRuedas | "Política de Privacidad" | `/politica-de-privacidad/` | 10 cláusulas legales de privacidad | Marco legal sobre tratamiento de datos de usuarios, remitentes, destinatarios y paquetes. |
| `serviciosdeposito-fulfillment.html` | 326.4 | 7,255 | Depósito y Fulfillment para PyMEs \| Envíos DosRuedas | "Vos vendés, nosotroslo entregamos hoyen Mar del Plata" | `/servicios/deposito-fulfillment/` | Almacenamiento, picking, empaque, drop-off | Solución de depósito urbano en Friuli 1972, stock, empaque y despacho directo en el día. |
| `serviciosempresas-cuenta-corriente.html` | 221.2 | 5,529 | Cuenta Corriente para Empresas \| Envíos DosRuedas | "LOGÍSTICA CON CUENTA CORRIENTE PARA EMPRESAS" | `/servicios/empresas-cuenta-corriente/` | Beneficios B2B, facturación, requisitos | Propuesta para empresas y despachantes recurrentes: facturación quincenal/mensual y crédito operativo. |
| `serviciosenvios-express.html` | 298.1 | 6,878 | Envíos Express en Moto en Mar del Plata \| Envíos DosRuedas | "Envíos Express, puerta a puerta" | `/servicios/envios-express/` | Franja 3hs, radio tarifario, urgencias | Servicio prioritario punto a punto con despacho en franja horaria acotada y seguimiento directo. |
| `serviciosenvios-lowcost.html` | 296.4 | 6,857 | Cadetería y Envíos en el Día en Mar del Plata \| Envíos DosRuedas | "Cortás el pedidoy lo recibís hoyen Mar del Plata" | `/servicios/envios-lowcost/` | Ruteo masivo, corte 13:00 hs, tarifas fijas | Cadetería urbana económica ruteada con entrega en el día para ventas minoristas y particulares. |
| `serviciosenviosflex.html` | 382.9 | 8,086 | Mercado Envíos Flex en Mar del Plata \| Envíos DosRuedas \| Envíos DosRuedas | "Entregamos tu venta Flexantes de las 20:00 hsen Mar del Plata" | `/servicios/enviosflex/` | Ventajas Flex, horarios de corte, reputación ML | Servicio certificado para vendedores de Mercado Libre Flex en Mar del Plata (corte 15:00 hs). |
| `terminos-y-condiciones.html` | 230.0 | 5,739 | Logística DosRuedas \| Seguimiento y Portales Digitales - Mar del Plata \| Envíos DosRuedas | "Seguí tu paquete en tiempo real e ingresá a tu panel operativo" | `/logistica-dosruedas/` | Idénticas a `logistica-dosruedas.html` | **CONTENIDO CORRUPTO / SOBREESCRITO**: Es una copia exacta de `logistica-dosruedas.html`. Términos legales faltantes. |

---

## 4. AUDITORÍA TÉCNICA Y DE CALIDAD DE CÓDIGO POR DIMENSIONES

### Dimensión 1: Validez de HTML y Estructura Semántica

#### Hallazgos Observados:
1. **Etiquetas de estructura semántica**: Todas las páginas incluyen correctamente elementos de alto nivel `<header>`, `<nav>`, `<main id="main-content">` y `<footer>`, así como enlaces de salto para accesibilidad (`<a href="#main-content">Saltar al contenido principal</a>`).
2. **Jerarquía de Encabezados (H1 - H4)**:
   - Todas las páginas poseen exactamente 1 etiqueta `<h1>`, lo cual cumple con las directrices de SEO y semántica.
   - Sin embargo, en varios encabezados el espaciado entre palabras en el texto colapsa debido a cómo se compusieron los spans decorativos. Ejemplo en `home.html` (línea 6128): `"El motor de tuúltima milla"` (falta espacio entre "tu" y "última"), `"Escribinoste respondemos"` en `contacto.html`, `"COTIZÁ TU ENVÍOY COMPARÁ"` en `cotizar.html`, `"Comunidad enlínea"` en `nosotrosnuestras-redes.html`, `"nosotroslo entregamos hoyen"` en `serviciosdeposito-fulfillment.html`.
3. **Atributo `style` residual en `<html>`**:
   - En los 16 archivos, la etiqueta raíz se abre como:
     `<html lang="es" class="Tao-HW_variable _7WFhHG_variable H_MGqW_variable lwqvDa_variable scroll-smooth" data-scroll-behavior="smooth" style="">`
   - El atributo `style=""` está vacío e innecesario.
4. **Elemento Fantasma `#mobile-navigation-dialog`**:
   - En el botón de menú móvil de cada página figura:
     `aria-controls="mobile-navigation-dialog"` (ej. `home.html:6104`).
   - Sin embargo, **dicho elemento `#mobile-navigation-dialog` no existe en ningún lugar del documento**. Al abrir la página en pantalla pequeña, no hay estructura de diálogo para desplegar.
5. **Div Oculto Residual**:
   - Inmediatamente tras `<body>` aparece en todas las páginas: `<div hidden="" bis_skin_checked="1" data-sd-id="1"></div>`. Es un elemento inerte generado por herramientas de scraping.

---

### Dimensión 2: Arquitectura de CSS, Peso y Rendimiento

#### Hallazgos Observados:
1. **Desacoplamiento Absoluto de `contexto/globals.css`**:
   - 0 de los 16 archivos HTML incluyen una etiqueta `<link rel="stylesheet">`.
   - Todas las reglas CSS de Tailwind v4 fueron incrustadas dentro del `<head>` de cada archivo.
2. **Cuantificación del Bloat de CSS Embebido**:
   - **Peso total de los 16 archivos HTML**: 4.71 MB.
   - **Peso total de CSS embebido en etiquetas `<style>`**: **2.14 MB** (45.4% del repositorio web).
   - En páginas como `logistica-dosruedas.html` y `serviciosempresas-cuenta-corriente.html`, el CSS embebido representa el **54.5% y 54.9% del archivo completo**.
3. **Impacto en Rendimiento (Core Web Vitals - FCP y LCP)**:
   - Al no existir un archivo `.css` externo, el navegador **no puede almacenar en caché el CSS** para visitas posteriores a otras páginas. Cada transición entre páginas obliga a descargar y parsear más de 5,800 líneas de CSS repetido, bloqueando el hilo principal del analizador HTML (parser-blocking).
4. **Estilos en Línea Excesivos (`style="..."`)**:
   - Cada archivo contiene entre 19 y 83 atributos `style="..."` directamente en etiquetas HTML.
   - Muchos de estos estilos corresponden a estados congelados de animaciones de scroll o coordenadas: ej. `style="transform:translateY(-4.67867px)"` (`home.html:933`), `style="transform:translateY(-1.83874px)"` (`cotizar.html:561`).

---

### Dimensión 3: Carga de Tipografías y Recursos Estáticos

#### Hallazgos Observados:
1. **Rutas Relativas Rotas para Fuentes**:
   - En las líneas 8-71 de cada archivo se declaran reglas `@font-face` con la sintaxis:
     `src: url("../public/fuentes/Outfit/Outfit-VariableFont_wght.ttf") format("truetype");`
   - Si la carpeta `envios/` se sirve como raíz del servidor web (lo habitual al desplegar en Vercel, Netlify o Nginx), la ruta `../public` **no existirá en el servidor web**, generando errores **404 Not Found** inmediatos al cargar tipografías y forzando a los fallbacks locales Arial.
2. **Formato TTF vs WOFF2 (Sobrecarga de Red)**:
   - El directorio `public/fuentes/` contiene 86 archivos que totalizan **13.22 MB**.
   - Las 8 fuentes activas cargadas por página suman **1.92 MB** de archivos `.ttf` sin comprimir (`IBMPlexSans-VariableFont_wdth,wght.ttf` pesa 520 KB; `IBMPlexSans-Italic...` pesa 580 KB).
   - La conversión a formato moderno **WOFF2 con subconjunto de caracteres (Latin)** reduciría este peso a menos de 200 KB en total (ahorro superior al 85%).
3. **Recurso Huérfano `public/logo_nuevo.webp`**:
   - Existe un archivo `logo_nuevo.webp` (15 KB) en `public/`, pero **ninguna página de `envios/` lo utiliza**.

---

### Dimensión 4: JavaScript, Interactividad y Conversión

#### Hallazgos Observados:
1. **El Kill-Switch de Clics (`preventDefault`)**:
   - Al pie de **todos y cada uno de los 16 archivos** se encuentra la siguiente instrucción:
     ```html
     <script>document.addEventListener("click", function (e) { var a = e.target.closest && e.target.closest("a"); if (!a) return; var h = a.getAttribute("href") || ""; if (h.length > 1 && h.charAt(0) === "#") return; e.preventDefault(); }, true);</script>
     ```
   - **Efecto devastador**: Si el enlace `<a>` tiene un `href` que no comienza con `#` (es decir, todas las URLs absolutas a otras páginas y todos los enlaces de WhatsApp que inician con `https://`), el script llama a `e.preventDefault()`, **anulando la acción de clic**.
   - **Resultado en producción**: El usuario hace clic en "Hablar por WhatsApp", "Cotizar", "Servicios" o cualquier enlace externo/interno y **la página no hace absolutamente nada**.
2. **Navegación Móvil Deshabilitada**:
   - El botón `#mobile-menu-toggle-opt` (`home.html:6102`) no posee ningún evento JavaScript asociado ni atributo `onclick`.
   - En pantallas móviles (donde la barra de escritorio `lg:flex` está oculta con `hidden`), el usuario queda atrapado sin poder navegar.
3. **Menús Desplegables de Escritorio Inertes**:
   - Los botones `<button aria-haspopup="true" aria-expanded="false">Servicios</button>` no tienen JavaScript para abrir ningún submenu.
4. **Formularios Inertes (Cotización y Contacto)**:
   - `cotizar.html:5509`: `<form novalidate="" class="space-y-5 relative z-10" data-sd-id="122">`
   - `contacto.html:5397`: `<form data-testid="contact-main-form" class="space-y-5" style="opacity:1" data-sd-id="137">`
   - Ambos formularios **carecen de atributo `action`**, **carecen de atributo `method`** y **carecen de manejador `onsubmit` o event listener**. Al presionar "Enviar Mensaje" o "Cotizar", los datos se pierden.
5. **Rastreo de Paquetes Inoperativo**:
   - En `logistica-dosruedas.html:4870-4906`, el formulario de búsqueda de código EDR y los botones de código de ejemplo (`EDR-4820-MDQ`, `EDR-999-OK`, `MELI-FLEX-MDQ`) son estáticos y no ejecutan ninguna consulta.

---

### Dimensión 5: Accesibilidad (a11y) y Experiencia de Usuario

#### Hallazgos Observados:
1. **Trampas y Focos Inválidos (`tabindex="0"` Anidado)**:
   - En los 16 archivos, el enlace del logotipo en el header envuelve un contenedor con `tabindex="0"`:
     ```html
     <a id="nav-logo-opt" ...>
       <div ...>
         <div class="relative w-10 h-10 shrink-0" tabindex="0" ...>
           <img alt="Logo Envíos Dos Ruedas" ...>
         </div>
       </div>
     </a>
     ```
     Tener un elemento con `tabindex="0"` dentro de un enlace interactivo `<a>` viola las pautas WCAG (elementos interactivos anidados), provocando doble tabulación y desorientación para lectores de pantalla.
   - En `home.html:8147` (y en otros archivos), un `div` con `tabindex="0"` envuelve a un `<button type="submit">`, repitiendo el mismo error de accesibilidad.
2. **Auditoría de Textos Alternativos en Imágenes (`alt`)**:
   - 5 archivos contienen imágenes con texto alternativo genérico e inútil: `alt="Image"` (`logistica-dosruedas.html`, `nosotrosnuestras-redes.html`, `politicade-privacidad.html`, `serviciosempresas-cuenta-corriente.html`, `terminos-y-condiciones.html`).
   - 5 archivos contienen imágenes con `alt=""` vacío en contextos que comunican contenido visual (`cotizar.html`, `home.html`, `html.html`, `serviciosenvios-express.html`, `serviciosenvios-lowcost.html`).
3. **Auditoría de Contraste Cromático**:
   - **Amarillo sobre Azul (`#FFEC01` sobre `#0950F6`)**: Ratio **4.99:1**. Cumple WCAG AA para texto normal y WCAG AAA para texto grande.
   - **Blanco sobre Azul (`#FFFFFF` sobre `#0950F6`)**: Ratio **6.09:1**. Cumple WCAG AA.
   - **Azul sobre Blanco (Texto de Párrafos `#0950F6` sobre `#FFFFFF`)**: Ratio **6.09:1**. Cumple contraste AA numérico, pero produce **fatiga visual y aberración cromática** (cromoestereopsis) al leer bloques densos de texto en azul eléctrico saturado sin un matiz oscuro o neutro.
   - **Amarillo sobre Blanco (`#FFEC01` sobre `#FFFFFF`)**: Ratio **1.22:1**. **Fallo crítico absoluto de contraste** (mínimo requerido 4.5:1). Si bien el sistema prohíbe amarillo sobre blanco, se detectaron iconos amarillos o spans decorativos cerca de fondos claros que comprometen la visibilidad.
4. **Cursor Forzado Globalmente**:
   - `<body style="cursor:pointer">` en los 16 archivos altera el comportamiento estándar del cursor del sistema operativo, impidiendo al usuario distinguir visualmente qué elementos son clickeables y cuáles son meros textos de lectura.

---

### Dimensión 6: SEO, Metadatos y Datos Estructurados

#### Hallazgos Observados:
1. **Títulos y Metadescripciones**:
   - Los títulos y metadescripciones están redactados de manera profesional y contienen palabras clave locales relevantes ("Mar del Plata", "moto", "Flex", "última milla").
   - **Anomalía en `serviciosenviosflex.html`**: El título repite la marca dos veces: `"Mercado Envíos Flex en Mar del Plata | Envíos DosRuedas | Envíos DosRuedas"`.
   - **Anomalía en `terminos-y-condiciones.html`**: Presenta el título y descripción de logística: `"Logística DosRuedas | Seguimiento y Portales Digitales..."`.
2. **OpenGraph y Twitter Cards**:
   - 15 de los 16 archivos apuntan su `og:image` a `https://www.enviosdosruedas.com/og-image.jpg`. Dicho archivo no existe en el repositorio local.
   - `serviciosenvios-express.html` apunta a una ruta dinámica con hash de build de Next.js: `https://www.enviosdosruedas.com/servicios/envios-express/opengraph-image?488cd29f142ce45b`.
3. **Ausencia Total de Datos Estructurados (Schema.org JSON-LD)**:
   - **0 de las 16 páginas** poseen marcado `application/ld+json`.
   - Para un negocio logístico físico con sede en Mar del Plata (Friuli 1972) y teléfono comercial, es crítico contar con esquemas `LocalBusiness`, `PostalAddress`, `FAQPage` y `Service` para posicionar en Google Maps, Knowledge Graph y fragmentos enriquecidos de búsqueda.
4. **Directiva `meta name="referrer" content="no-referrer"`**:
   - Presente en todos los archivos. Provoca que las herramientas de analítica (Google Analytics, Search Console, píxeles de conversión) pierdan la procedencia de las visitas cuando los usuarios navegan desde o hacia sitios externos.

---

### Dimensión 7: Hospedaje de Activos y Resiliencia

#### Hallazgos Observados:
1. **Dependencia Total de Bucket Externo Supabase**:
   - Todas las imágenes del sitio se descargan desde:
     `https://vgbujcuwptvheqijyjbe.supabase.co/storage/v1/object/public/clone-assets/<hash>.webp`
   - Se identificaron **24 hashes de imágenes distintos**.
   - No hay copia de seguridad local de estas imágenes en `public/`. Si la instancia de Supabase se desactiva, todo el catálogo visual del sitio web colapsa.
2. **Falta de Dimensiones Explícitas (`width`/`height`) en `<img>`**:
   - Las imágenes utilizan la clase `data-nimg="fill"` y estilo `position:absolute;height:100%;width:100%`, heredado del componente `<Image fill>` de Next.js. Al no tener dimensiones intrínsecas en el HTML estático, provocan desfasajes de diseño acumulado (Cumulative Layout Shift - CLS) durante la renderización inicial.

---

### Dimensión 8: Artefactos de Scraping y Extensiones de Navegador

#### Hallazgos Observados:
1. **Atributos de Bloqueador de Publicidad (`bis_skin_checked`)**:
   - Aparece entre **139 y 388 veces por archivo** (totalizando más de 3,500 ocurrencias en el proyecto). Es un atributo inyectado por extensiones de navegador como *Stands Fair AdBlocker* al guardar el HTML desde el inspector.
2. **Atributos de Superdesign (`data-sd-id`)**:
   - Aparece entre **393 y 950 veces por archivo** (totalizando más de 9,000 ocurrencias). Es un atributo de rastreo de nodos del editor canvas.
3. **Atributo `bis_register` en `<body>`**:
   - En `home.html:6013` (y en otros archivos), `<body>` contiene un string en base64 de registro de adblocker:
     `bis_register="W3sibWFzdGVyIjp0cnVlLCJleHRlbnNpb25JZCI6ImVwcGlvY2VtaG1ubGJoanBsY2drb2ZjaWllZ29tY29uIi..."`
4. **Componente Desechable de Next.js Router**:
   - Al final de cada archivo figura:
     `<next-route-announcer style="position:absolute"><template shadowrootmode="open"><div aria-live="assertive" id="__next-route-announcer__"...></div></template></next-route-announcer>`
     Es un nodo residual generado por el enrutador de Next.js que carece de utilidad en páginas puramente estáticas.

---

## 5. RÚBRICA DE EVALUACIÓN Y AUDITORÍA TÉCNICA

A continuación se evalúa el estado del código de acuerdo a criterios objetivos con escala del 1 al 5:
- **1/5 - Crítico / Roto**: Falla que impide la operación básica o incumple estándares elementales.
- **2/5 - Deficiente**: Presenta problemas severos que afectan navegación, SEO o rendimiento.
- **3/5 - Aceptable**: Funciona pero con vicios técnicos, redundancias o advertencias graves.
- **4/5 - Bueno**: Cumple estándares con oportunidades menores de optimización.
- **5/5 - Excelente**: Cumple plenamente con las mejores prácticas de la industria.

| Criterio Evaluado | Puntuación | Estado | Diagnóstico Resumido |
| :--- | :---: | :---: | :--- |
| **Arquitectura de CSS y Tokens** | **3.5 / 5** | Aceptable | `globals.css` está excelentemente estructurado con Tailwind v4 y Sistema Lúcido, pero está 100% desconectado de los HTMLs, los cuales replican 2.14 MB de CSS inlined no cacheable. |
| **Integridad de Archivos y Contenidos** | **1.5 / 5** | Crítico | `terminos-y-condiciones.html` está sobreescrito por `logistica-dosruedas.html` (contenido legal perdido). `html.html` es un duplicado redundante de `home.html`. |
| **Interactividad y JavaScript** | **1.0 / 5** | Roto | Script de bloqueo `preventDefault` activo en todos los archivos, impidiendo navegación y WhatsApp. 0% de interactividad funcional en menús, formularios, acordeones y rastreo. |
| **Rendimiento Web y Carga de Recursos** | **2.0 / 5** | Deficiente | 2.14 MB de CSS inlined bloqueante; 1.92 MB de fuentes TTF sin comprimir; rutas de fuentes relativas rotas; falta de caché HTTP en hojas de estilo. |
| **Accesibilidad (a11y) y UX** | **2.5 / 5** | Deficiente | Landmarks presentes, pero con foco inválido (`tabindex="0"` anidado en logo y botones), diálogo móvil inexistente en DOM, textos `alt="Image"` o vacíos, y cursor global pointer. |
| **SEO y Metadatos** | **3.0 / 5** | Aceptable | Títulos y metadescripciones bien redactados. Ausencia total de JSON-LD LocalBusiness; imagen OG rota; título duplicado en Flex; `no-referrer` perjudicial para analítica. |
| **Resiliencia e Infraestructura de Activos** | **1.5 / 5** | Crítico | 100% de imágenes dependientes de un bucket de pruebas en Supabase; cero imágenes locales; riesgo de caída total si el bucket externo expira. |
| **Limpieza y Calidad de Código HTML** | **2.0 / 5** | Deficiente | Miles de atributos parásitos de scraping (`bis_skin_checked`, `data-sd-id`, `bis_register`, `<next-route-announcer>`). |

**Puntuación Promedio General: 2.1 / 5.0 (Nivel de Riesgo Operativo: ALTO)**

---

## 6. PLAN DE ACCIONES Y RECOMENDACIONES PRIORIZADAS

### Prioridad P0: Bloqueadores Inmediatos (Implementar antes de cualquier lanzamiento)

1. **Eliminar el Script de Interceptación de Clics**:
   - **Ubicación**: Última etiqueta `<script>` en los 16 archivos de `envios/` (línea ~6440 a ~8880).
   - **Acción**: Suprimir completamente el listener `document.addEventListener("click", ... e.preventDefault(); ...)` para reactivar la navegación de enlaces y los botones directos a WhatsApp.
2. **Restaurar el Contenido Real de `terminos-y-condiciones.html`**:
   - **Ubicación**: `envios/terminos-y-condiciones.html`.
   - **Acción**: Reemplazar el código actual (que es una réplica errónea de `logistica-dosruedas.html`) por el texto legal auténtico de Términos del Servicio de Envíos DosRuedas, con su título y URL canónica correspondientes.
3. **Eliminar el Archivo Redundante `envios/html.html`**:
   - **Acción**: Eliminar de forma segura `envios/html.html` para evitar duplicidad de contenido, confusión en el build y canibalización SEO con `home.html`.
4. **Remover el Atributo `style="cursor:pointer"` de `<body>`**:
   - **Ubicación**: Etiqueta `<body>` en los 16 archivos HTML.
   - **Acción**: Eliminar el atributo inline para devolver el cursor estándar de texto y flecha a los elementos no interactivos.

---

### Prioridad P1: Arquitectura y Rendimiento Crítico

5. **Externalizar el CSS en una Hoja de Estilos Compartida**:
   - **Acción**: Compilar `contexto/globals.css` mediante Tailwind CSS hacia un archivo centralizado (ej. `public/css/globals.css` o `/dist/assets/index.css`) y reemplazar las 5,800 líneas inlined de cada archivo HTML por una única etiqueta:
     `<link rel="stylesheet" href="/css/globals.css">`.
   - **Impacto**: Reducción de más de **2 MB de HTML** en el proyecto, posibilitando que el navegador almacene el CSS en caché una sola vez para todas las páginas.
6. **Localizar y Respaldar Todas las Imágenes de Supabase**:
   - **Acción**: Descargar las 24 imágenes referenciadas en Supabase y guardarlas en `public/images/`.
   - **Acción en HTML**: Reemplazar las URLs absolutas `https://vgbujcuwptvheqijyjbe.supabase.co/...` por rutas locales relativas o absolutas a la raíz `/images/...`.
7. **Optimizar Tipografías: Conversión a WOFF2 y Rutas Absolutas**:
   - **Acción**: Convertir las fuentes clave (Outfit, Anton, Bebas Neue, Geist Mono, IBM Plex Sans) a formato `.woff2` y actualizar las declaraciones `@font-face` con rutas absolutas desde la raíz `/fuentes/...` en lugar de `../public/fuentes/...`.

---

### Prioridad P2: Funcionalidad, Accesibilidad y Limpieza

8. **Implementar el Diálogo de Navegación Móvil y Dropdowns**:
   - **Acción**: Crear el marcado del contenedor `#mobile-navigation-dialog` en cada página y añadir un script ligero (o solución basada en CSS con checkbox / details) que abra y cierre el menú al pulsar `#mobile-menu-toggle-opt`.
   - **Acción**: Agregar funcionalidad de despliegue a los dropdowns del menú superior.
9. **Corregir Violaciones de Accesibilidad (`tabindex` y `alt`)**:
   - **Acción**: Quitar `tabindex="0"` de los divs internos del logotipo en el header y de los divs que envuelven botones submit.
   - **Acción**: Reemplazar los textos `alt="Image"` por descripciones semánticas representativas del servicio.
10. **Sanitizar Artefactos de Scraping**:
    - **Acción**: Ejecutar una tarea automatizada de limpieza para remover todos los atributos `bis_skin_checked="1"`, `bis_register`, `data-sd-id` y los tags `<next-route-announcer>`.
11. **Configurar Acciones de Formularios**:
    - **Acción**: Enlazar los formularios de `contacto.html` y `cotizar.html` hacia un endpoint operativo (API, webhook de mensajería o redirección dinámica a WhatsApp con parámetros codificados).

---

### Prioridad P3: Optimización SEO Avanzada

12. **Incorporar Datos Estructurados JSON-LD**:
    - **Acción**: Añadir esquema `LocalBusiness` en `home.html` y `contacto.html` con nombre de empresa, dirección en Friuli 1972, teléfono `+54 9 223 660-2699`, horario de atención y área de servicio en Mar del Plata.
    - **Acción**: Añadir esquema `FAQPage` en `nosotrospreguntas-frecuentes.html`.
13. **Subsanar Errores Menores de Títulos y Metadatos**:
    - **Acción**: Corregir la duplicación de marca en `serviciosenviosflex.html`.
    - **Acción**: Modificar `meta name="referrer"` a `strict-origin-when-cross-origin` para permitir analítica web confiable.
    - **Acción**: Incorporar la imagen local `public/og-image.jpg` referenciada por los tags OpenGraph.

---

*Fin del Informe de Auditoría Técnica y Relevamiento de Código.*
