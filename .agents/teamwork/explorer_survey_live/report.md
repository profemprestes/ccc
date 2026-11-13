# Auditoría Exhaustiva: Sitio en Producción vs. Repositorio Local
**Envíos DosRuedas (`https://www.enviosdosruedas.com/`)**

- **Fecha de Auditoría**: 13 de Noviembre de 2026
- **Auditor**: Live Site & Production Parity Explorer
- **Alcance**: Inspección en vivo de `https://www.enviosdosruedas.com/`, rastreo de URLs públicas, validación de interactividad (WhatsApp, formularios, calculadoras, rastreo), inventario y contraste 1:1 con `envios/`, `public/` y configuraciones del repositorio.

---

## 1. Resumen Ejecutivo

Se completó una auditoría exhaustiva e integral del sitio web en producción de **Envíos DosRuedas** (`https://www.enviosdosruedas.com/`) y su contraste punto por punto con los activos estáticos y recursos visuales almacenados en el repositorio local.

### Hallazgos Principales de Alto Impacto

1. **Disparidad Tecnológica Radical (Next.js en Vercel vs. Exportación Superdesign en Local)**:
   - **Producción**: Es una aplicación moderna desarrollada en **Next.js (App Router con Turbopack)**, desplegada sobre la infraestructura Edge de **Vercel** (`Server: Vercel`, datacenter `gru1`), con Server-Side Prerendering (`X-Nextjs-Prerender: 1`), Server Components y assets cacheados de forma inmutable (`/_next/static/immutable/...`).
   - **Repositorio (`envios/`)**: Los 16 archivos `.html` **no son el código fuente de Next.js**, sino clones/capturas del DOM estático exportados desde una sesión de diseño asistida por la herramienta **Superdesign** (evidenciado por entre 393 y 950 atributos `data-sd-id="..."` por archivo, y marcadores de extensión de navegador Bitwarden `bis_skin_checked="1"`). En esta exportación se eliminaron los scripts de hidratación de React, dejando inertes calculadoras y formularios.
2. **Corrupción Crítica de Archivo en Repositorio (`terminos-y-condiciones.html`)**:
   - El archivo local `envios/terminos-y-condiciones.html` es un **duplicado binario exacto** (mismo hash SHA-256: `D82177D1DF7E1F9D0004831753C35D367A68AE9158A02BC84AD701DF3FD15C8E`) de `envios/logistica-dosruedas.html`. El texto real legal de Términos y Condiciones que sí está activo en producción fue sobrescrito y se encuentra completamente ausente del repositorio local.
3. **Páginas Clave en Producción Ausentes en el Repositorio**:
   - `https://www.enviosdosruedas.com/cobertura/` (238 KB, mapa tarifario y zonas de Mar del Plata) **no existe** en `envios/`.
   - `https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata/` (105 KB, guía técnica para vendedores de Mercado Libre Flex) **no existe** en `envios/`.
   - `https://www.enviosdosruedas.com/servicios/` (213 KB, hub central de servicios) **no existe** en `envios/`.
4. **Vulnerabilidad Crítica de Dependencia de Activos (`Supabase clone-assets`)**:
   - En las páginas locales de `envios/*.html`, **las 31 imágenes referenciadas** apuntan a un bucket externo de Supabase (`https://vgbujcuwptvheqijyjbe.supabase.co/storage/v1/object/public/clone-assets/...`).
   - En el directorio local `public/` **no existe ninguna de estas imágenes** (únicamente existe `public/logo_nuevo.webp` y la carpeta de fuentes tipográficas). Si dicho bucket temporal de Supabase se pausa o elimina, todo el sitio local colapsará visualmente.
   - En cambio, en producción las imágenes están autoalojadas limpiamente (`/logo-envios-simplified.webp`, `/heroes/inicio-mapa.webp`, `/cards/fondo_*.webp`).
