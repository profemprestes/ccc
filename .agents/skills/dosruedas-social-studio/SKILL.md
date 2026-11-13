---
name: dosruedas-social-studio
description: >
  Orquesta la creación completa de contenido e imágenes para las redes sociales de Envíos DosRuedas combinando la identidad de marca (brand-style), el motor de calendario y voz (social-content-engine), la edición segura en Canva (canva-edit-design) y la generación de imágenes con IA. Úsalo cuando el usuario pida generar imágenes para redes sociales, armar placas de Instagram, TikTok, LinkedIn o WhatsApp, editar diseños de Canva para la empresa, planificar el calendario de publicaciones o producir campañas visuales de Envíos DosRuedas.
---

# Envíos DosRuedas — Social Studio

Skill reutilizable para producir placas, copys e imágenes de redes sociales alineadas 100% con la identidad visual de **Envíos DosRuedas** (Mar del Plata), sin improvisar colores, tipografías ni tarifas.

## Step 1 — Cargar identidad y voz de marca (`brand-style`)

Antes de diseñar o escribir, lee `reference/brand-and-prompts.md` para fijar:
- **Ley de Tres Colores** (de `contexto/globals.css`): Blanco `#FFFFFF`, Azul Vibrante `#0950F6` (tope máximo de oscuridad, sin negros `#000` ni grises) y Amarillo Vial `#FFEC01` (máximo 15% de cobertura como señal/CTA).
- **Tipografías:** `Anton` / `Anton SC` (Display), `Bebas Neue` (Subtítulos/CTAs), `Outfit` (Cuerpo) y `Geist Mono` (Tarifas/Horarios).
- **Voz:** Cercana, directa, ágil y local (Mar del Plata). Sin tecnicismos vacíos.
- **Fuente de verdad de datos:** Verifica precios, franjas (ej. Express 3 hs, Flex en el día, LowCost) y cobertura contra `https://www.enviosdosruedas.com/` o `envios/` antes de publicarlos en una placa. Nunca inventes precios ni promociones.

## Step 2 — Planificar o actualizar el calendario (`social-content-engine`)

1. Define el lote pedido (una placa puntual o calendario semanal/mensual) indicando para cada pieza: **Fecha**, **Red/Formato** (`4:5` Feed/Ads, `9:16` Stories/Reels, `1:1` Carrusel/WhatsApp), **Servicio/Tema**, **Ruta de producción** (`Canva` o `IA Directa`), y **Texto principal**.
2. **Checkpoint 1 — Aprobación del plan:** Presenta la tabla del lote al usuario y espera su confirmación antes de generar imágenes o consumir cuota de Canva.

## Step 3 — Definir presupuesto y ruta de producción

- **Ruta A — Edición de plantilla existente en Canva (`canva-edit-design`):**
  Usa el protocolo transaccional obligatorio en `reference/canva-and-qa.md`:
  `start-editing-transaction` → `perform-editing-operations` → mostrar miniatura y pedir aprobación → `commit-editing-transaction`.
  Si el cambio pedido está en la lista de limitaciones de la API (cambiar familia tipográfica, agregar cajas de texto nuevas, cambiar fondo o reordenar páginas), informa al usuario qué parte se hace manual en Canva.
- **Ruta B — Generación de imágenes con IA (cuando no hay foto o plantilla base):**
  Usa `image-generator` (o `superdesign` para piezas compuestas) aplicando el **Bloque de Control Cromático** y uno de los 4 pilares de `reference/brand-and-prompts.md`.
- **Reutilización:** Si una pieza se aprueba para Feed (`4:5`), adáptala/redimensiónala a Stories (`9:16`) o LinkedIn en lugar de regenerar desde cero.

## Step 4 — Control de calidad visual (QA) y Copy

Antes de mostrar resultados al usuario, verifica cada pieza contra `reference/canva-and-qa.md`:
1. ¿Hay negros puros o grises neutros? Si sí, rechazar o corregir hacia `#0950F6` / `#E6EEFE`.
2. ¿El amarillo `#FFEC01` supera el 15% del área? Si sí, reducirlo a señal/CTA.
3. Redacta el **copy** de cada post con: *Hook directo → 1 beneficio concreto → 1 CTA (cotizar / WhatsApp) → 3 a 5 hashtags locales*.

**Checkpoint 2 — Aprobación de diseños y copys:** Muestra las miniaturas o imágenes generadas junto con su copy. Nada se guarda en `public/` ni se da por definitivo sin el "sí" del usuario.

## Step 5 — Entrega y staging (nunca publicar solo)

- Guarda los recursos aprobados en `public/social/` con nombre estándar: `[red]-[tema]-[ratio]-[fecha].[png|jpg|webp]` (ej. `ig-express3hs-4x5-20261113.png`).
- Si se editó en Canva, entrega el enlace directo tras el `commit-editing-transaction`.
- Nunca publiques automáticamente en redes; entrega el paquete listo para programar.

## What not to do

- **No generar imágenes sin aprobar primero el plan/lote** — evita desperdiciar cuota y tiempo.
- **No usar negros ni grises neutros en prompts o diseños** — rompe la identidad oficial de `contexto/globals.css`.
- **No hacer `commit` en Canva sin mostrar primero la vista previa y obtener aprobación.**
- **No inventar tarifas, zonas ni horarios** — si falta un dato, pedirlo o consultarlo en el sitio oficial.

## Reference files

- `reference/brand-and-prompts.md` — tokens de color/tipografía, pilares visuales y prompts base listos para IA.
- `reference/canva-and-qa.md` — protocolo transaccional de Canva y checklist de QA antes de entregar.
