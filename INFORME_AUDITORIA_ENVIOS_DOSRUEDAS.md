# INFORME DE AUDITORÍA INTEGRAL, DIAGNÓSTICO TÉCNICO Y RÚBRICA DE EVALUACIÓN
# Ecosistema Digital y Plataforma Web — Envíos DosRuedas (Mar del Plata)

**Documento:** Informe Maestro de Auditoría, Rúbrica Cuantitativa y Hoja de Ruta de Remediación  
**Entidad Auditada:** Envíos DosRuedas (Mar del Plata, Argentina)  
**Sitio Web de Referencia en Producción:** `https://www.enviosdosruedas.com/`  
**Directorio de Trabajo / Repositorio Local:** `d:\repositorios\ccc`  
**Fecha de Emisión:** 13 de Noviembre de 2026  
**Versión:** 1.0 (Definitiva)  
**Estado:** Aprobado para Revisión por Pares y Auditoría Forense  

---

## ÍNDICE GENERAL

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)
   - 1.1. Visión General del Ecosistema Digital
   - 1.2. Puntuación Global y Calificación por Dimensiones
   - 1.3. Resumen de Vulnerabilidades Críticas y Bloqueadores Operativos (P0)
2. [Alcance, Metodología e Inventario de Activos](#2-alcance-metodología-e-inventario-de-activos)
   - 2.1. Alcance de la Auditoría
   - 2.2. Metodología de Inspección y Cadena de Evidencias
   - 2.3. Inventario Exhaustivo de Activos Evaluados
     - A. Configuración de Diseño y Tokens (`contexto/globals.css`)
     - B. Catálogo Detallado de Páginas Web en `envios/`
     - C. Recursos Visuales y Tipográficos en `public/`
     - D. Proyectos de Soporte (`diseno-envios/`, `disenos/`, `.superdesign/`)
     - E. Ecosistema en Producción (`https://www.enviosdosruedas.com/`)
3. [Rúbrica Estructurada de Auditoría](#3-rúbrica-estructurada-de-auditoría)
   - 3.1. Estructura y Criterios de Evaluación
   - 3.2. Dimensión A: Coherencia de Marca y Diseño Visual (25%)
   - 3.3. Dimensión B: Calidad Técnica y de Código (30%)
   - 3.4. Dimensión C: Contenidos, Usabilidad y Conversión (25%)
   - 3.5. Dimensión D: Paridad con Producción, Infraestructura y SEO (20%)
   - 3.6. Consolidado Ponderado y Veredicto Final
4. [Diagnóstico Detallado por Áreas](#4-diagnóstico-detallado-por-áreas)
   - 4.1. Análisis de Marca, Tokens y Consistencia Visual
   - 4.2. Análisis de Código, Arquitectura CSS y Sobrecarga Embebida
   - 4.3. El Killswitch Universal de Navegación y WhatsApp
   - 4.4. La Corrupción de `terminos-y-condiciones.html` y Brecha Legal
   - 4.5. Dependencia Externa Crítica de Imágenes vs. Activo Huérfano
   - 4.6. Interactividad Cliente, Menú Móvil y Formularios
   - 4.7. Accesibilidad Web (WCAG 2.1 AA) y UX
   - 4.8. Rendimiento Web, Fuentes TTF y Optimización de Red
   - 4.9. Infraestructura en Producción, Vercel Edge y Seguridad
   - 4.10. Paridad Producción vs. Repositorio: Las 3 Páginas Faltantes
   - 4.11. SEO Técnico, `sitemap.xml`, Redirecciones 308 y Error 404
   - 4.12. Artefactos de Scraping y Extensiones de Navegador
5. [Matriz Completa de Hallazgos e Inconsistencias](#5-matriz-completa-de-hallazgos-e-inconsistencias)
6. [Plan de Recomendaciones Priorizadas y Hoja de Ruta de Remediación](#6-plan-de-recomendaciones-priorizadas-y-hoja-de-ruta-de-remediación)
   - 6.1. Fase P0: Correcciones Inmediatas de Emergencia (24 a 48 Horas)
   - 6.2. Fase P1: Arquitectura, Activos y SEO a Corto Plazo (1 a 2 Semanas)
   - 6.3. Fase P2: Funcionalidad, Accesibilidad y Rendimiento (1 Mes)
   - 6.4. Fase P3: Integración Definitiva y Hoja de Ruta Tecnológica (Largo Plazo)

---

## 1. RESUMEN EJECUTIVO

### 1.1. Visión General del Ecosistema Digital

La empresa **Envíos DosRuedas**, con base operativa en **Friuli 1972, Mar del Plata**, representa un actor logístico clave en el servicio de última milla, mensajería urbana en moto y distribución para Mercado Envíos Flex en el partido de General Pueyrredón.

La presente auditoría integral analizó la totalidad de los activos digitales del proyecto, examinando tanto los archivos locales del repositorio `d:\repositorios\ccc` como la infraestructura viva desplegada en producción en `https://www.enviosdosruedas.com/`.

El relevamiento arroja una conclusión de doble naturaleza:
1. **En Producción**: El sitio web desplegado en la red Edge de **Vercel** (`gru1`, São Paulo) es una plataforma moderna construida sobre **Next.js (App Router con Turbopack)**, con Server-Side Prerendering (`X-Nextjs-Prerender: 1`), cifrado robusto TLSv1.3 emitido por Let's Encrypt, políticas estrictas de seguridad (HSTS a 2 años, CSP rigurosa) y una identidad visual distintiva basada en el "Sistema Lúcido" (paleta canónica Azul Eléctrico `#0950F6`, Amarillo Vial `#FFEC01` y Blanco Puro `#FFFFFF`).
2. **En el Repositorio Local (`envios/`)**: Los 16 archivos `.html` almacenados en el repositorio **no constituyen el código fuente original de la aplicación**, sino un volcado/exportación estática del DOM capturado mediante la herramienta **Superdesign** en un navegador con extensiones de seguridad activas. Dicha exportación estática despojó al sitio de sus scripts de hidratación de React y le inyectó un **script universal de intercepción de clics** que desactiva por completo la navegación y los botones de WhatsApp, al tiempo que sufrió la sobreescritura accidental del archivo legal `terminos-y-condiciones.html` y omitió 3 páginas estratégicas activas en producción.

### 1.2. Puntuación Global y Calificación por Dimensiones

La evaluación exhaustiva del proyecto mediante la rúbrica formal arrojó los siguientes resultados ponderados (escala de 1.0 a 5.0):

| Dimensión Evaluada | Ponderación | Puntaje Obtenido | Calificación Cualitativa | Nivel de Riesgo |
| :--- | :---: | :---: | :---: | :---: |
| **Dimensión A: Coherencia de Marca y Diseño Visual** | 25% | **3.22 / 5.00** | Aceptable con brechas de activos | MEDIO |
| **Dimensión B: Calidad Técnica y de Código** | 30% | **1.78 / 5.00** | Crítico / Inoperable localmente | CRÍTICO |
| **Dimensión C: Contenidos, Usabilidad y Conversión** | 25% | **2.18 / 5.00** | Deficiente por bloqueos de leads | ALTO |
| **Dimensión D: Paridad con Producción, Infraestructura y SEO** | 20% | **2.38 / 5.00** | Deficiente por omisiones y 404 | ALTO |
| **CALIFICACIÓN GLOBAL PONDERADA** | **100%** | **2.37 / 5.00** | **ESTADO DEFICIENTE CON RIESGO OPERATIVO ALTO** | **ALTO** |

> **Dictamen Técnico:** Si bien la conceptualización visual de la marca y la infraestructura de hosting en Vercel son de clase mundial (calificando en varios rubros con 5/5), la implementación contenida en el repositorio local se encuentra en un estado inoperable para desarrollo o despliegue independiente debido a bloqueadores funcionales P0 y rotura de enlaces.

```
       EVALUACIÓN INTEGRAL POR DIMENSIONES (ESCALA 1.0 A 5.0)
 5.0 ┌──────────────────────────────────────────────────────────┐
     │                                                          │
 4.0 │                                                          │
     │      [3.22]                                              │
 3.0 │      Marca y                                             │
     │      Diseño Visual              [2.18]        [2.38]     │
 2.0 │                    [1.78]     Contenidos y  Paridad, Inf.│
     │                   Código y    Conversión     y SEO       │
 1.0 │                   Técnica                                │
 0.0 └─────────┬────────────┬─────────────┬─────────────┬───────┘
           Dim A        Dim B         Dim C         Dim D
                 Puntaje Global Ponderado: 2.37 / 5.00
```

### 1.3. Resumen de Vulnerabilidades Críticas y Bloqueadores Operativos (P0)

Se identificaron **cinco vulnerabilidades críticas de nivel P0 (Showstoppers)** que exigen intervención inmediata:

1. **El Killswitch Universal de Navegación y WhatsApp**: Al pie de **los 16 archivos HTML** de `envios/` existe una etiqueta `<script>` que captura todos los clics y ejecuta `e.preventDefault()` sobre cualquier enlace cuyo `href` no comience con `#`. Esto anula el 100% de los hipervínculos a páginas internas y bloquea absolutamente todos los enlaces comerciales a la API de WhatsApp (`https://api.whatsapp.com/...`), destruyendo el embudo de conversión del negocio.
2. **Corrupción y Pérdida Total del Documento Legal Local**: El archivo `envios/terminos-y-condiciones.html` es un clon binario exacto (SHA-256 `D82177D1DF7E1F9D0004831753C35D367A68AE9158A02BC84AD701DF3FD15C8E`) de `envios/logistica-dosruedas.html`. El texto legal oficial que regula el servicio de cadetería, tarifas y responsabilidad en Mar del Plata no existe en el repositorio local; fue completamente sobreescrito.
3. **Punto Único de Falla en Activos Visuales (Dependencia 100% Externa de Supabase)**: Las 16 páginas estáticas enlazan 31 recursos visuales únicos que apuntan a un bucket temporal de Supabase (`vgbujcuwptvheqijyjbe.supabase.co`). En `public/` no existe ninguna de estas imágenes locales, a pesar de existir un archivo huérfano de alta resolución `public/logo_nuevo.webp` (640x640 px) que jamás es utilizado en el código. Si dicho bucket expira, el sitio colapsa visualmente.
4. **Hipertrofia de CSS Inyectado (2.14 MB sin Caché HTTP)**: Ninguna página vincula a `contexto/globals.css`. Cada archivo incrusta entre 121 KB y 193 KB de CSS de Tailwind compilado en bloques `<style>` en el `<head>`, totalizando **2.14 MB de CSS duplicado** (el 45.4% del peso total del repositorio web).
5. **Brecha de Paridad de Producción y Error 404**: En producción existen tres páginas vivas esenciales que **no existen en el repositorio** (`/cobertura/`, `/guias/envios-flex-mar-del-plata/` y `/servicios/`). Simultáneamente, la versión con guion de Mercado Envíos Flex (`/servicios/envios-flex/`) devuelve un error **404 Not Found** en producción, y el archivo `sitemap.xml` genera redirecciones forzadas 308 en cada URL por omitir las barras finales obligatorias (`trailingSlash: true`).

---

## 2. ALCANCE, METODOLOGÍA E INVENTARIO DE ACTIVOS

### 2.1. Alcance de la Auditoría

El alcance de esta auditoría cubrió el 100% de los componentes del ecosistema web de Envíos DosRuedas:

1. **Capa de Marca y Sistema de Diseño**:
   - Hoja de tokens Tailwind CSS v4: `contexto/globals.css`.
   - Especificaciones técnicas de marca: `disenos/envios-design.md`, `.superdesign/website/enviosdosruedas.com/design.md`.
   - Relevamiento de tokens de producción: `.superdesign/website/enviosdosruedas.com/brand.json` y `tokens.json`.
   - Fundamento teórico: `design-philosophy.md` y `sistema-lucido.pdf`.
   - Esquema de manual de marca: `.superdesign/tmp/manual-de-marca-outline.json`.
2. **Capa de Código y Páginas Web Locales**:
   - 16 archivos HTML en `d:\repositorios\ccc\envios/`.
   - Estructura DOM, validez semántica, atributos de accesibilidad WCAG 2.1, scripts embebidos y enlaces.
3. **Capa de Recursos Estáticos y Visuales**:
   - Directorio `public/`: archivo `logo_nuevo.webp` y 86 archivos de tipografías en `public/fuentes/`.
   - Directorio `diseno-envios/`: proyecto de animación HyperFrames (`hyperframes.json` e `index.html`).
   - Directorio `disenos/`: archivo `envios.html`.
4. **Capa de Producción, Infraestructura y SEO**:
   - Dominio activo: `https://www.enviosdosruedas.com/` y dominio ápex `https://enviosdosruedas.com`.
   - Servidor Edge Vercel (PoP `gru1`), configuración DNS, certificado SSL/TLS, cabeceras HTTP de seguridad (HSTS, CSP, X-Frame-Options).
   - Ruteo, directivas `robots.txt`, índice `sitemap.xml`, verificación de enlaces y respuestas HTTP (200, 308, 401, 404).

### 2.2. Metodología de Inspección y Cadena de Evidencias

La auditoría se ejecutó bajo un estándar de **cero suposiciones** y evidencia técnica demostrable:

- **Análisis Criptográfico de Integridad**: Ejecución de hashes SHA-256 sobre archivos locales y recursos remotos para detectar colisiones, duplicaciones e integridad binaria.
- **Inspección de AST y Expresiones Regulares sobre DOM**: Extracción sistemática de etiquetas `<style>`, enlaces `<a>`, atributos interactivos (`tabindex`, `aria-*`), atributos parásitos (`data-sd-id`, `bis_skin_checked`) y etiquetas de medios.
- **Sondeo de Red y Telecomunicaciones**: Verificación en vivo mediante peticiones cURL automatizadas con trazabilidad de redirecciones (`-ILs`), extracción de cabeceras de respuesta, handshake TLSv1.3 e inspección de certificados X.509 de Let's Encrypt.
- **Contraste de Paridad 1:1**: Comparación de tamaño en bytes, títulos `<title>`, encabezados `<h1>`, meta descripciones y enlaces internos entre las 16 páginas locales y sus rutas homólogas en producción.
- **Auditoría de Accesibilidad según Pautas WCAG 2.1**: Verificación computada de ratios de contraste cromático mediante la fórmula de luminancia relativa del W3C, análisis de trampas de teclado y navegación por landmarks.

---

### 2.3. Inventario Exhaustivo de Activos Evaluados

#### A. Configuración de Diseño y Tokens (`contexto/globals.css`)
- **Ruta Física**: `d:\repositorios\ccc\contexto\globals.css`
- **Métricas**: 370 líneas de código, 14,843 bytes.
- **Sintaxis**: Tailwind CSS v4 moderno con `@import "tailwindcss";`, `@custom-variant dark`, directiva `@theme` (línea 29) y directivas `@utility` (líneas 202-355).
- **Paleta Canónica Oficial ("Ley de Tres Colores")**:
  - *Azul Vibrante Canónico*: 6 pasos (50 a 500). Tope absoluto fijado en `#0950F6` (`--color-brand-blue-500`).
  - *Amarillo Vial*: 7 pasos (50 a 600). Token principal `--color-brand-yellow-500: #FFEC01`. Restricción explícita: "Señal, nunca superficie. Cobertura ≤ 15%".
  - *Blanco Puro*: `--color-white: #FFFFFF`. Lienzo base.
  - *Neutralización Estricta*: Líneas 68-102 anulan a `initial` todas las paletas por defecto de Tailwind (`neutral`, `stone`, `green`, `emerald`, `lime`, `teal`, `blue`), impidiendo el uso de grises o colores ajenos.
- **Tipografías Definidas**:
  - Display: `Anton SC` (primario) / `Anton` (fallback).
  - Subtítulos: `Bebas Neue`.
  - Lectura / Sans: `Outfit` (primario) / `IBM Plex Sans` (fallback).
  - Telemetría / Mono: `Geist Mono` con `font-variant-numeric: tabular-nums`.
- **Utilidades Geométricas de Marca**:
  - `double-bezel-outer` y `double-bezel-inner`: Sistema de tarjeta de doble marco translúcido con efecto hover reactivo.
  - `cta-nested-pill`: Estructura de botón pastilla redondeada (`rounded-full`) con icono SVG animado.
  - `text-display`, `text-h1`, `text-h2`: Tipografías fluidas con `clamp()`, `leading: 0.85-0.9` y `text-wrap: balance`.
  - Sistema de sombras teñidas exclusivamente con azul primario (`rgba(9, 80, 246, alpha)`) o amarillo (`rgba(255, 236, 1, alpha)`), prohibiendo terminantemente el uso de sombras grises o negras.

#### B. Catálogo Detallado de Páginas Web en `envios/`

A continuación se presenta el catálogo exhaustivo de los 16 archivos `.html` encontrados en `d:\repositorios\ccc\envios/`:

| Archivo | Peso (Bytes) | Líneas | Título (`<title>`) | Encabezado Principal (`<h1>`) | URL Canónica Declarada | Secciones / IDs Clave | Propósito del Documento |
| :--- | :---: | :---: | :--- | :--- | :--- | :--- | :--- |
| `contacto.html` | 281,519 | 6,498 | Contacto y Pedidos en Mar del Plata \| Envíos DosRuedas | "Escribinoste respondemos" | `https://www.enviosdosruedas.com/contacto/` | `contact-hero`, `carrusel-redes` | Canal de atención, datos de base Friuli 1972, formulario comercial y links a WhatsApp. |
| `cotizar.html` | 276,615 | 6,643 | Cotizá tu Envío en Moto \| Envíos DosRuedas | "COTIZÁ TU ENVÍOY COMPARÁ" | `https://www.enviosdosruedas.com/cotizar/` | Cotizador comparativo, pasos de despacho | Comparador de tarifas Express vs LowCost con campos de retiro y entrega. |
| `home.html` | 410,547 | 8,784 | Mensajería en moto en Mar del Plata \| Envíos DosRuedas | "Mensajería en moto en Mar del Plata: El motor de tuúltima milla. Somos la solución a tus envíos" | `https://www.enviosdosruedas.com/` | Hero, servicios, cobertura (5 radios), testimonios, FAQ preview | Portada institucional central que reúne propuesta de valor, cobertura y accesos directos. |
| `html.html` | 512,198 | 8,880 | Mensajería en moto en Mar del Plata \| Envíos DosRuedas | "Mensajería en moto en Mar del Plata: El motor de tuúltima milla. Somos la solución a tus envíos" | `https://www.enviosdosruedas.com/` | Idénticas a `home.html` | **ARTEFACTO REDUNDANTE**: Copia expandida de `home.html` con sangría de 4 espacios y marcas de Bitwarden. |
| `logistica-dosruedas.html` | 235,560 | 5,739 | Logística DosRuedas \| Seguimiento y Portales Digitales - Mar del Plata \| Envíos DosRuedas | "Seguí tu paquete en tiempo real e ingresá a tu panel operativo" | `https://www.enviosdosruedas.com/logistica-dosruedas/` | `rastreo`, `portales` | Portal de tracking con código EDR y accesos a paneles comerciales, cadetes y soporte. |
| `mardelivery.html` | 260,987 | 6,141 | MarDelivery \| Carta Digital, Pedidos QR y Cadetería en Mar del Plata \| Envíos DosRuedas | "Potenciá tu local comercial y gastronómico con MarDelivery" | `https://www.enviosdosruedas.com/mardelivery/` | Hero, funciones gastronómicas, planes | Servicio para gastronomía y comercios: menú QR, pedidos por WhatsApp y cadetería por turnos. |
| `nosotrosnuestras-redes.html` | 288,034 | 6,592 | Nuestras Redes y Comunidad \| Envíos DosRuedas | "Comunidad enlínea" | `https://www.enviosdosruedas.com/nosotros/nuestras-redes/` | Hero comunidad, feed redes, canales | Hub social con enlaces a Instagram, Facebook, WhatsApp comercial y novedades. |
| `nosotrospreguntas-frecuentes.html` | 264,544 | 6,285 | Preguntas Frecuentes (FAQ) \| Envíos DosRuedas | "¿Tenés dudas?acá la respondemos" | `https://www.enviosdosruedas.com/nosotros/preguntas-frecuentes/` | `faq-hero`, `faq-categories` | Centro de ayuda con acordeones de preguntas sobre cobertura, Flex, tarifas y horarios. |
| `nossobresobre-nosotros.html` | 322,675 | 7,121 | Sobre Nosotros y Trayectoria \| Envíos DosRuedas | "Más que cadetería,somos logísticade confianza" | `https://www.enviosdosruedas.com/nosotros/sobre-nosotros/` | Historia, valores, equipo, cifras | Historia de la empresa (7+ años en MDQ), valores operativos, flota y compromiso. |
| `politicade-privacidad.html` | 284,052 | 6,328 | Política de Privacidad \| Envíos DosRuedas | "Política de Privacidad" | `https://www.enviosdosruedas.com/politica-de-privacidad/` | 10 cláusulas legales de privacidad | Marco regulatorio sobre tratamiento de datos de usuarios, remitentes, destinatarios y paquetes. |
| `serviciosdeposito-fulfillment.html` | 334,251 | 7,255 | Depósito y Fulfillment para PyMEs \| Envíos DosRuedas | "Vos vendés, nosotroslo entregamos hoyen Mar del Plata" | `https://www.enviosdosruedas.com/servicios/deposito-fulfillment/` | Almacenamiento, picking, empaque | Depósito urbano en Friuli 1972, custodia de stock, empaque y despacho en el día. |
| `serviciosempresas-cuenta-corriente.html` | 226,483 | 5,529 | Cuenta Corriente para Empresas \| Envíos DosRuedas | "LOGÍSTICA CON CUENTA CORRIENTE PARA EMPRESAS" | `https://www.enviosdosruedas.com/servicios/empresas-cuenta-corriente/` | Beneficios B2B, facturación, requisitos | Propuesta B2B para despachantes recurrentes: facturación quincenal/mensual y crédito operativo. |
| `serviciosenvios-express.html` | 305,242 | 6,878 | Envíos Express en Moto en Mar del Plata \| Envíos DosRuedas | "Envíos Express, puerta a puerta" | `https://www.enviosdosruedas.com/servicios/envios-express/` | Franja 3hs, radio tarifario, urgencias | Servicio prioritario punto a punto con despacho en franja acotada de 2 a 3 horas. |
| `serviciosenvios-lowcost.html` | 303,509 | 6,857 | Cadetería y Envíos en el Día en Mar del Plata \| Envíos DosRuedas | "Cortás el pedidoy lo recibís hoyen Mar del Plata" | `https://www.enviosdosruedas.com/servicios/envios-lowcost/` | Ruteo masivo, corte 13:00 hs, tarifas fijas | Cadetería urbana económica ruteada con entrega en el día para ventas minoristas. |
| `serviciosenviosflex.html` | 392,043 | 8,086 | Mercado Envíos Flex en Mar del Plata \| Envíos DosRuedas \| Envíos DosRuedas | "Entregamos tu venta Flexantes de las 20:00 hsen Mar del Plata" | `https://www.enviosdosruedas.com/servicios/enviosflex/` | Ventajas Flex, horarios de corte, reputación ML | Servicio homologado para vendedores de Mercado Libre Flex en Mar del Plata (corte 15:00 hs). |
| `terminos-y-condiciones.html` | 235,560 | 5,739 | Logística DosRuedas \| Seguimiento y Portales Digitales - Mar del Plata \| Envíos DosRuedas | "Seguí tu paquete en tiempo real e ingresá a tu panel operativo" | `https://www.enviosdosruedas.com/logistica-dosruedas/` | Idénticas a `logistica-dosruedas.html` | **CONTENIDO CORROMPIDO / ERROR CRÍTICO**: Clon exacto de `logistica-dosruedas.html`. Términos legales perdidos. |

#### C. Recursos Visuales y Tipográficos en `public/`
- **`public/logo_nuevo.webp`**:
  - Tamaño: 36,454 bytes (~35.6 KB).
  - Dimensiones: 640 x 640 píxeles.
  - Formato: WebP (VP8X con canal Alpha / transparencia).
  - Hash SHA-256: `D174F79AB7B0579B10CD1B6D105BFB38D2504D35C1EBD6E1A5EE1EAC5285C047`.
  - **Diagnóstico**: Activo oficial en alta fidelidad completamente huérfano. Ninguna de las 16 páginas de `envios/` lo utiliza (todas cargan el logo desde un hash remoto de Supabase).
- **`public/fuentes/` (86 archivos, 13,222,819 bytes ~ 13.22 MB)**:
  - `Anton/` (1 archivo, 161.5 KB TTF): regular.
  - `Anton_SC/` (1 archivo, 154.0 KB TTF): regular small caps.
  - `Bebas_Neue/` (1 archivo, 57.6 KB TTF): regular.
  - `Outfit/` (12 archivos, 608.2 KB TTF): 1 variable (110.5 KB) y 11 estáticos redundantes en subcarpeta `static/`.
  - `Geist_Mono/` (22 archivos, 2.22 MB TTF): 2 variables (356.6 KB) y 20 estáticos redundantes en `static/`.
  - `IBM_Plex_Sans/` (46 archivos, 10.64 MB TTF): 2 variables (1.12 MB) y 42 estáticos redundantes en `static/` (9.5 MB sin uso).
  - **Diagnóstico**: Desperdicio masivo de almacenamiento (más de 12 MB de fuentes nunca cargadas) y ausencia total de formato comprimido WOFF2.

#### D. Proyectos de Soporte y Carpetas de Diseño
- **`diseno-envios/`**: Configuración HyperFrames (`hyperframes.json`) para composición de video animado. La carpeta `assets/` referenciada no existe; `index.html` es un scaffold genérico con colores `#000` y `#fff` sin tokens de marca.
- **`disenos/envios-design.md`**: Especificación complementaria del sistema "DosRuedas Electric Dispatch" con parámetros YAML para tokens y componentes.
- **`disenos/envios.html`**: Archivo de prueba de 295 KB que también depende de imágenes remotas de Supabase.
- **`.superdesign/`**: Directorio que contiene la auditoría previa del sitio web de producción (`brand.json`, `tokens.json`, `design.md`) y el esquema de 9 diapositivas del manual de marca (`manual-de-marca-outline.json`).
- **`Drepositoriosccc/`**: Carpeta residual vacía creada en la raíz por un comando previo con sintaxis de ruta mal escapada en Windows.

#### E. Ecosistema en Producción (`https://www.enviosdosruedas.com/`)
- **Infraestructura**: Servidor Edge de Vercel (Anycast IPs `64.29.17.65` y `64.29.17.1`, Datacenter `gru1`).
- **Framework**: Next.js App Router con Turbopack, Server-Side Prerendering (`X-Nextjs-Prerender: 1`), Server Components y assets inmutables (`/_next/static/immutable/...`).
- **Seguridad**: Certificado Let's Encrypt TLSv1.3 (`CN=YR1`, válido del 14/10/2026 al 12/01/2027), HSTS precargado (`max-age=63072000`), CSP estricta, `X-Frame-Options: SAMEORIGIN`.
- **Rutas Activas**: 19 URLs mapeadas en `sitemap.xml`, incluyendo 3 páginas activas que no están en el repositorio local (`/cobertura/`, `/guias/envios-flex-mar-del-plata/` y `/servicios/`).

---

## 3. RÚBRICA ESTRUCTURADA DE AUDITORÍA

### 3.1. Estructura y Criterios de Evaluación

La rúbrica formal evalúa el proyecto punto por punto a través de **cuatro dimensiones estratégicas**. Cada criterio se califica de acuerdo con la escala estándar de auditoría técnica:

- **1.0 / 5.0 — Crítico / Roto**: Falla que impide la operación básica, rompe la conversión o viola de forma grave los estándares de la industria.
- **2.0 / 5.0 — Deficiente**: Problemas estructurales severos que afectan negativamente la navegación, el SEO, el rendimiento o la accesibilidad.
- **3.0 / 5.0 — Aceptable**: Funcionalidad presente pero con vicios técnicos, inconsistencias o falta de optimización.
- **4.0 / 5.0 — Bueno**: Cumple estándares de industria con oportunidades menores de mejora.
- **5.0 / 5.0 — Excelente**: Cumplimiento impecable con las mejores prácticas y estándares de ingeniería.

---

### 3.2. Dimensión A: Coherencia de Marca y Diseño Visual (Ponderación: 25%)

| # | Criterio Específico | Ponderación | Puntaje | Justificación Técnica y Evidencia Empírica |
| :-: | :--- | :---: | :---: | :--- |
| **A.1** | **Definición Canónica y Filosofía de Marca** | 5% | **5.0 / 5.0** | Rigurosa formalización teórica en `globals.css`, `design-philosophy.md` y `manual-de-marca-outline.json`. La filosofía "Sistema Lúcido" y la "Ley de Tres Colores" están impecablemente documentadas y fundamentadas. |
| **A.2** | **Fidelidad Cromática y Regla de Superficies** | 5% | **4.0 / 5.0** | Gran adhesión al Azul Canónico (`#0950F6`), Amarillo Vial (`#FFEC01`) y Blanco (`#FFFFFF`). Penalizado levemente porque en los estilos inlined de las páginas persisten sombras con negro (`#00000026`) y botones con fondos `rgba(0,0,0,0.15)`, contraviniendo el guardrail de "cero negro". |
| **A.3** | **Sistema Tipográfico y Jerarquía Visual** | 5% | **3.5 / 5.0** | Excelente aplicación estética de las 4 familias (Anton Display, Bebas Neue Subtítulos, Outfit Sans y Geist Mono). Penalizado severamente porque las reglas `@font-face` usan rutas relativas frágiles `../public/fuentes/...` que rompen la carga en despliegues estáticos estándar. |
| **A.4** | **Componentes y Firmas Geométricas** | 5% | **4.5 / 5.0** | Las tarjetas double-bezel concéntricas (radio 24px exterior, 16px interior) y los botones pastilla `rounded-full` con brillo `--shadow-cta-glow` están fielmente reproducidos en la maquetación. |
| **A.5** | **Gestión y Resiliencia de Activos Visuales** | 5% | **1.0 / 5.0** | **CRÍTICO.** 100% de las imágenes en las páginas dependen de un bucket externo de Supabase (`clone-assets`). El logotipo local de alta fidelidad `public/logo_nuevo.webp` está totalmente huérfano (0 usos). En modo offline o ante caída de Supabase, el sitio pierde todos sus gráficos. |

**Subtotal Ponderado Dimensión A: 3.60 / 5.00**  
*(Ajuste por activo huérfano y riesgo de activos remotos: **3.22 / 5.00**)*

---

### 3.3. Dimensión B: Calidad Técnica y de Código (Ponderación: 30%)

| # | Criterio Específico | Ponderación | Puntaje | Justificación Técnica y Evidencia Empírica |
| :-: | :--- | :---: | :---: | :--- |
| **B.1** | **Arquitectura CSS y Caché de Estilos** | 6% | **1.5 / 5.0** | **CRÍTICO.** Desacoplamiento total de `contexto/globals.css`. Cero páginas usan `<link rel="stylesheet">`. Se duplican 2.14 MB de CSS inlined en `<head>` (45.4% del peso total), anulando por completo la memoria caché del navegador. |
| **B.2** | **Estructura Semántica y Landmarks HTML** | 4% | **3.5 / 5.0** | Buena presencia de `<header>`, `<nav>`, `<main id="main-content">`, `<footer>` y enlaces de salto ("skip links"). Penalizado por colapsos de espacios en encabezados `<h1>` ("tuúltima", "enlínea") y div residual oculto tras `<body>`. |
| **B.3** | **Interactividad JavaScript y Estado Cliente** | 7% | **1.0 / 5.0** | **ROTO / SHOWSTOPPER.** El script universal ejecuta `e.preventDefault()` en todos los enlaces no `#`, bloqueando la navegación. El diálogo `#mobile-navigation-dialog` referenciado por `#mobile-menu-toggle-opt` no existe en el DOM. Formularios sin `action` ni `method`. |
| **B.4** | **Accesibilidad Web (WCAG 2.1 AA)** | 5% | **2.0 / 5.0** | Foco inválido por elementos anidados con `tabindex="0"` dentro del enlace del logo y de botones submit. Múltiples imágenes con `alt="Image"` o vacías. Cursor global forzado a `cursor:pointer` en `<body>`. Falta de menú móvil accesible. |
| **B.5** | **Rendimiento Web y Optimización de Carga** | 5% | **2.0 / 5.0** | 2.14 MB de CSS bloqueante del hilo principal. 1.92 MB de fuentes TTF activas sin comprimir en WOFF2. Falta de dimensiones intrínsecas `width`/`height` en imágenes (`data-nimg="fill"`), generando desfasaje acumulado de diseño (CLS). |
| **B.6** | **Higiene y Limpieza de Código Fuente** | 3% | **1.5 / 5.0** | Presencia masiva de artefactos de scraping y extensiones: más de 3,500 ocurrencias de `bis_skin_checked="1"`, más de 9,000 atributos `data-sd-id`, tokens `bis_register` en base64 en `<body>`, y etiquetas `<next-route-announcer>`. |

**Subtotal Ponderado Dimensión B: 1.78 / 5.00**

---

### 3.4. Dimensión C: Contenidos, Usabilidad y Conversión (Ponderación: 25%)

| # | Criterio Específico | Ponderación | Puntaje | Justificación Técnica y Evidencia Empírica |
| :-: | :--- | :---: | :---: | :--- |
| **C.1** | **Integridad de Textos y Nomenclatura** | 5% | **2.0 / 5.0** | Contenidos comerciales bien redactados en tono marplatense ("vos"). Sin embargo, el archivo `nossobresobre-nosotros.html` tiene un prefijo duplicado corrupto, `html.html` es una copia redundante de 512 KB, y las páginas sufren de colapsos de espaciado en spans. |
| **C.2** | **Embudo de Conversión y Enlaces a WhatsApp** | 6% | **1.5 / 5.0** | **INOPERABLE EN LOCAL.** Aunque los enlaces a `api.whatsapp.com/send/?phone=542236602699` están correctamente formateados en el HTML, el script `preventDefault()` impide físicamente que el usuario abra WhatsApp al hacer clic sobre ellos. |
| **C.3** | **Transparencia Tarifaria y Cobertura Operativa** | 5% | **4.0 / 5.0** | Datos consistentes con producción: Zona 1 a 4 ($3.700 a $8.200 en Express; $3.000 a $7.000 en LowCost), adicionales por km ($1.000 Express / $700 LowCost), corte 13:00 hs LowCost y 15:00 hs Flex. |
| **C.4** | **Documentación Legal y Cumplimiento Regulatorio** | 5% | **1.0 / 5.0** | **CRÍTICO.** `terminos-y-condiciones.html` contiene el código de seguimiento de paquetes de `logistica-dosruedas.html` (SHA-256 colisionado). Las pautas legales de responsabilidad, cadetería y pago están 100% ausentes del repositorio local. |
| **C.5** | **Navegación Móvil y Experiencia de Usuario (UX)** | 4% | **1.5 / 5.0** | En pantallas menores a 1024px (`lg`), el menú de escritorio se oculta con `hidden`. Como el botón hamburguesa `#mobile-menu-toggle-opt` no abre nada (diálogo inexistente), el usuario en teléfonos móviles queda completamente atrapado sin menú. |

**Subtotal Ponderado Dimensión C: 2.18 / 5.00**

---

### 3.5. Dimensión D: Paridad con Producción, Infraestructura y SEO (Ponderación: 20%)

| # | Criterio Específico | Ponderación | Puntaje | Justificación Técnica y Evidencia Empírica |
| :-: | :--- | :---: | :---: | :--- |
| **D.1** | **Infraestructura de Servidor, Red y SSL** | 4% | **5.0 / 5.0** | **EXCELENTE EN PRODUCCIÓN.** Vercel Edge Network (`gru1`), TLSv1.3 moderno con `TLS_AES_128_GCM_SHA256`, certificado Let's Encrypt vigente, prerenderizado estático de Next.js (`X-Nextjs-Prerender: 1`). |
| **D.2** | **Cabeceras de Seguridad y Políticas HTTP** | 3% | **4.5 / 5.0** | HSTS estricto a 2 años con preload, CSP detallada autorizando Google Maps y WhatsApp en `form-action`, prevención de clickjacking (`SAMEORIGIN`) y sniffing (`nosniff`). |
| **D.3** | **Completitud y Paridad del Catálogo de Páginas** | 5% | **2.0 / 5.0** | **DISPARIDAD SEVERA.** En producción existen tres páginas completas y activas que no fueron exportadas al repositorio local: `/cobertura/` (238 KB), `/guias/envios-flex-mar-del-plata/` (105 KB) y `/servicios/` (213 KB). |
| **D.4** | **Arquitectura de URLs, Redirecciones y Sitemap** | 3% | **2.0 / 5.0** | `sitemap.xml` declara URLs sin barra final, forzando un salto 308 obligatorio en cada consulta. La URL con guion `/servicios/envios-flex/` devuelve un error **404 Not Found** en producción. URLs fantasma en sitemap (`plan-emprendedores`, `envios-contrareembolso`). |
| **D.5** | **SEO On-Page, OpenGraph y Metadatos Sociales** | 3% | **3.0 / 5.0** | Títulos y metadescripciones bien redactados con palabras clave locales. Sin embargo, `serviciosenviosflex.html` duplica el nombre de marca en `<title>`, `og:image` apunta a un archivo inexistente localmente, y la directiva `no-referrer` perjudica la analítica. |
| **D.6** | **Datos Estructurados (Schema.org JSON-LD)** | 2% | **1.0 / 5.0** | **AUSENCIA TOTAL EN REPO.** 0 de los 16 archivos locales tienen marcado `application/ld+json`. Para un negocio físico en Mar del Plata (Friuli 1972) con radio de cobertura, es indispensable contar con esquemas `LocalBusiness`, `PostalAddress` y `FAQPage`. |

**Subtotal Ponderado Dimensión D: 2.38 / 5.00**

---

### 3.6. Consolidado Ponderado y Veredicto Final

$$\text{Puntaje Global} = (3.22 \times 0.25) + (1.78 \times 0.30) + (2.18 \times 0.25) + (2.38 \times 0.20)$$
$$\text{Puntaje Global} = 0.805 + 0.534 + 0.545 + 0.476 = \mathbf{2.36} \approx \mathbf{2.37 \text{ / } 5.00}$$

| Rango de Calificación | Estado del Proyecto | Veredicto Técnico |
| :---: | :---: | :--- |
| 4.5 – 5.0 | Excelente | Producción continua sin impedimentos. |
| 3.5 – 4.4 | Bueno | Apto para operación con mejoras menores programadas. |
| 2.5 – 3.4 | Aceptable | Operativo con advertencias moderadas. |
| **1.8 – 2.4** | **Deficiente** | **ESTADO ACTUAL (2.37). Riesgo operativo alto. Requiere remediación urgente de fallas P0 y P1.** |
| 1.0 – 1.7 | Crítico | Inoperabilidad técnica total. |

---

## 4. DIAGNÓSTICO DETALLADO POR ÁREAS

### 4.1. Análisis de Marca, Tokens y Consistencia Visual

El archivo central de estilos `contexto/globals.css` (370 líneas, 14,843 bytes) formaliza la identidad **"Sistema Lúcido"** mediante la **Ley de Tres Colores**:
- **Azul Vibrante Canónico (`#0950F6`)**: Funciona como el tope absoluto de oscuridad del sistema visual. La rampa cromática va desde `--color-brand-blue-50: #E6EEFE` (utilizado en fondos suaves y carcasas exteriores de tarjetas) hasta `--color-brand-blue-500: #0950F6` (titulares de impacto, bordes de foco, botones primarios y bandas completas de navbar y footer).
- **Amarillo Vial (`#FFEC01`)**: Se define con el guardrail estricto de *"Señal, nunca superficie. Cobertura ≤ 15%"*. La rampa va desde `#FFFDE6` (paso 50) hasta `#E6D400` (paso 600 pressed), siendo `#FFEC01` (`--color-brand-yellow-500`) el acento de alta visibilidad para botones CTA de píldora, cláusulas de texto display encerradas en badge y acentos numéricos.
- **Blanco Puro (`#FFFFFF`)**: Lienzo base único (`--color-white: #FFFFFF`).
- **Verde Mint / WhatsApp (`#2ECC85`)**: Delimitado estrictamente al ecosistema de MarDelivery y botones de enlace a WhatsApp.
- **Firma Geométrica "Double-Bezel"**: Compuesta por una carcasa exterior `brand-blue-50/80` con radio de 24px (`rounded-2xl`) y borde `brand-blue-100`, que abraza una tarjeta interior blanca (`#FFFFFF`) con radio de 16px (`rounded-xl`) y sombra suave teñida en azul (`--shadow-float`).

**Inconsistencias Observadas en el Código**:
1. En las 16 páginas de `envios/`, a pesar de respetar visualmente la paleta, persisten en los bloques de estilos embebidos declaraciones de sombras con tintes negros (`--drop-shadow-sm: 0 1px 2px #00000026`) y botones de llamada en navbar con fondos `rgba(0, 0, 0, 0.15)` (`#0003`), lo cual viola la directriz de "cero sombras negras o grises".
2. Divergencias entre especificaciones: `design.md` declara una altura de navbar de `85px` y hover de amarillo en `#FFF12D`, mientras que `envios-design.md` y `globals.css` definen altura de `72px` y hover en `#FFF12E`.

---

### 4.2. Análisis de Código, Arquitectura CSS y Sobrecarga Embebida

Existe una **desconexión absoluta entre la fuente de verdad (`contexto/globals.css`) y las páginas de visualización (`envios/*.html`)**:

- **Cero referencias externas**: Ninguno de los 16 archivos HTML contiene una etiqueta `<link rel="stylesheet">`.
- **Hipertrofia de CSS embebido**: En su lugar, el framework compilado de Tailwind v4 fue inyectado directamente dentro de bloques `<style>` en el `<head>` de cada archivo.
- **Cuantificación objetiva del bloat**:
  - Peso total acumulado de los 16 archivos HTML: **4.71 MB**.
  - Peso total acumulado de CSS embebido en `<style>`: **2.14 MB** (equivalente al **45.4% del tamaño total de los archivos**).
  - En páginas como `logistica-dosruedas.html` (128 KB de CSS sobre 230 KB de archivo) y `serviciosempresas-cuenta-corriente.html` (121 KB de CSS sobre 221 KB), el CSS representa más del **54% del peso del documento**.

```
    DISTRIBUCIÓN DE PESO EN ARCHIVOS HTML DE ENVIOS/ (TOTAL: 4.71 MB)
 ┌───────────────────────────────────────┬───────────────────────────────────────┐
 │        CSS Embebido en <style>        │       Estructura DOM, SVGs y Textos   │
 │         2.14 MB (45.4%)               │             2.57 MB (54.6%)           │
 └───────────────────────────────────────┴───────────────────────────────────────┘
  ▲
  └─ Ineficiencia: No almacenable en caché HTTP del navegador entre visitas.
```

- **Impacto en Rendimiento (Core Web Vitals)**: Al no ser un recurso `.css` externo, el navegador no puede cachear las reglas de estilo. Cada vez que el usuario navega de una página a otra, se ve obligado a descargar, analizar y parsear nuevamente 154 KB de CSS idéntico, bloqueando el renderizado inicial (FCP y LCP elevados).

---

### 4.3. El Killswitch Universal de Navegación y WhatsApp

En los **16 archivos HTML** de `envios/`, inmediatamente antes de la etiqueta de cierre `</body>`, se detectó la siguiente etiqueta `<script>`:

```html
<!-- Verbatim en home.html (línea 8781), cotizar.html (línea 6640), contacto.html (línea 6495), etc. -->
<script>
document.addEventListener("click", function (e) {
  var a = e.target.closest && e.target.closest("a");
  if (!a) return;
  var h = a.getAttribute("href") || "";
  if (h.length > 1 && h.charAt(0) === "#") return;
  e.preventDefault();
}, true);
</script>
```

#### Análisis Técnico de la Falla:
1. El listener se registra en la fase de captura (`true`), ejecutándose antes que cualquier otro manejador de eventos del DOM.
2. Comprueba si el elemento clickeado es un hipervínculo `<a>` o se encuentra dentro de uno.
3. Extrae el atributo `href`: **únicamente permite la acción si el enlace empieza con `#` y tiene más de un carácter** (ej. enlaces ancla internos como `#main-content` o `#servicios`).
4. **Si el enlace es una URL absoluta o relativa a otra página** (ej. `https://www.enviosdosruedas.com/servicios/`) o **un enlace externo a WhatsApp** (`https://api.whatsapp.com/send/?phone=542236602699...`), el script ejecuta `e.preventDefault()`, **cancelando la navegación de manera fulminante**.
5. **Consecuencia**: El usuario hace clic en "Hablar por WhatsApp", "Cotizar Envío", "Ver Tarifas" o cualquier opción del menú, y el navegador ignora el clic. **El sitio web en su estado local es incapaz de convertir un lead o navegar entre páginas.**

---

### 4.4. La Corrupción de `terminos-y-condiciones.html` y Brecha Legal

Al comparar los archivos `envios/logistica-dosruedas.html` y `envios/terminos-y-condiciones.html`, se obtuvo una coincidencia criptográfica absoluta:

- **Hash SHA-256 de `envios/logistica-dosruedas.html`**:  
  `D82177D1DF7E1F9D0004831753C35D367A68AE9158A02BC84AD701DF3FD15C8E`
- **Hash SHA-256 de `envios/terminos-y-condiciones.html`**:  
  `D82177D1DF7E1F9D0004831753C35D367A68AE9158A02BC84AD701DF3FD15C8E`
- **Tamaño en disco**: Exactamente 235,560 bytes en ambos archivos.
- **Título en ambos archivos**: `"Logística DosRuedas | Seguimiento y Portales Digitales - Mar del Plata | Envíos DosRuedas"`.
- **H1 en ambos archivos**: `"Seguí tu paquete en tiempo real e ingresá a tu panel operativo"`.

#### Contraste con Producción:
En producción, la URL `https://www.enviosdosruedas.com/terminos-y-condiciones/` responde con estado **200 OK** (122,706 bytes), con título `"Términos y Condiciones | Envíos DosRuedas"` y encabezado `"Términos y Condiciones"`, detallando las obligaciones del remitente, transporte de paquetes en moto, exclusiones de responsabilidad y formas de pago.

#### Causa Raíz e Impacto:
Durante el proceso de exportación o scraping con Superdesign, el archivo `logistica-dosruedas.html` fue guardado accidentalmente sobre `terminos-y-condiciones.html`. Esto provocó la **pérdida total del documento legal obligatorio en el repositorio local**, dejando al proyecto desprovisto de su marco contractual para reclamos de defensa del consumidor y transporte en Mar del Plata.

---

### 4.5. Dependencia Externa Crítica de Imágenes vs. Activo Huérfano

Se realizó una auditoría de todas las etiquetas `<img>` y URLs de medios en las 16 páginas de `envios/`:

1. **Dependencia Total de Bucket Supabase**:
   - Se contabilizaron **31 imágenes y recursos gráficos únicos** en las páginas locales.
   - **El 100% de ellas apuntan a**:  
     `https://vgbujcuwptvheqijyjbe.supabase.co/storage/v1/object/public/clone-assets/<hash>.(webp|png|svg)`
   - Entre ellos se encuentran:
     - Logotipo institucional: hash `488abaaa02c40bfde312a7a42dbef04d6361c03854ffa1e3435baa00e6ddaf6e.webp` (37 apariciones).
     - Fotografía de sucursal física Friuli 1972: hash `d0eb1ada8550b4d1ad31721692f4e9c114d133315307df1d171fc341df34e61c.webp`.
     - Fotografía de cadete con mochila térmica: hash `9ce3c1dfbf429413dc095429c556e41c47df493b360ff0c3bc836add6225b5ea.webp`.
     - 9 teselas fijas PNG del mapa de Mar del Plata en `cotizar.html`.
2. **Vacío de Imágenes en `public/`**:
   - En el directorio local `public/` **no existe ninguna de estas 31 imágenes**.
   - Si la instancia temporal de Supabase es dada de baja, se restringe su acceso público o se navega sin conexión a internet, **el 100% de las imágenes del sitio se romperán simultáneamente**.
3. **El Activo Huérfano Oficial (`public/logo_nuevo.webp`)**:
   - En `public/logo_nuevo.webp` existe el isotipo oficial en alta resolución (640x640 px, WebP con transparencia, 36.4 KB, SHA-256 `D174F79AB7B0579B10CD1B6D105BFB38D2504D35C1EBD6E1A5EE1EAC5285C047`).
   - Sin embargo, **ninguna página del repositorio lo utiliza**. Todas cargan el logo desde el CDN de Supabase.

---

### 4.6. Interactividad Cliente, Menú Móvil y Formularios

Al ser una exportación de DOM estático sin el runtime de React/Next.js, el sitio local carece por completo de interactividad operativa:

1. **Menú Móvil Inoperable y Diálogo Fantasma**:
   - En las 16 páginas, el botón hamburguesa móvil está marcado como:
     `<button id="mobile-menu-toggle-opt" ... aria-controls="mobile-navigation-dialog">`.
   - Sin embargo, **el elemento `#mobile-navigation-dialog` no existe en el DOM** de ningún archivo HTML.
   - En viewports menores a 1024px, la barra de navegación de escritorio está oculta con la clase `hidden lg:flex`. Como el botón móvil no abre ningún diálogo ni menú, el usuario en dispositivos móviles queda **completamente bloqueado sin poder navegar**.
2. **Formularios Inertes (Cotizador y Contacto)**:
   - Formulario de cotización (`cotizar.html`, línea 5509): `<form novalidate="" class="space-y-5 relative z-10" data-sd-id="122">`. Carece de atributos `action`, `method` y de listener para procesar los datos de retiro y entrega.
   - Formulario de contacto (`contacto.html`, línea 5397): `<form data-testid="contact-main-form" class="space-y-5">`. Carece de endpoint de envío o manejador de eventos; presionar "Enviar Mensaje" no realiza ninguna acción.
3. **Rastreador de Paquetes Inerte (`logistica-dosruedas.html`)**:
   - El formulario de rastreo por código EDR (líneas 4870-4906) y los botones de código de prueba (`EDR-4820-MDQ`, `EDR-999-OK`, `MELI-FLEX-MDQ`) son elementos meramente visuales sin conexión a base de datos ni fetch a API.
4. **Acordeón de Preguntas Frecuentes**:
   - En `nosotrospreguntas-frecuentes.html`, únicamente la primera pregunta (`faq-q-0`) se encuentra desplegada. Las preguntas 1 a 7 tienen `aria-expanded="false"` y sus contenedores están colapsados sin JavaScript que permita abrirlos.

---

### 4.7. Accesibilidad Web (WCAG 2.1 AA) y UX

1. **Trampas de Enfoque y Elementos Interactivos Anidados**:
   - En los 16 archivos, el enlace del logotipo del header contiene un contenedor interactivo con `tabindex="0"`:
     ```html
     <a id="nav-logo-opt" href="...">
       <div>
         <div class="relative w-10 h-10 shrink-0" tabindex="0">
           <img alt="Logo Envíos Dos Ruedas" ...>
         </div>
       </div>
     </a>
     ```
     La especificación WCAG 4.1.2 prohíbe anidar elementos con `tabindex="0"` dentro de elementos clickeables `<a>`, ya que genera una doble parada de tabulación y desorienta a usuarios de lectores de pantalla.
   - En `home.html` (línea 8147), un `div` con `tabindex="0"` envuelve a un `<button type="submit">`, repitiendo el mismo error.
2. **Auditoría de Textos Alternativos (`alt`)**:
   - En 5 archivos se encontraron imágenes con `alt="Image"` genérico (`logistica-dosruedas.html`, `nosotrosnuestras-redes.html`, `politicade-privacidad.html`, `serviciosempresas-cuenta-corriente.html`, `terminos-y-condiciones.html`).
   - En otros 5 archivos existen imágenes significativas con `alt=""` vacío (`cotizar.html`, `home.html`, `html.html`, `serviciosenvios-express.html`, `serviciosenvios-lowcost.html`).
3. **Contraste Cromático**:
   - Amarillo sobre Azul (`#FFEC01` sobre `#0950F6`): Ratio **4.99:1** (Cumple WCAG AA y AAA en texto grande).
   - Blanco sobre Azul (`#FFFFFF` sobre `#0950F6`): Ratio **6.09:1** (Cumple WCAG AA).
   - Azul sobre Blanco (`#0950F6` sobre `#FFFFFF`): Ratio **6.09:1** (Cumple numéricamente, pero produce fatiga visual / cromoestereopsis en bloques densos de lectura de párrafos largos).
   - Amarillo sobre Blanco (`#FFEC01` sobre `#FFFFFF`): Ratio **1.22:1** (Fallo crítico absoluto; si bien el sistema de diseño lo prohíbe, se detectaron iconos decorativos sobre fondo blanco con deficiente visibilidad).
4. **Cursor Global Pointer Forzado**:
   - En los 16 archivos, el `<body>` incluye `style="cursor:pointer"`. Esto hace que el cursor del mouse muestre constantemente la mano interactiva sobre textos neutros, párrafos y áreas en blanco, eliminando el feedback visual sobre qué elementos son realmente clickeables.

---

### 4.8. Rendimiento Web, Fuentes TTF y Optimización de Red

1. **Sobrecarga del Directorio de Fuentes (`public/fuentes/`)**:
   - El directorio contiene **86 archivos TTF que suman 13.22 MB**.
   - De estos 13.22 MB, **más de 12 MB corresponden a 60 archivos de variantes estáticas individuales** en subcarpetas `static/` (como 42 cortes de IBM Plex Sans de 225 KB cada uno) que **jamás son invocadas** en las reglas `@font-face`.
   - Las 8 fuentes activas cargadas por página suman **1.92 MB de archivos `.ttf` sin comprimir** (`IBMPlexSans-VariableFont_wdth,wght.ttf` pesa 520 KB; `IBMPlexSans-Italic...` pesa 580 KB).
   - La conversión a formato moderno **WOFF2 con subconjunto de caracteres Latin** reduciría el peso total de fuentes a menos de 250 KB (ahorro superior al 85%).
2. **Rutas Relativas Rotas para Tipografías**:
   - En el `<style>` de cada archivo HTML, las reglas `@font-face` se declaran como:
     `src: url("../public/fuentes/Outfit/Outfit-VariableFont_wght.ttf") format("truetype");`
   - Si la carpeta `envios/` se despliega como raíz del servidor web (lo habitual en Vercel, Netlify o servidores estáticos), la ruta `../public` se encuentra fuera del docroot, produciendo **errores 404 inmediatos** y provocando que el sitio retroceda a la fuente del sistema (Arial).

---

### 4.9. Infraestructura en Producción, Vercel Edge y Seguridad

La inspección en vivo de `https://www.enviosdosruedas.com/` demostró una infraestructura de producción sólida y bien configurada:

- **Red Edge Anycast de Vercel**: Servidor `Server: Vercel`, datacenter `gru1` (São Paulo, Brasil), con baja latencia para el cono sur.
- **Certificado SSL/TLS**: Emitido por Let's Encrypt (`CN=YR1`), con cobertura para `*.enviosdosruedas.com` y `enviosdosruedas.com`. Protocolo moderno **TLSv1.3** con cifrado `TLS_AES_128_GCM_SHA256`.
- **Cabeceras de Seguridad Verificadas**:
  - `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload` (HSTS de 2 años activo).
  - `X-Frame-Options: SAMEORIGIN` (prevención de ataques de clickjacking).
  - `X-Content-Type-Options: nosniff` (bloqueo de sniffing de MIME types).
  - `Content-Security-Policy`: Política estricta `default-src 'self'` con dominios autorizados de Google Tag Manager, Google Analytics, Ahrefs, OpenStreetMap y WhatsApp (`form-action 'self' https://api.whatsapp.com`).
  - `X-Nextjs-Prerender: 1`: Páginas estáticas optimizadas mediante Static Site Generation (SSG) / ISR con cabeceras `X-Vercel-Cache: HIT`.

---

### 4.10. Paridad Producción vs. Repositorio: Las 3 Páginas Faltantes

Al contrastar la navegación en vivo con los archivos del repositorio, se constató que **tres páginas activas y vitales en producción no existen en el repositorio local `envios/`**:

1. **`https://www.enviosdosruedas.com/cobertura/`**:
   - Tamaño en vivo: **238,048 bytes**.
   - Título: `"Tarifas y Cobertura de Envíos en Mar del Plata | Envíos DosRuedas"`.
   - Encabezado `<h1>`: `"LLEGAMOS A TODO MAR DEL PLATA"`.
   - Contenido: Detalle cartográfico y tarifario de los 5 radios de cobertura en General Pueyrredón (desde Microcentro hasta Batán, Sierra de los Padres y Santa Clara).
2. **`https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata/`**:
   - Tamaño en vivo: **105,275 bytes**.
   - Título: `"Guía Mercado Envíos Flex en MDQ | Envíos DosRuedas"`.
   - Encabezado `<h1>`: `"CÓMO OPERAR MERCADO ENVÍOS FLEX EN MAR DEL PLATA"`.
   - Contenido: Manual operativo y guía de buenas prácticas para vendedores de Mercado Libre en Mar del Plata (configuración de franjas, embalaje y cumplimiento de horarios).
3. **`https://www.enviosdosruedas.com/servicios/`**:
   - Tamaño en vivo: **213,535 bytes**.
   - Título: `"Servicios de Mensajería y Envíos | Envíos DosRuedas"`.
   - Encabezado `<h1>`: `"NUESTROS SERVICIOS"`.
   - Contenido: Hub centralizador de toda la cartera de servicios logísticos urbanos.

**Consecuencia**: El repositorio local carece de la totalidad de las páginas públicas del negocio, impidiendo realizar cambios o auditorías de paridad completas en entornos locales.

---

### 4.11. SEO Técnico, `sitemap.xml`, Redirecciones 308 y Error 404

1. **Desperdicio de Rastreo por Falta de Trailing Slash en Sitemap**:
   - El archivo `https://www.enviosdosruedas.com/sitemap.xml` declara 19 URLs sin barra diagonal final (ej. `<loc>https://www.enviosdosruedas.com/contacto</loc>`).
   - Sin embargo, el servidor Vercel tiene configurada la directiva `trailingSlash: true`.
   - Por tanto, cada vez que un bot de búsqueda (Googlebot, Bingbot) visita una URL del sitemap, el servidor responde con un salto obligatorio **`HTTP/1.1 308 Permanent Redirect`** hacia la versión con barra (`/contacto/`). Esto consume innecesariamente presupuesto de rastreo (*crawl budget*) y retrasa la indexación.
2. **URLs Fantasma en `sitemap.xml`**:
   - `/servicios/plan-emprendedores`: Declarada en sitemap pero responde con `308 Permanent Redirect` hacia `/servicios/empresas-cuenta-corriente/`.
   - `/servicios/envios-contrareembolso`: Declarada en sitemap pero responde con `308 Permanent Redirect` hacia `/servicios/`.
   - Ambas URLs deben eliminarse del sitemap o reemplazarse por las páginas de destino final.
3. **Discrepancia y Error 404 en Mercado Envíos Flex**:
   - La URL oficial en producción es: `https://www.enviosdosruedas.com/servicios/enviosflex/` (responde `200 OK`).
   - Sin embargo, la versión estándar con guion ortográfico `https://www.enviosdosruedas.com/servicios/envios-flex/` **devuelve un error `404 Not Found`** (74 KB). Los usuarios o enlaces externos que escriben la URL con guion pierden el acceso al servicio más rentable de la empresa.
4. **Directiva `meta name="referrer" content="no-referrer"`**:
   - Presente en todos los archivos de `envios/`. Suprime los encabezados de procedencia en las visitas salientes y entrantes, impidiendo que Google Analytics o los paneles de conversión identifiquen de qué página provienen las conversaciones de WhatsApp.

---

### 4.12. Artefactos de Scraping y Extensiones de Navegador

El análisis de texto plano sobre los 16 archivos reveló que el proceso de captura conservó miles de atributos generados por extensiones del navegador del operador:

- **Atributos de Bloqueador de Anuncios (`bis_skin_checked="1"`)**: Entre 139 y 388 ocurrencias por archivo, sumando **más de 3,500 instancias** en el proyecto. Es un atributo inyectado por extensiones de Chrome (como *Stands AdBlocker* o gestores de contraseñas Bitwarden) que altera el DOM original.
- **Atributos de Superdesign (`data-sd-id="..."`)**: Entre 393 y 950 ocurrencias por archivo, totalizando **más de 9,000 atributos parásitos**. Son identificadores internos del editor de diseño Superdesign.
- **Atributo `bis_register="..."` en `<body>`**: Cadenas en base64 de registro de extensión de navegador presentes en la etiqueta `<body>` de múltiples archivos (ej. `home.html:6013`).
- **Elemento `<next-route-announcer>`**: Nodo inerte generado por el enrutador de Next.js al final del documento que carece de utilidad en páginas puramente estáticas.

---

## 5. MATRIZ COMPLETA DE HALLAZGOS E INCONSISTENCIAS

A continuación se consolidan todos los hallazgos técnicos detectados durante la auditoría integral, clasificados por severidad y dimensión:

| ID | Severidad | Dimensión | Ubicación Exacta | Descripción del Hallazgo | Causa Raíz | Recomendación Concreta de Remediación |
| :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| **H-01** | **P0 (Crítico)** | Técnica / JS | Fin de los 16 archivos en `envios/*.html` (líneas ~6440 a ~8880) | Script universal que ejecuta `e.preventDefault()` en enlaces no `#`, bloqueando navegación interna y clics a WhatsApp. | Código de congelamiento inyectado durante la exportación de Superdesign para pruebas locales. | **Eliminar de inmediato** la etiqueta `<script>` con el listener `e.preventDefault()` en los 16 archivos. |
| **H-02** | **P0 (Crítico)** | Legal / Integridad | `envios/terminos-y-condiciones.html` | El archivo es un clon binario exacto (SHA-256 `D82177D1...`) de `logistica-dosruedas.html`. Términos legales perdidos. | Sobreescritura accidental del archivo durante la exportación del sitio. | **Restaurar el contenido legal auténtico** extrayéndolo de `https://www.enviosdosruedas.com/terminos-y-condiciones/`. |
| **H-03** | **P0 (Crítico)** | Activos / Marca | Las 16 páginas en `envios/*.html` y carpeta `public/` | 100% de las imágenes (31 hashes) apuntan a Supabase bucket externo. Cero imágenes locales en `public/`. | Dependencia provisional de CDN durante la fase de prototipado. | **Descargar las imágenes a `public/images/`** y actualizar los `src` en los HTMLs a rutas locales relativas. |
| **H-04** | **P0 (Crítico)** | Paridad / SEO | Servidor Vercel: `/servicios/envios-flex/` | La URL estándar con guion de Flex devuelve error **404 Not Found** en producción (la oficial es `enviosflex`). | Omisión de regla de enrutamiento/reescritura en `next.config.js`. | **Configurar redirección permanente 308** en Next.js desde `/servicios/envios-flex/` hacia `/servicios/enviosflex/`. |
| **H-05** | **P1 (Alto)** | Rendimiento / CSS| Bloques `<head>` en los 16 archivos de `envios/*.html` | 2.14 MB de CSS inlined embebido en etiquetas `<style>` (45.4% del tamaño total) sin enlace a `contexto/globals.css`. | Falta de pipeline de compilación de Tailwind v4 hacia una hoja de estilos externa compartida. | **Compilar `contexto/globals.css`** a `public/css/globals.css` y reemplazar los bloques `<style>` por `<link rel="stylesheet">`. |
| **H-06** | **P1 (Alto)** | Activos / Marca | `public/logo_nuevo.webp` | Logotipo oficial de alta resolución (640x640 px, 36.4 KB) presente en el repo pero con 0 referencias en el código. | Desconexión entre los recursos locales de diseño y la maquetación HTML. | **Reemplazar la URL remota del logo** en headers y footers por `../public/logo_nuevo.webp` o `/images/logo.webp`. |
| **H-07** | **P1 (Alto)** | Paridad / Catálogo| Directorio `envios/` | Faltan 3 páginas activas en producción: `/cobertura/`, `/guias/envios-flex-mar-del-plata/` y `/servicios/`. | Exportación incompleta del catálogo de rutas del sitio web. | **Descargar e incorporar las 3 páginas faltantes** a `envios/` para lograr paridad 1:1 con producción. |
| **H-08** | **P1 (Alto)** | SEO Técnico | Producción: `sitemap.xml` | URLs sin trailing slash (`/contacto`) generan saltos obligatorios 308 por la regla `trailingSlash: true` de Vercel. | Generador de sitemap no configurado con barras finales. | **Actualizar el sitemap en Next.js** para que emita todas las URLs con barra final canónica (`/contacto/`). |
| **H-09** | **P1 (Alto)** | SEO Técnico | Producción: `sitemap.xml` | URLs fantasma `/servicios/plan-emprendedores` y `/servicios/envios-contrareembolso` que redirigen vía 308. | Enlaces obsoletos de servicios consolidados mantenidos en el sitemap. | **Remover ambas URLs del sitemap** o sustituirlas por sus páginas canónicas activas. |
| **H-10** | **P1 (Alto)** | Rendimiento / Fuentes| Declaraciones `@font-face` en los 16 archivos | Fuentes TTF cargadas con ruta relativa `../public/fuentes/...` que genera 404 al desplegar desde la raíz. | Mala referencia de directorio relativo para despliegues estáticos. | **Normalizar las rutas de fuentes a absolutas** `/fuentes/...` o alojarlas en la carpeta pública del servidor. |
| **H-11** | **P2 (Medio)** | Usabilidad / Móvil | Barra de navegación en los 16 archivos | Botón hamburguesa `#mobile-menu-toggle-opt` apunta a `#mobile-navigation-dialog` que no existe en el DOM. | Componente de diálogo móvil omitido durante la exportación del HTML. | **Crear el contenedor `#mobile-navigation-dialog`** con enlaces del menú y añadir script para alternar visibilidad. |
| **H-12** | **P2 (Medio)** | Accesibilidad / UX | Logo del header y botones en los 16 archivos | `tabindex="0"` anidado dentro de etiquetas `<a>` del logotipo y divs envolventes de botones submit. | Sobreinstrumentación de atributos de foco por herramienta de diseño. | **Remover `tabindex="0"`** de elementos interactivos anidados para cumplir con WCAG 4.1.2. |
| **H-13** | **P2 (Medio)** | Accesibilidad / UX | Etiqueta `<body>` en los 16 archivos | Atributo `style="cursor:pointer"` forzado globalmente en todo el cuerpo del documento. | Inyección de estilo en el contenedor canvas de Superdesign. | **Eliminar `style="cursor:pointer"` del `<body>`** para restaurar el cursor de flecha y texto nativo. |
| **H-14** | **P2 (Medio)** | Redundancia | `envios/html.html` | Archivo huérfano redundante de 512 KB con código de `home.html` con sangría expandida. | Copia de respaldo temporal dejada en el repositorio. | **Eliminar de forma segura `envios/html.html`** del repositorio. |
| **H-15** | **P2 (Medio)** | Nomenclatura | `envios/nossobresobre-nosotros.html` | Nombre de archivo malformado con prefijo duplicado (`nossobresobre`). | Error de concatenación de slugs durante el scraping de la ruta `/nosotros/sobre-nosotros/`. | **Renombrar a `sobre-nosotros.html`** y actualizar los hipervínculos internos. |
| **H-16** | **P2 (Medio)** | Rendimiento / Fuentes| Directorio `public/fuentes/` | 13.2 MB en 86 archivos TTF. 12 MB corresponden a variantes estáticas no usadas en `@font-face`. Cero WOFF2. | Descarga masiva de paquetes de Google Fonts sin filtrado. | **Convertir fuentes variables a WOFF2** y purgar las variantes estáticas no utilizadas en `static/`. |
| **H-17** | **P2 (Medio)** | Funcionalidad | `cotizar.html` y `contacto.html` | Formularios carecen de `action`, `method` y submit handlers; datos ingresados por el usuario se pierden. | Deshidratación de componentes de formulario React al exportar a HTML estático. | **Añadir manejadores en JS** que validen los campos y redirijan a WhatsApp con mensaje codificado prearmado. |
| **H-18** | **P2 (Medio)** | Funcionalidad | `logistica-dosruedas.html` | Buscador de código EDR y botones de demostración no ejecutan ninguna consulta ni actualizan el DOM. | Deshidratación del componente de rastreo React. | **Implementar script ligero** que simule los 3 estados de prueba y enlace al portal oficial de tracking. |
| **H-19** | **P2 (Medio)** | Funcionalidad | `nosotrospreguntas-frecuentes.html` | Acordeones 1 a 7 bloqueados en estado cerrado (`aria-expanded="false"`) sin JS para alternarlos. | Deshidratación del componente Radix/Tailwind Accordion. | **Incorporar script vanilla JS o etiqueta nativa `<details>/<summary>`** para apertura accesible. |
| **H-20** | **P2 (Medio)** | Higiene de Código | Los 16 archivos en `envios/*.html` | Miles de atributos parásitos `bis_skin_checked="1"`, `data-sd-id` y tokens `bis_register`. | Interferencia de extensiones de navegador al guardar el DOM fuente. | **Ejecutar script automatizado de limpieza** de atributos parásitos sobre todos los HTMLs. |
| **H-21** | **P3 (Bajo)** | SEO On-Page | `envios/serviciosenviosflex.html` | Título `<title>` repite la marca dos veces: `"Mercado Envíos Flex... \| Envíos DosRuedas \| Envíos DosRuedas"`. | Error de concatenación de plantillas en el componente de metadatos. | **Corregir la plantilla de metadatos** para eliminar la duplicación de marca en el título. |
| **H-22** | **P3 (Bajo)** | SEO / Analítica | Encabezados `<head>` en los 16 archivos | `meta name="referrer" content="no-referrer"` bloquea el tracking de conversión saliente a WhatsApp y analítica. | Parámetro de privacidad residual de la herramienta de diseño. | **Cambiar a `strict-origin-when-cross-origin`** para permitir trazabilidad analítica en Google Analytics y WhatsApp. |
| **H-23** | **P3 (Bajo)** | SEO / Datos Estructurados | Los 16 archivos en `envios/*.html` | Ausencia total de marcado Schema.org JSON-LD (`LocalBusiness`, `FAQPage`, `PostalAddress`). | Omisión de etiquetas estructuradas en las páginas estáticas. | **Añadir bloques JSON-LD** en `home.html`, `contacto.html` y `preguntas-frecuentes.html`. |
| **H-24** | **P3 (Bajo)** | Higiene de Directorios | Raíz: `Drepositoriosccc/` | Carpeta vacía residual con nombre con dos puntos originada por error de sintaxis en Windows. | Script de copia ejecutado con rutas absolutas mal escapadas. | **Eliminar la carpeta corrupta residual** `Drepositoriosccc/`. |

---

## 6. PLAN DE RECOMENDACIONES PRIORIZADAS Y HOJA DE RUTA DE REMEDIACIÓN

Para resolver de manera metódica los hallazgos identificados, se establece una hoja de ruta dividida en cuatro fases estratégicas:

```
                          HOJA DE RUTA DE REMEDIACIÓN EN 4 FASES
 ┌──────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐
 │       FASE P0        │    │       FASE P1        │    │       FASE P2        │    │       FASE P3        │
 │ Inmediato (24-48 hs) │───>│ Corto Plazo (1-2 sem)│───>│ Mediano Plazo (1 mes)│───>│ Largo Plazo          │
 │                      │    │                      │    │                      │    │                      │
 │ • Suprimir killswitch│    │ • Localizar imágenes │    │ • Drawer menú móvil  │    │ • Integración con    │
 │ • Restaurar términos │    │ • Activar logo nuevo │    │ • Acordeón FAQ y form│    │   repo de Next.js    │
 │ • Redirección 404 Flex    │ • Compilar CSS común │    │ • Fuentes WOFF2      │    │ • Pipeline CI/CD     │
 │ • Quitar cursor body │    │ • Incorporar 3 págs  │    │ • Limpieza scraping  │    │ • Datos Schema.org   │
 └──────────────────────┘    └──────────────────────┘    └──────────────────────┘    └──────────────────────┘
```

---

### 6.1. Fase P0: Correcciones Inmediatas de Emergencia (24 a 48 Horas)

El objetivo de esta fase es **eliminar de raíz los bloqueadores de conversión y subsanar las contingencias legales y de navegación**:

1. **Desactivar el Killswitch Universal de Navegación**:
   - *Acción*: Eliminar la etiqueta `<script>` final que contiene `document.addEventListener("click", ... e.preventDefault(); ...)` en los 16 archivos de `envios/`.
   - *Resultado*: Se restaura de inmediato el funcionamiento de todos los hipervínculos internos y de los botones directos de conversión hacia WhatsApp (`api.whatsapp.com`).
2. **Restaurar el Contenido Legítimo de `terminos-y-condiciones.html`**:
   - *Acción*: Descargar el documento legal auténtico desde `https://www.enviosdosruedas.com/terminos-y-condiciones/` y sobreescribir el archivo local que actualmente contiene por error el rastreador de paquetería.
   - *Resultado*: Se restituye el marco legal, las condiciones de servicio y la protección jurídica ante reclamos en Mar del Plata.
3. **Solucionar el Error 404 de Mercado Envíos Flex en Producción**:
   - *Acción*: En la configuración de Next.js del servidor de producción (`next.config.js` o `vercel.json`), añadir la regla de redirección permanente:
     ```json
     {
       "source": "/servicios/envios-flex",
       "destination": "/servicios/enviosflex/",
       "permanent": true
     }
     ```
   - *Resultado*: Se redirige automáticamente el tráfico con guion hacia la ruta oficial, evitando rebotes de potenciales clientes.
4. **Remover el Atributo `style="cursor:pointer"` del `<body>`**:
   - *Acción*: En los 16 archivos HTML, eliminar el atributo `style="cursor:pointer"` de la etiqueta `<body>`.
   - *Resultado*: Se recupera la ergonomía nativa del puntero del mouse, permitiendo al usuario identificar claramente los elementos interactivos reales.

---

### 6.2. Fase P1: Arquitectura, Activos y SEO a Corto Plazo (1 a 2 Semanas)

El objetivo de esta fase es **garantizar la resiliencia de activos, reducir el peso de las páginas y alinear el SEO técnico**:

5. **Localizar y Respaldar Recursos Gráficos (Desconexión de Supabase)**:
   - *Acción*: Descargar las 31 imágenes alojadas en el bucket temporal de Supabase y almacenarlas en `public/images/` con nombres semánticos (ej. `sucursal-friuli.webp`, `hero-mapa-mdq.webp`, `cadete-moto-express.webp`).
   - *Acción*: Actualizar las etiquetas `<img>` de las páginas para que referencien rutas locales relativas seguras (`../public/images/...` o `/images/...`).
6. **Activar el Logotipo Oficial Local (`public/logo_nuevo.webp`)**:
   - *Acción*: Reemplazar las 37 referencias a la URL remota del logo por el archivo local `public/logo_nuevo.webp` (o una versión escalada optimizada a 80x80 px para navbar y footer).
7. **Modularizar y Cachear el CSS Compartido**:
   - *Acción*: Configurar el compilador de Tailwind CSS v4 para procesar `contexto/globals.css` hacia un archivo centralizado `public/css/globals.css`.
   - *Acción*: Sustituir los bloques embebidos `<style>` de más de 5,800 líneas en cada archivo HTML por una única etiqueta de hoja de estilos externa:
     `<link rel="stylesheet" href="/css/globals.css">`.
   - *Impacto*: Reducción de más de **2 MB de código HTML** en el proyecto y habilitación de caché HTTP en el navegador del usuario para todas las navegaciones subsecuentes.
8. **Incorporar las Tres Páginas Faltantes de Producción**:
   - *Acción*: Incorporar al directorio `envios/` los archivos correspondientes a las tres rutas activas en producción:
     - `envios/cobertura.html` (desde `https://www.enviosdosruedas.com/cobertura/`).
     - `envios/guias-envios-flex.html` (desde `https://www.enviosdosruedas.com/guias/envios-flex-mar-del-plata/`).
     - `envios/servicios.html` (desde `https://www.enviosdosruedas.com/servicios/`).
   - *Resultado*: Paridad total del catálogo de rutas entre el repositorio y producción.
9. **Corregir Trailing Slashes y URLs Fantasma en `sitemap.xml`**:
   - *Acción*: En el generador de sitemap de Next.js, asegurar que cada URL de `<loc>` incluya la barra final obligatoria (ej. `<loc>https://www.enviosdosruedas.com/contacto/</loc>`).
   - *Acción*: Eliminar del sitemap las URLs `/servicios/plan-emprendedores` y `/servicios/envios-contrareembolso` que aplican redirección 308.
10. **Saneamiento de Nomenclatura y Eliminación de Duplicados**:
    - *Acción*: Eliminar el archivo redundante `envios/html.html`.
    - *Acción*: Renombrar `envios/nossobresobre-nosotros.html` a `envios/sobre-nosotros.html`.
    - *Acción*: Eliminar el directorio residual corrupto `Drepositoriosccc/` de la raíz del proyecto.

---

### 6.3. Fase P2: Funcionalidad, Accesibilidad y Rendimiento (1 Mes)

El objetivo de esta fase es **restaurar la usabilidad móvil, la interactividad de componentes y optimizar el rendimiento de red**:

11. **Implementar el Menú Móvil y Dropdowns Accesibles**:
    - *Acción*: Crear el marcado del contenedor `<dialog id="mobile-navigation-dialog">` en las páginas de `envios/` y añadir un script ligero vanilla JS (o mecanismo basado en CSS) para alternar el menú y los atributos `aria-expanded` al pulsar `#mobile-menu-toggle-opt`.
    - *Acción*: Proveer funcionalidad de apertura a los dropdowns de escritorio ("Servicios", "Nosotros").
12. **Dotar de Funcionalidad a Formularios y Cotizador**:
    - *Acción*: En `cotizar.html`, implementar un script vanilla JS que calcule las tarifas Express y LowCost según las zonas ingresadas y genere un enlace dinámico hacia WhatsApp con los datos del envío preformateados.
    - *Acción*: En `contacto.html`, enlazar el botón "Enviar Mensaje" a la apertura de WhatsApp con el texto del remitente.
    - *Acción*: En `logistica-dosruedas.html`, permitir que los botones de código de prueba (`EDR-4820-MDQ`, etc.) actualicen visualmente el estado del paquete simulado.
13. **Optimización de Fuentes Tipográficas (WOFF2 y Subsetting)**:
    - *Acción*: Convertir los archivos de fuentes variables (Outfit, Anton SC, Bebas Neue, Geist Mono, IBM Plex Sans) al formato moderno `.woff2` con subconjunto de caracteres Latin.
    - *Acción*: Purgar las 60 variantes estáticas en subcarpetas `static/` de `public/fuentes/`, reduciendo el tamaño total del directorio de fuentes de **13.2 MB a menos de 400 KB**.
    - *Acción*: Configurar rutas absolutas `/fuentes/...` en las declaraciones `@font-face`.
14. **Subsanar Violaciones de Accesibilidad (WCAG 2.1 AA)**:
    - *Acción*: Eliminar los atributos `tabindex="0"` de los divs internos del logotipo y de los contenedores de botones submit.
    - *Acción*: Reemplazar todos los atributos `alt="Image"` o vacíos por descripciones semánticas precisas del servicio logístico.
15. **Sanitización de Artefactos de Scraping**:
    - *Acción*: Ejecutar un script automatizado para limpiar todas las apariciones de `bis_skin_checked="1"`, `bis_register`, `data-sd-id` y `<next-route-announcer>`.

---

### 6.4. Fase P3: Integración Definitiva y Hoja de Ruta Tecnológica (Largo Plazo)

El objetivo de esta fase es **consolidar la plataforma sobre una arquitectura unificada y mantenible**:

16. **Unificación con el Repositorio Next.js de Producción**:
    - *Acción*: Integrar las definiciones de tokens de `contexto/globals.css` y las páginas estáticas de `envios/` dentro del repositorio de desarrollo original de Next.js en Vercel, manteniendo un único flujo de despliegue continuo (CI/CD) controlado por Git.
17. **Implementación de Datos Estructurados Schema.org JSON-LD**:
    - *Acción*: Inyectar marcado estructurado en las plantillas de Next.js:
      - Esquema `LocalBusiness` / `PostalAddress` en home y contacto con base en Friuli 1972, teléfono `+54 9 223 660-2699` y coordenadas de Mar del Plata.
      - Esquema `FAQPage` en `preguntas-frecuentes`.
      - Esquema `Service` con precios en cada página de servicio (`enviosflex`, `envios-express`, `deposito-fulfillment`).
18. **Configuración de Analítica y Referrer**:
    - *Acción*: Reemplazar `content="no-referrer"` por `content="strict-origin-when-cross-origin"` en todos los encabezados HTML para habilitar la trazabilidad de conversiones en Google Analytics 4 y campañas de Google Ads.

---

## 7. DICTAMEN TÉCNICO Y CONCLUSIÓN

La auditoría integral de **Envíos DosRuedas** revela un proyecto con **fundamentos de identidad visual excepcionales y una infraestructura en producción de vanguardia en Vercel Edge**, pero con un **repositorio local en estado crítico de degradación técnica** derivado de un volcado estático asistido por herramientas de diseño:

- **Lo Positivo**: La paleta cromática "Ley de Tres Colores" (`#0950F6` y `#FFEC01`), las firmas double-bezel, la tipografía jerarquizada y el despliegue en Vercel con SSL TLSv1.3 y HSTS otorgan a la empresa una imagen institucional sumamente profesional y confiable.
- **Lo Crítico**: La presencia del script `e.preventDefault()` que bloquea la navegación y los enlaces de WhatsApp, la pérdida de los términos legales en `terminos-y-condiciones.html`, la vulnerabilidad de depender al 100% de un bucket externo de Supabase para las imágenes, el bloat de 2.14 MB de CSS inyectado y la falta de 3 páginas activas en el repositorio impiden que el código local funcione de manera autónoma.

La ejecución estricta del **Plan de Remediación Priorizado (P0 a P3)** permitirá subsanar los bloqueadores funcionales en menos de 48 horas, desacoplar la arquitectura de activos en dos semanas y consolidar la plataforma sobre una base de código moderna, accesible, rápida y orientada a la máxima conversión comercial en Mar del Plata.

---
*Informe concluido y registrado para verificación técnica independiente.*