5. **Inconsistencias de SEO y Enrutamiento en Producción**:
   - **Desperdicio de redirecciones (Trailing Slash)**: `sitemap.xml` declara todas las URLs sin barra final (`/contacto`), pero la configuración del servidor Vercel fuerza `trailingSlash: true`, generando un salto obligatorio `308 Permanent Redirect` en cada página.
   - **URLs Fantasma en Sitemap**: `sitemap.xml` incluye `/servicios/plan-emprendedores` y `/servicios/envios-contrareembolso` como páginas individuales, pero en el servidor ambas aplican redirecciones 308 hacia `/servicios/empresas-cuenta-corriente/` y `/servicios/` respectivamente.
   - **Inconsistencia de Slug**: `/servicios/enviosflex/` responde 200 OK, pero la versión estándar con guion `/servicios/envios-flex/` devuelve un error **404 Not Found**.

---

## 2. Diagnóstico Técnico y de Infraestructura en Producción

### 2.1. Conectividad, Dominio y Certificado SSL

| Parámetro | Valor Observado en Producción | Evaluación |
| :--- | :--- | :--- |
| **Dominio Principal** | `https://www.enviosdosruedas.com/` | Configuración Canónica Activa |
| **Dominio Ápex** | `https://enviosdosruedas.com` | Redirige vía `307 Temporary Redirect` a `www.enviosdosruedas.com/` |
| **HTTP (Puerto 80)** | `http://www.enviosdosruedas.com` | Redirige vía `308 Permanent Redirect` a HTTPS |
| **Proveedor de Hosting** | **Vercel Edge Network** (`Server: Vercel`) | Pop / Datacenter: `gru1` (São Paulo, Brasil) |
| **Direcciones IP Resueltas** | `64.29.17.65`, `64.29.17.1` (Vercel Anycast) | Responde con baja latencia |
| **Certificado SSL/TLS** | Let's Encrypt (`CN=YR1`, Subject `*.enviosdosruedas.com`) | Válido: 14/Oct/2026 al 12/Ene/2027 |
| **Versión TLS y Cifrado** | TLSv1.3 con `TLS_AES_128_GCM_SHA256` | Cifrado moderno de alta seguridad |
| **Subject Alternative Names (SAN)**| `*.enviosdosruedas.com`, `enviosdosruedas.com` | Cobertura completa de subdominios |

### 2.2. Cabeceras de Seguridad y Configuración HTTP

Las cabeceras HTTP inspeccionadas demuestran una configuración de producción robusta:
- `Strict-Transport-Security`: `max-age=63072000; includeSubDomains; preload` (HSTS activo por 2 años).
- `Content-Security-Policy`: Estricta política `default-src 'self'`, permitiendo scripts de Google Maps, Google Tag Manager (`AW-17510443994`, `G-LSLQ3RJ8WT`), Google Analytics, Ahrefs (`analytics.ahrefs.com`) y unpkg. La directiva `form-action` autoriza explícitamente `'self' https://api.whatsapp.com`.
- `X-Frame-Options`: `SAMEORIGIN` (mitigación de clickjacking).
- `X-Content-Type-Options`: `nosniff` (prevención de MIME-sniffing).
- `Permissions-Policy`: `camera=(), microphone=(), geolocation=(self)`.
- `X-Nextjs-Prerender`: `1` (páginas SSG/ISR optimizadas para entrega estática desde Vercel CDN).

---

## 3. Mapeo de URLs Públicas, Sitemap y Rutas en Producción

### 3.1. Auditoría de `robots.txt`
El archivo `https://www.enviosdosruedas.com/robots.txt` responde con estado `200 OK` (458 bytes).
- **Reglas declaradas**:
  - Permite acceso a todos los bots (`*`, `Googlebot`, `Bingbot`, `Applebot`, `GPTBot`, `ClaudeBot`, `PerplexityBot`).
  - Bloquea explícitamente: `Disallow: /api/`, `Disallow: /admin/`, `Disallow: /revisar`.
  - Declara correctamente el Sitemap: `Sitemap: https://www.enviosdosruedas.com/sitemap.xml`.
- **Comprobación de Rutas Protegidas / Restringidas**:
  - `/revisar/`: Devuelve `401 Unauthorized` (64 bytes).
  - `/admin/`: Devuelve `401 Unauthorized` (64 bytes).
  - `/api/`: Devuelve `404 Not Found` (74 KB).

