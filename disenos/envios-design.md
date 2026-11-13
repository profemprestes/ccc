---
version: "superdesign-alpha"
name: "DosRuedas Electric Dispatch"
description: "High-contrast urban logistics design system built on electric blue (#0950F6) hero bands, pure white (#FFFFFF) content surfaces, high-visibility yellow (#FFEC01) CTAs, and blue-tinted elevation shadows."
colors:
  background: "#FFFFFF"
  surface: "#E6EEFE"
  surface-dark: "#031811"
  brand-blue: "#0950F6"
  brand-blue-400: "#3570F8"
  brand-blue-300: "#628FF9"
  brand-blue-100: "#BACEFD"
  brand-blue-50: "#E6EEFE"
  text-primary: "#0950F6"
  text-on-dark: "#FFFFFF"
  accent: "#FFEC01"
  accent-hover: "#FFF12E"
  accent-600: "#E6D400"
  whatsapp-green: "#2ECC85"
typography:
  display-lg:
    fontFamily: "Anton"
    fontSize: "56px"
    fontWeight: 400
    lineHeight: "1.02"
    letterSpacing: "0.5px"
    textTransform: "uppercase"
  subheading-md:
    fontFamily: "Bebas Neue"
    fontSize: "32px"
    fontWeight: 400
    lineHeight: "1.1"
    letterSpacing: "0.8px"
  headline-md:
    fontFamily: "Outfit"
    fontSize: "40px"
    fontWeight: 800
    lineHeight: "1.12"
    letterSpacing: "-0.4px"
  body-lg:
    fontFamily: "Outfit"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: "1.55"
  body-md:
    fontFamily: "Outfit"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "1.5"
  mono-data:
    fontFamily: "Geist Mono"
    fontSize: "14px"
    fontWeight: 500
    lineHeight: "1.4"
spacing:
  base: "8px"
  gap: "24px"
  section-padding: "80px"
  container-max: "1280px"
rounded:
  sm: "6px"
  md: "8px"
  lg: "12px"
  xl: "16px"
  2xl: "24px"
  3xl: "32px"
  pill: "9999px"
components:
  button-primary-yellow:
    background: "#FFEC01"
    text-color: "#0950F6"
    radius: "9999px"
    height: "48px"
    padding: "12px 28px"
    shadow: "0 0 28px #ffec0173, 0 8px 24px #0950f62e"
    hover-background: "#FFF12E"
  button-secondary-blue:
    background: "#0950F6"
    text-color: "#FFFFFF"
    radius: "9999px"
    height: "48px"
    padding: "12px 28px"
    hover-background: "#3570F8"
  button-outline-light:
    background: "transparent"
    text-color: "#FFFFFF"
    radius: "9999px"
    height: "48px"
    padding: "12px 28px"
    border: "1px solid rgba(255, 255, 255, 0.45)"
  button-whatsapp:
    background: "#2ECC85"
    text-color: "#031811"
    radius: "9999px"
    height: "44px"
    padding: "10px 22px"
  navbar:
    background: "#0950F6"
    text-color: "#FFFFFF"
    height: "72px"
  card-service:
    background: "#FFFFFF"
    radius: "24px"
    padding: "28px"
    border: "1px solid #BACEFD"
    shadow: "0 16px 32px #0950f61f, 0 8px 16px #0950f614"
  card-double-bezel:
    outer-background: "#E6EEFE"
    inner-background: "#FFFFFF"
    radius: "24px"
    padding: "6px"
  footer:
    background: "#0950F6"
    text-color: "#FFFFFF"
---
# DosRuedas Electric Dispatch
Source: `d:\repositorios\ccc\envios\` (Envíos DosRuedas — Mar del Plata)

## Overview
DosRuedas Electric Dispatch is an energetic, high-contrast urban logistics system built for instant legibility and conversion. Instead of neutral grays, the entire system anchors its ink, borders, and elevation shadows in **Electric Blue (`#0950F6`)**, paired with **Pure White (`#FFFFFF`)** resting surfaces and **High-Visibility Yellow (`#FFEC01`)** reserved for primary calls to action, active badges, and route accents. The visual voice combines industrial display typography (`Anton` and `Bebas Neue`) with clean geometric body copy (`Outfit`) and tabular telemetry (`Geist Mono`) for quotes, cut-off times, and package tracking.

## Composition
Pages open with a full-bleed `#0950F6` hero band overlaid with a subtle procedural dot grid and dashed `#FFEC01` route curves (`stroke-dasharray: 12 16`). A 12-column asymmetric grid (`lg:grid-cols-12`, 7 columns for headline/CTAs, 5 columns for interactive quote/status widget) establishes immediate utility above the fold. Below the hero, sections alternate between `#FFFFFF` pure white bands, `#E6EEFE` (`brand-blue-50`) soft-tinted bands, and occasional `#0950F6` high-impact callout bands, closing on a dense `#0950F6` multi-column footer.