### 3.2. Matriz de Estado y Redirecciones de URLs

A continuación se detalla el comportamiento de cada URL descubierta en `sitemap.xml` y la navegación del sitio:

| URL Solicitada | Estado Inicial | Redirección (Location) | Estado Final | URL Canónica Declarada | Peso (Bytes) |
| :--- | :---: | :--- | :---: | :--- | :---: |
| `/` | `200 OK` | Ninguna | `200 OK` | `https://www.enviosdosruedas.com/` | 205.919 |
| `/servicios/` *(Hub central)* | `200 OK` | Ninguna | `200 OK` | `https://www.enviosdosruedas.com/servicios/` | 213.535 |
| `/servicios/envios-express` | `308 Perm` | `/servicios/envios-express/` | `200 OK` | `https://www.enviosdosruedas.com/servicios/envios-express/` | 174.748 |
| `/servicios/envios-lowcost` | `308 Perm` | `/servicios/envios-lowcost/` | `200 OK` | `https://www.enviosdosruedas.com/servicios/envios-lowcost/` | 159.528 |
| `/servicios/enviosflex` | `308 Perm` | `/servicios/enviosflex/` | `200 OK` | `https://www.enviosdosruedas.com/servicios/enviosflex/` | 212.011 |
| `/servicios/envios-flex` *(con guion)* | `308 Perm` | `/servicios/envios-flex/` | **`404 Not Found`** | N/A | 74.094 |
| `/servicios/deposito-fulfillment` | `308 Perm` | `/servicios/deposito-fulfillment/` | `200 OK` | `https://www.enviosdosruedas.com/servicios/deposito-fulfillment/` | 175.058 |
| `/servicios/empresas-cuenta-corriente` | `308 Perm` | `/servicios/empresas-cuenta-corriente/` | `200 OK` | `https://www.enviosdosruedas.com/servicios/empresas-cuenta-corriente/` | 105.328 |
| `/servicios/plan-emprendedores` | `308 Perm` | `/servicios/empresas-cuenta-corriente/` | `200 OK` *(Alias)*| `https://www.enviosdosruedas.com/servicios/empresas-cuenta-corriente/` | 105.328 |
| `/servicios/envios-contrareembolso`| `308 Perm` | `/servicios/` | `200 OK` *(Alias)*| `https://www.enviosdosruedas.com/servicios/` | 213.535 |
| `/cotizar` | `308 Perm` | `/cotizar/` | `200 OK` | `https://www.enviosdosruedas.com/cotizar/` | 128.462 |
| `/cobertura` | `308 Perm` | `/cobertura/` | `200 OK` | `https://www.enviosdosruedas.com/cobertura/` | 238.048 |
| `/logistica-dosruedas` | `308 Perm` | `/logistica-dosruedas/` | `200 OK` | `https://www.enviosdosruedas.com/logistica-dosruedas/` | 97.133 |
| `/mardelivery` | `308 Perm` | `/mardelivery/` | `200 OK` | `https://www.enviosdosruedas.com/mardelivery/` | 111.730 |
| `/guias/envios-flex-mar-del-plata` | `308 Perm` | `/guias/envios-flex-mar-del-plata/` | `200 OK` | `https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata/` | 105.275 |
| `/contacto` | `308 Perm` | `/contacto/` | `200 OK` | `https://www.enviosdosruedas.com/contacto/` | 134.561 |
| `/nosotros/sobre-nosotros` | `308 Perm` | `/nosotros/sobre-nosotros/` | `200 OK` | `https://www.enviosdosruedas.com/nosotros/sobre-nosotros/` | 163.099 |
| `/nosotros/preguntas-frecuentes` | `308 Perm` | `/nosotros/preguntas-frecuentes/` | `200 OK` | `https://www.enviosdosruedas.com/nosotros/preguntas-frecuentes/` | 137.253 |
| `/nosotros/nuestras-redes` | `308 Perm` | `/nosotros/nuestras-redes/` | `200 OK` | `https://www.enviosdosruedas.com/nosotros/nuestras-redes/` | 135.102 |
| `/politica-de-privacidad` | `308 Perm` | `/politica-de-privacidad/` | `200 OK` | `https://www.enviosdosruedas.com/politica-de-privacidad/` | 123.237 |
| `/terminos-y-condiciones` | `308 Perm` | `/terminos-y-condiciones/` | `200 OK` | `https://www.enviosdosruedas.com/terminos-y-condiciones/` | 122.706 |

---

## 4. Auditoría de Elementos Funcionales e Interactivos en Producción

### 4.1. Canales y Enlaces de WhatsApp
- **Número Único Utilizado**: `+54 9 223 660-2699` (formato en enlaces: `542236602699`).
- **Estructura de URLs**:
  - `https://api.whatsapp.com/send/?phone=542236602699`
  - Variantes con mensaje predeterminado: `https://api.whatsapp.com/send/?phone=542236602699&text=Hola%20Envíos%20DosRuedas!%20Quiero%20hacer%20una%20consulta%20de%20envíos`.
- **Integración y Distribución**:
  - Presente en **todas** las páginas del sitio (entre 3 y 11 botones/enlaces por página).
  - Incluye atributos de seguridad `target="_blank"` y `rel="noopener noreferrer"`.
  - En páginas de servicios (`enviosflex`, `deposito-fulfillment`), el número de llamadas a la acción vía WhatsApp asciende a 11 puntos de contacto por página.

### 4.2. Teléfono Fijo, Correo Electrónico y Dirección
- **Enlace Telefónico (`tel:`)**: `tel:+542236602699` (texto visible: `223 660-2699`).
- **Enlace de Correo (`mailto:`)**: `mailto:matiascejas@enviosdosruedas.com` (correo personal/comercial del fundador Matías Cejas).
- **Ubicación Física**: Base operativa central en `Friuli 1972, Mar del Plata, Buenos Aires (B7600), Argentina`.
- **Horarios Declarados**:
  - Lunes a Viernes: 09:00 a 18:00 hs.
  - Sábados: 10:00 a 15:00 hs.

### 4.3. Redes Sociales y Plataformas Externas
- **Instagram**: `https://www.instagram.com/enviosdosruedas/` (enlaces directos a publicaciones destacadas: `DEaAGAmRMKj`, `DK12WIDslKW`, `DJhlS5xOrTb`).
- **Facebook**: `https://www.facebook.com/enviosdosruedas/` y publicaciones oficiales (`pfbid0a1i...`, `pfbid03WP...`).
- **Plataformas Propias Vinculadas**:
  - **Portal Logístico**: `https://www.logisticadosruedas.com/` (portal de autogestión de despachos para empresas y comercios).
  - **Plataforma E-Commerce**: `https://shopdosruedas.com/` (tienda y catálogo digital).
  - **MarDelivery**: Servicio de carta digital, QR gastronómico y ruteo para locales.

### 4.4. Formularios y Herramientas Interactivas en Vivo
1. **Cotizador Interactivo (`/cotizar/`)**:
   - Campos de entrada:
     - `guia-origen-input`: Campo combobox con autocompletado para dirección de retiro (`role="combobox"`, `aria-autocomplete="list"`).
     - `guia-destino-input`: Campo combobox con autocompletado para dirección de entrega.
     - `nombre`: Nombre completo del solicitante.
     - `telefono`: Teléfono de contacto (`type="tel"`).
     - `producto`: Descripción del paquete.
   - Botón de acción: `Ver las dos tarifas` (calcula en tiempo real la comparativa entre tarifa Express y LowCost según distancia kilométrica calculada).
2. **Sistema de Rastreo de Envíos (`/logistica-dosruedas/`)**:
   - Campo de entrada con máscara y validación: `placeholder="Ej: EDR-8420-MDQ o código numérico..."`.
   - Botones interactivos de simulación de estado para demostración:
     - `EDR-4820-MDQ (En camino)`
     - `EDR-999-OK (Entregado)`
     - `MELI-FLEX-MDQ (Flex)`
   - Botón: `Rastrear Envío`.