## Colors
- **Electric Blue (`#0950F6` / `--color-brand-blue-500`)**: Carries both primary hero/footer fills and the main text ink role (`--color-brand-ink`) on light surfaces, supported by a 6-step tint ramp (`#E6EEFE` → `#BACEFD` → `#8EAFFB` → `#628FF9` → `#3570F8` → `#0950F6`).
- **High-Vis Yellow (`#FFEC01` / `--color-brand-yellow-500`)**: Used exclusively for high-priority CTAs, text selection (`selection:bg-brand-yellow selection:text-brand-blue`), route node dots, and promotional highlights, with hover state `#FFF12E` and pressed/dark accent `#E6D400`.
- **Pure White (`#FFFFFF` / `--color-brand-white`)**: Primary page canvas (`bg-brand-white`) and card interior surface.
- **Scoped WhatsApp / MarDelivery Mint (`#2ECC85`) & Deep Forest (`#031811`)**: Rationed strictly to WhatsApp action buttons, live status indicators, and MarDelivery QR modules — never used as general brand chrome on standard pages.

## Typography
- **Display (`Anton` / `Anton SC`)**: Uppercase, tight-leading (`1.02`) headlines for hero statements and bold numerical callouts.
- **Subheading (`Bebas Neue`)**: Condensed uppercase section kickers, service category labels, and badge headers (`letter-spacing: 0.8px`).
- **Sans Body (`Outfit`, fallback `IBM Plex Sans`)**: Weights `300–900` for UI controls, navigation, service descriptions, and readable long-form copy.
- **Monospace (`Geist Mono`)**: Prices, tracking IDs, horario de corte (`13:00 hs`, `20:00 hs`), and technical metadata.

## Layout
Content sits inside a centered `max-w-7xl` (`1280px`) container with responsive horizontal padding (`px-4 sm:px-6 lg:px-8`) and generous vertical rhythm (`py-14 sm:py-20 lg:py-24`). Service grids use 2- and 3-column layouts (`gap-6` / `24px`) with generous `rounded-2xl` (`24px`) and `rounded-3xl` (`32px`) corners. Interactive widgets (cotizador, tracking) use `.double-bezel-inner` framing: an outer `#E6EEFE` shell with `1px solid #BACEFD` wrapping a crisp `#FFFFFF` inner surface.

## Components
- **Navbar**: Fixed top bar (`72px`), solid `#0950F6` over hero transitioning smoothly (`duration-300`) on scroll with border/shadow. Houses the circular Envíos DosRuedas logo (`488abaaa...webp`), concise nav links, and a primary yellow CTA pill.
- **Button — Primary Yellow Pill**: `#FFEC01` fill, `#0950F6` bold text, `rounded-full` (`9999px`), enhanced with `--shadow-cta-glow` (`0 0 28px #ffec0173, 0 8px 24px #0950f62e`), hover → `#FFF12E`.
- **Button — Secondary Blue Pill**: `#0950F6` fill, `#FFFFFF` text, `rounded-full`, hover → `#3570F8`.
- **Button — Outline Light Pill**: Transparent fill, `1px solid rgba(255,255,255,0.45)`, `#FFFFFF` text for secondary actions on blue hero bands.
- **Button — WhatsApp Pill**: `#2ECC85` fill with `#031811` text for direct order/chat triggers.
- **Double-Bezel Service Card**: Outer `rounded-2xl` (`24px`) container in `#E6EEFE` with inner `#FFFFFF` card, `1px solid #BACEFD`, and `--shadow-lg` / `--shadow-hover-lift` on hover.
- **Footer**: Full-bleed `#0950F6` surface with white/yellow links, brand logo, Mar del Plata (MDQ) contact details (`2236602699`), and legal links.

## Graphics & Effects
Every elevation shadow is tinted in `#0950F6` rather than neutral black (`--shadow-sm` through `--shadow-antigravity-deep: 0 24px 64px #0950f638`), keeping white cards luminous against `#E6EEFE` backgrounds. Yellow glow tokens (`--shadow-glow-yellow: 0 0 25px #fff12e73`, `--shadow-cta-glow`) draw immediate eye focus to primary conversion buttons. Hero backgrounds layer a subtle SVG dot pattern and animated dashed yellow route paths (`opacity: 0.2`) to reinforce moto-courier movement without hurting text contrast.

## Motion
Transitions use clean `300ms` CSS property transitions on `background-color`, `border-color`, `box-shadow`, and `transform` (`hover:-translate-y-1`). Dashed SVG route lines pulse gently (`motion-safe:animate-pulse`) and respect `prefers-reduced-motion: reduce`.

## Guardrails
- Never use neutral gray (`#666`/`#999`) or pure black (`#000`) for body text on light backgrounds — always use `#0950F6` (`--color-brand-ink`) or tinted blue-slate shades.
- Never use black-tinted box shadows; all elevation shadows must use `#0950F6` alpha values.
- Reserve `#FFEC01` for high-priority CTAs, selection highlights, and small status accents — never as a full-page background.
- Keep `#2ECC85` strictly scoped to WhatsApp and MarDelivery states so it does not dilute the blue/yellow core identity.
- Preserve Rioplatense Spanish (`vos`, *"Cotizá"*, *"Escribinos"*, *"Mar del Plata"*) across all UI copy.