3. **Formulario de Captura Comercial (`/` y `/contacto/`)**:
   - Inputs: `nombre`, `empresa`, `volumen` (select con rangos: `1 a 50 envíos`, `51 a 200 envíos`, `Más de 200 envíos`).
   - Botón: `Hablar por WhatsApp` (compone dinámicamente un mensaje preformateado y abre la sesión de WhatsApp).
4. **Formulario B2B (`/servicios/empresas-cuenta-corriente/`)**:
   - Botón de solicitud directa: `Pedir Apertura de Cuenta`.

---

## 5. Matriz de Paridad 1:1: Producción vs. Archivos Locales en `envios/`

A continuación se presenta el contraste riguroso entre cada archivo `.html` existente en la carpeta `envios/` del repositorio y su contraparte viva en producción:

| Archivo Local en `envios/` | Tamaño Local | URL Correspondiente en Producción | Tamaño en Vivo | Estado de Paridad | Discrepancias Identificadas |
| :--- | :---: | :--- | :---: | :---: | :--- |
| `home.html` | 410.547 B | `https://www.enviosdosruedas.com/` | 205.919 B | **Parcial** | Es un clon estático de Superdesign (`data-sd-id=950`). Las imágenes apuntan a Supabase externo (`clone-assets`). Faltan scripts de hidratación de Next.js. |
| `html.html` | 512.198 B | N/A (Duplicado huérfano de la home) | N/A | **Duplicado** | Archivo huérfano de 512 KB con código HTML expandido de la home y marcadores de Bitwarden (`bis_skin_checked=388`). Debe eliminarse. |
| `contacto.html` | 281.519 B | `https://www.enviosdosruedas.com/contacto/` | 134.561 B | **Parcial** | Mismo contenido visual, pero con 527 atributos `data-sd-id`, imágenes en Supabase y sin submit de React. |
| `cotizar.html` | 276.615 B | `https://www.enviosdosruedas.com/cotizar/` | 128.462 B | **Inerte** | Contiene el markup visual del cotizador (`data-sd-id=578`), pero carece del motor JavaScript de autocompletado y cálculo de tarifas en vivo. |
| `logistica-dosruedas.html` | 235.560 B | `https://www.enviosdosruedas.com/logistica-dosruedas/`| 97.133 B | **Parcial** | Markup estático (`data-sd-id=411`). Botones de simulación de rastreo no actualizan el estado dinámico. |
| `mardelivery.html` | 260.987 B | `https://www.enviosdosruedas.com/mardelivery/` | 111.730 B | **Parcial** | Estructura visual equivalente (`data-sd-id=457`), imágenes alojadas en Supabase bucket externo. |
| `nosotrosnuestras-redes.html` | 288.034 B | `https://www.enviosdosruedas.com/nosotros/nuestras-redes/` | 135.102 B | **Parcial** | Nombre de archivo aplanado. Embeds y enlaces a Instagram/Facebook funcionales en enlaces, assets en Supabase. |
| `nosotrospreguntas-frecuentes.html`| 264.544 B | `https://www.enviosdosruedas.com/nosotros/preguntas-frecuentes/` | 137.253 B | **Parcial** | Los acordeones inician cerrados sin interacción JS local. Faltan datos estructurados JSON-LD Schema.org FAQPage que sí están en producción. |
| `nossobresobre-nosotros.html` | 322.675 B | `https://www.enviosdosruedas.com/nosotros/sobre-nosotros/` | 163.099 B | **Parcial** | Nombre de archivo con errata de prefijo (`nossobresobre`). Contenido textual coincide con producción. |
| `politicade-privacidad.html` | 284.052 B | `https://www.enviosdosruedas.com/politica-de-privacidad/` | 123.237 B | **Parcial** | Texto legal íntegro y coincidente. Depende de Supabase para imágenes del header/footer. |
| `serviciosdeposito-fulfillment.html`| 334.251 B | `https://www.enviosdosruedas.com/servicios/deposito-fulfillment/`| 175.058 B | **Parcial** | Tabla de planes y tarifas coincide con producción. 753 etiquetas `data-sd-id`. |
| `serviciosempresas-cuenta-corriente.html`| 226.483 B | `https://www.enviosdosruedas.com/servicios/empresas-cuenta-corriente/`| 105.328 B | **Parcial** | Contenido coincidente. Formulario B2B inerte. |
| `serviciosenvios-express.html` | 305.242 B | `https://www.enviosdosruedas.com/servicios/envios-express/` | 174.748 B | **Parcial** | Precios y zonas coinciden ($3.700 base). Imágenes en Supabase. |
| `serviciosenvios-lowcost.html` | 303.509 B | `https://www.enviosdosruedas.com/servicios/envios-lowcost/` | 159.528 B | **Parcial** | Precios y franjas horarias coinciden ($3.000 base). Imágenes en Supabase. |
| `serviciosenviosflex.html` | 392.043 B | `https://www.enviosdosruedas.com/servicios/enviosflex/` | 212.011 B | **Parcial** | Contenido exhaustivo de Mercado Envíos Flex. 889 etiquetas `data-sd-id`. |
| **`terminos-y-condiciones.html`** | **235.560 B** | `https://www.enviosdosruedas.com/terminos-y-condiciones/` | **122.706 B** | **CORRUPTO / ERROR CRÍTICO** | **El archivo local es un duplicado idéntico de `logistica-dosruedas.html` (SHA-256 idéntico). El texto legal de Términos y Condiciones está totalmente perdido en el repositorio local.** |
| *(No existe en repo)* | N/A | `https://www.enviosdosruedas.com/cobertura/` | 238.048 B | **Faltante en Repo** | Página vital con tarifas por barrio y zonas de cobertura. Ausente en `envios/`. |
| *(No existe en repo)* | N/A | `https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata/` | 105.275 B | **Faltante en Repo** | Guía operativa de Mercado Envíos Flex. Ausente en `envios/`. |
| *(No existe en repo)* | N/A | `https://www.enviosdosruedas.com/servicios/` | 213.535 B | **Faltante en Repo** | Página hub central que agrupa la oferta de servicios. Ausente en `envios/`. |

---

## 6. Auditoría de Recursos Visuales y Estilos (`public/`, `contexto/`)

### 6.1. Inventario del Directorio `public/`
Al analizar el directorio local `public/`, se encontraron **87 archivos**, pero la gran mayoría corresponde a variantes de fuentes tipográficas:
- `public/logo_nuevo.webp` (36.454 bytes) — **Único asset gráfico/imagen en todo el repositorio**.
- `public/fuentes/`:
  - `Anton/` (TTF regular + licencia OFL).
  - `Anton_SC/` (TTF regular + licencia OFL).
  - `Bebas_Neue/` (TTF regular + licencia OFL).
  - `Geist_Mono/` (Variable font wght + italic, más 10 cortes estáticos Black, Bold, Light, etc.).
  - `IBM_Plex_Sans/` (Variable font wdth/wght + italic).
  - `Outfit/` (Variable font wght).

### 6.2. La Brecha Crítica de Imágenes Locales
- En `envios/*.html`, se encontraron **31 imágenes distintas**.
- **100% de ellas apuntan a**: `https://vgbujcuwptvheqijyjbe.supabase.co/storage/v1/object/public/clone-assets/<hash>.(webp|png|svg)`.
- **Ninguna de estas 31 imágenes existe en `public/` ni en otra carpeta del repositorio**.
- En producción, el sitio web sirve las imágenes desde rutas relativas limpias de Next.js:
  - `/logo-envios-simplified.webp`
  - `/heroes/inicio-mapa.webp`
  - `/cards/fondo_emprendedores.webp`
  - `/cards/fondo_express.webp`
  - `/cards/fondo_flex.webp`
  - `/cards/fondo_lowcost.webp`
- **Riesgo Operativo**: Si el bucket de Supabase `clone-assets` caduca o se bloquea el acceso público, las 16 páginas estáticas de `envios/` quedarán con todas sus imágenes rotas.

### 6.3. Coherencia de Marca y Estilos (`contexto/globals.css`)
- `contexto/globals.css` define con precisión el sistema de diseño Tailwind CSS v4 bajo la **Ley de Tres Colores**:
  - Azul Primario: `#0950F6` (tope de oscuridad, escala 50 a 500).
  - Amarillo Vial: `#FFEC01` (señalética y acentos, escala 50 a 600).
  - Blanco: `#FFFFFF` (lienzo base).
  - Neutralización de paletas por defecto de Tailwind (`stone`, `neutral`, `green` forzados a `initial`).
  - Tipografías canónicas: Anton SC (display), Bebas Neue (subheading), Outfit (sans), Geist Mono (mono).
- **Paridad con Producción**: Tanto la aplicación Next.js en producción como las páginas en `envios/` respetan fielmente estos tokens de color (`#0950F6` y `#FFEC01`), las familias tipográficas y las clases utilitarias (`shadow-cta-glow`, `button-pill`, `card-token`).

---

## 7. Análisis de Contenidos, Precios y Discrepancias Comerciales

### 7.1. Estructura de Precios Validada (Marzo - Noviembre 2026)
A través de la inspección de datos estructurados Schema.org, metadatos y contenido textual en vivo, se confirmó la consistencia de las tarifas vigentes:

| Zona | Radio Kilométrico | Tarifa Express (Franja 2-3 hs) | Tarifa LowCost (En el día) | Observaciones |
| :---: | :---: | :---: | :---: | :--- |
| **Zona 1** | 0 a 3 km (Centro / Macrocentro) | **$3.700** | **$3.000** | Sin recargo hasta 5 kg |
| **Zona 2** | 3 a 5 km (Güemes / Puerto / Const.) | **$4.600** | **$4.000** | Sin recargo hasta 5 kg |
| **Zona 3** | 5 a 7 km (Mogotes / Constitución ext.) | **$6.100** | **$5.300** | Sin recargo hasta 5 kg |
| **Zona 4** | 7 a 10 km (Periferia urbana MDQ) | **$8.200** | **$7.000** | Sin recargo hasta 5 kg |
| **Excedente > 10 km** | Por km adicional (redondeo ceil) | **+$1.000 / km** | **+$700 / km** | Ej: 10,3 km = 11 km × tarifa/km |
| **Parada Adicional** | Punto intermedio de ruta | **+$1.000** | **+$700** | Coordinación en recorrido |
| **Retorno** | Vuelta con remito o cobro | **$2.200** | **$1.800** | Retorno formal en 24 hs |
| **Recargo por Lluvia** | Contingencia climática | Variable dinámico | Variable dinámico | Se informa en cotizador |

### 7.2. Horarios Operativos y Cortes
- **Envíos LowCost**: Horario de corte a las **13:00 hs** para entregas en el día hasta las 19:00 / 20:00 hs.
- **Mercado Envíos Flex**: Horario de corte a las **15:00 hs** para entregas en el mismo día antes de las 20:00 hs.
- **Envíos Express**: Despacho continuo en franja acordada de 2 a 3 horas con 2 horas de anticipación mínima.
- **Atención en Base Central**: Lunes a Viernes de 09:00 a 18:00 hs, Sábados de 10:00 a 15:00 hs.

---

## 8. Problemas de Higiene del Repositorio Local

1. **Directorio Corrupto en Raíz (`Drepositoriosccc`)**:
   - En el directorio raíz del proyecto existe una carpeta llamada `Drepositoriosccc` (con carácter de dos puntos codificado indebidamente). Se originó por una ejecución con rutas absolutas mal escapadas en Windows. Es una carpeta vacía que debe eliminarse.
2. **Archivos Redundantes en `envios/`**:
   - `html.html` es un duplicado residual sin minificar de `home.html`.
3. **Nombres de Archivos Inconsistentes en `envios/`**:
   - `nossobresobre-nosotros.html` contiene un error de duplicación en el prefijo.
   - La mezcla de nombres aplanados dificulta la correspondencia con las rutas canónicas del sitio en producción.

---

## 9. Matriz de Recomendaciones Accionables y Priorizadas

| Prioridad | Área / Archivo | Hallazgo / Inconsistencia | Acción Recomendada | Impacto |
| :---: | :--- | :--- | :--- | :---: |
| **CRÍTICA** | `envios/terminos-y-condiciones.html` | Archivo sobrescrito por duplicado de `logistica-dosruedas.html`. Texto legal perdido en local. | Extraer el HTML de `https://www.enviosdosruedas.com/terminos-y-condiciones/` y restaurar el archivo local con su contenido legítimo. | Evita contingencias legales y repara la integridad del repositorio. |
| **CRÍTICA** | `public/` y `envios/*.html` | Dependencia de 31 imágenes alojadas en un bucket externo de Supabase (`clone-assets`). 0 imágenes locales. | Descargar los assets desde producción (`/logo-envios-simplified.webp`, `/heroes/inicio-mapa.webp`, `/cards/...`), guardarlos en `public/` y reescribir las rutas relativas en los archivos HTML. | Independencia de infraestructura externa y resiliencia local. |
| **ALTA** | `envios/` | Faltan 3 páginas activas en producción: `/cobertura/`, `/guias/envios-flex-mar-del-plata/` y `/servicios/`. | Incorporar las 3 páginas faltantes al directorio `envios/` (`cobertura.html`, `guias-envios-flex.html`, `servicios.html`) para paridad 1:1. | Completitud del catálogo de páginas. |
| **ALTA** | Producción (`sitemap.xml`) | URLs sin barra final provocan 308 redirects obligatorios en cada visita de motores de búsqueda. | Actualizar el generador de `sitemap.xml` en Next.js para emitir URLs con trailing slash (`<loc>.../contacto/</loc>`). | Optimización de crawl budget y SEO técnico. |
| **ALTA** | Producción (`sitemap.xml`) | URLs fantasma `/servicios/plan-emprendedores` y `/servicios/envios-contrareembolso` que redirigen. | Eliminar ambas URLs obsoletas de `sitemap.xml` o reemplazar sus redirecciones por páginas canónicas activas. | Limpieza de indexación en Google Search Console. |
| **MEDIA** | Producción (`/servicios/envios-flex/`) | Error 404 en la versión con guion de Mercado Envíos Flex. | Configurar una redirección permanente `308` en `next.config.js` desde `/servicios/envios-flex/` hacia `/servicios/enviosflex/`. | Prevención de pérdida de tráfico y enlaces rotos. |
| **MEDIA** | `envios/html.html` | Archivo huérfano duplicado de la home (512 KB). | Eliminar de forma segura `envios/html.html` del repositorio. | Reducción de peso y limpieza del repositorio. |
| **MEDIA** | Raíz (`Drepositoriosccc`) | Carpeta vacía generada por error de path en Windows. | Eliminar el directorio `Drepositoriosccc`. | Higiene y limpieza del repositorio. |
| **BAJA** | `envios/*.html` | Presencia de 393-950 atributos `data-sd-id` y marcadores `bis_skin_checked`. | Ejecutar un script de limpieza sobre los HTML locales para remover atributos instrumentales de diseño y extensiones. | Calidad de código y legibilidad HTML. |
| **BAJA** | `envios/cotizar.html` y otros | Formularios y calculadora sin interactividad JS cliente. | Proveer un script JS ligero (vanilla JS) que implemente la lógica de cálculo de tarifas y apertura de WhatsApp para visualización estática independiente. | Funcionalidad completa en entornos locales. |

---

## 10. Conclusión del Relevamiento

El sitio web en producción `https://www.enviosdosruedas.com/` se encuentra en un estado operativo, seguro y de alto rendimiento técnico, aprovechando Next.js en Vercel con cabeceras de seguridad estrictas y un diseño visual coherente con la paleta canónica del proyecto (`#0950F6` y `#FFEC01`).

Sin embargo, **el repositorio local no refleja una copia fiel ni mantenible del código fuente de producción**, sino una colección de capturas estáticas exportadas mediante Superdesign que sufrieron corrupción de archivos (`terminos-y-condiciones.html`), omisión de rutas vivas (`/cobertura/`, `/guias/envios-flex-mar-del-plata/`, `/servicios/`) y una peligrosa dependencia de assets alojados en un bucket externo de Supabase (`clone-assets`). La ejecución de las recomendaciones priorizadas resolverá estas fallas estructurales y restablecerá la paridad técnica y documental completa.
