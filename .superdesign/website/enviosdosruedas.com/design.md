---
version: "superdesign-alpha"
name: "Fleet-blue impact grotesk"
description: "A royal-blue-dominant, condensed-display system built on stacked slab headlines, a single rationed yellow accent, and pill-shaped buttons with a soft glow — logistics-grade confidence rendered in poster type."
colors:
  background: "#0950F6"
  surface: "#FFFFFF"
  surface-tint: "#E6EEFE"
  text-primary: "#0950F6"
  text-on-fill: "#FFFFFF"
  accent: "#FFEC01"
  accent-hover: "#FFF12D"
  border-subtle: "#BACEFD"
typography:
  display-lg:
    fontFamily: "Anton"
    fontSize: "72px"
    fontWeight: 400
    lineHeight: "0.92"
    letterSpacing: "-2.2px"
  headline-md:
    fontFamily: "Outfit"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "1.5"
  body-md:
    fontFamily: "Outfit"
    fontSize: "18px"
    fontWeight: 300
    lineHeight: "1.63"
  label-md:
    fontFamily: "Bebas Neue"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: "1.56"
    letterSpacing: "0.9px"
  accent-mono:
    fontFamily: "Geist Mono"
    fontWeight: 400
spacing:
  base: "8px"
  gap: "24px"
  gap-lg: "32px"
  section-padding: "112px"
rounded:
  control: "12px"
  card: "24px"
  card-sm: "16px"
  pill: "9999px"
  sharp: "2px"
components:
  button-hero-primary:
    background: "#FFEC01"
    text-color: "#0950F6"
    radius: "9999px"
    height: "58px"
    border: "1px solid rgb(255, 236, 1)"
    shadow: "rgba(255, 236, 1, 0.15) 0px 2px 4px 0px"
    hover-background: "#FFF12D"
    hover-shadow: "rgba(255, 236, 1, 0.45) 0px 0px 28px 0px, rgba(9, 80, 246, 0.18) 0px 8px 24px 0px"
  button-accent-compact:
    background: "#FFF12E"
    text-color: "#0950F6"
    radius: "9999px"
    height: "44px"
    border: "1px solid rgb(255, 241, 46)"
    shadow: "rgba(255, 241, 46, 0.45) 0px 0px 25px 0px"
  button-ghost-light:
    background: "transparent"
    text-color: "#FFFFFF"
    radius: "9999px"
    height: "44px"
  button-navbar-cta:
    background: "rgba(0, 0, 0, 0.2)"
    text-color: "#FFEC01"
    radius: "16px"
    height: "37px"
  button-navbar-outline:
    background: "transparent"
    text-color: "#FFFFFF"
    radius: "16px"
    height: "42px"
    border: "1px solid rgba(0, 0, 0, 0)"
  card-bare-list:
    background: "transparent"
    radius: "0px"
    padding: "0px"
  card-inverted-glass-footer:
    background: "rgba(9, 80, 246, 0.8)"
    backdrop-filter: "blur(12px)"
    radius: "24px"
    padding: "8px"
    shadow: "rgba(9, 80, 246, 0.12) 0px 16px 32px 0px, rgba(9, 80, 246, 0.08) 0px 8px 16px 0px"
  card-inverted-solid:
    background: "rgba(9, 80, 246, 0.8)"
    radius: "16px"
    padding: "12px"
  card-translucent-dark:
    background: "rgba(255, 255, 255, 0.05)"
    radius: "24px"
    padding: "8px"
    shadow: "rgba(3, 24, 17, 0.3) 0px 4px 16px -2px"
  card-translucent-light:
    background: "rgba(230, 237, 254, 0.8)"
    radius: "24px"
    padding: "8px"
    shadow: "rgba(9, 80, 246, 0.15) 0px 25px 50px -12px"
  navbar:
    background: "#0950F6"
    radius: "0px"
    height: "85px"
---
# Fleet-blue impact grotesk
Source: https://enviosdosruedas.com/

## Overview
This is a flat, poster-driven marketing system: a saturated royal blue dominates nearly every section, white and pale-blue surfaces interrupt for data-dense content, and a single acid yellow is rationed as the only alarm color. The display face is a tight, all-caps condensed grotesk (Anton) stacked in short multi-line headlines, paired with a clean geometric sans (Outfit) for body copy and a compressed display label face (Bebas Neue) for eyebrows and badges. Pill-shaped buttons with soft colored glows, 24px-radius glass cards, and dashed/marquee decorative rails give it a confident, operational-tech feel — industrial logistics energy rendered with playful, high-contrast poster typography rather than minimalist restraint.

## Composition
The first screen is hero-led: a left-aligned stack of an eyebrow pill, a three-line condensed headline with one line highlighted in a yellow block, a body paragraph, a solid-yellow primary pill button beside a ghost text-link, all set against full-bleed blue, with an isometric illustrated pin/map graphic occupying the right half and two floating glass info-chips pinned to it. A scrolling marquee rail of dashed bullet labels caps the hero. Below, the rhythm alternates: a white three-card service-selector band, a blue section header introducing a bento of four feature cards plus a blue-to-lighter-blue gradient callout band, a pale-lavender six-card testimonial grid, a white-card lead-capture form on blue, and a final blue footer band with a CTA strip and four-column link footer. The deliberate choice is maximum color-blocking by section (hard cuts between full blue and full white/lavender bands) rather than a continuous single-background scroll — this creates a drumbeat of alternating contrast instead of a smooth gradient wash, reinforcing a modular, card-catalog read over an immersive one.

## Colors
Blue (`#0950F6`) is the dominant surface — hero, navbar, footer, and callout bands — confirmed by the pixel field where blue variants (#0048F0/#1860F0/#1848F0 family) sum to roughly 55% of rendered pixels. White (`#FFFFFF`, ~19–46% declared) carries the content-dense mid-page bands: service cards, the form panel. A pale blue-white (`#E6EEFE`, ~10% pixel share) softens the testimonial section as a muted alternative to pure white. Yellow (`#FFEC01`/`#FFF12E`/`#FFF12D`) is tightly rationed — under 1–2% of pixels — reserved exclusively for the hero's primary CTA, one highlighted headline clause, badge pills, and the navbar CTA text; it never appears as a background fill. A near-black teal (`#001818`, ~8%) surfaces only in the decorative dot/line texture layer. Borders stay nearly invisible (`#BACEFD`) — structure comes from fill contrast, not strokes.

## Typography
Anton (72px/0.92 line-height/-2.2px tracking) drives every headline, always set in multi-line stacks with one line or clause boxed in solid yellow — the system's signature treatment, covering exactly one short line (2–3 words) per headline, never a full sentence. Bebas Neue (18px, 0.9px tracking) handles eyebrows and small all-caps labels/badges. Outfit carries all running copy: 16px/1.5 for compact UI labels and navigation, 18px/300/1.63 for body paragraphs — a lighter weight that keeps long-form text airy against the bold display type. A monospace family (Geist Mono) appears only for coded/tracking-style accents (ID strings, counters).

## Layout
Content is capped at a 1280px max-width with 112px section padding, giving each band generous top/bottom breathing room against tightly packed card interiors. Card grids run 3-column at 32px or 24px gaps: the service-selector is 3 cards in one row (32/32/32); the feature/portal grid is 3 cards in one row (32/32/32); the testimonial grid is 2 rows of 3 (32/32/32 | 32/32/32), with alternating blue/white/yellow card fills rather than uniform color — a card-grid "checkerboard" rather than bento asymmetry. The footer community band runs 3 cards in one row (gradient-filled, uniform width). Base spacing unit is 8px, scaling through 12/16/24/32px for gaps and internal padding. The system is card-dense but never crowds: generous internal card padding (8–12px wrapping larger content blocks) and consistent 16–24px radii keep the grid feeling soft despite high information density.

## Components
- **Navbar**: edge-to-edge square bar spanning full viewport width (0px inset either side), 85px tall, four-corner radius 0/0/0/0, sticky, solid `#0950F6` fill, 10 total items (logo lockup, 5 nav links/dropdowns, phone number, CTA). Its CTA is a small pill: `rgba(0,0,0,0.2)` fill, `#FFEC01` text, 16px radius, 37px height. A secondary ghost-outline button variant (transparent fill, white text, 16px radius, 42px height, 1px transparent border) sits among the nav utilities, not in the hero.
- **Hero primary CTA**: a solid yellow pill under the headline — observed near-`#FFEC01` fill, ~white/blue text, full pill radius, sitting at prominent size with a visible warm glow; matches the measured 58px-tall yellow pill (`#FFEC01`, text `#0950F6`, 9999px radius, 12px/32px padding, `rgba(255,236,1,0.15)` resting shadow, hover glow `rgba(255,236,1,0.45) 0px 0px 28px 0px`). This is the single most emphasized control on the first screen; the adjacent underlined text link is a secondary ghost action, not a button.
- **Button, accent-compact**: `#FFF12E` fill, `#0950F6` text, 9999px radius, 44px height, 8/16px padding, used mid-page for inline list CTAs (e.g. "cotizar" actions inside service cards); hover scales 1.02×.
- **Button, ghost-light**: transparent fill, white text, 9999px radius, 44px height, no padding — used for marquee/community row link-outs ("seguir", "ver", "iniciar") over colored gradient card footers; hover scales ~1.16×.
- **Service-selector card** (×3, one row): white fill, rounded ~16–24px, bordered hairline, numbered badge top-right (01/02/03), small icon chip, eyebrow label, two-line Anton heading, body paragraph, a pill info-chip divider, a yellow or outline pill CTA at the bottom — full top-to-bottom anatomy per card.
- **Portal/feature card** (×4 in a bento row, one row of 4): white or pale-blue translucent fill (`rgba(230,237,254,0.8)` variant), 24px radius, 8px padding, icon chip + small status-tag pill top, Anton heading, body paragraph, divider rule, checklist tag row at base.
- **Gradient callout/CTA band**: full-width rounded panel, gradient fill `linear-gradient(135deg, rgb(9,80,246) 0%, rgb(9,80,246) 55%, rgb(53,112,248) 100%)`, housing an eyebrow pill, two-line heading, two side-by-side pill buttons (yellow solid + white-outline ghost) — appears once, mid-page, as the trust/tracking CTA band.
- **Testimonial card** (×6 in 2 rows of 3): alternating solid-blue, white-with-yellow-border, and solid-yellow fills, 16–24px radius, star-rating row + time-stamp pill top, bold heading, body quote, divider, circular avatar-initial badge + name footer.
- **Lead-capture form panel**: single white card, ~24px radius, housing a two-column split — left text block (eyebrow, heading, body, fine-print), right a vertical form stack (labeled inputs with icon prefixes, a select dropdown, a full-width yellow pill submit button).
- **Community/gradient card** (×3 in one row): each a different vivid gradient fill (blue, red/orange, green), rounded card, housing a label + a white pill "view" button with arrow icon — a social/community CTA row near the footer.
- **Footer**: solid `#0950F6` fill, top CTA strip (status-dot pill, heading, two pill buttons) above a 4-column link layout (brand block with social icons + address chip, two link columns, a contact-info column with icon rows), 29 total links, bottom legal row.

## Graphics & Effects
A faint grid-dot texture overlays sections at low opacity, built from repeating `linear-gradient(90deg, rgb(46,204,133) 1px, rgba(0,0,0,0) 1px)` and its vertical counterpart — a sparse dot/line grain visible across roughly a fifth of the page, giving the flat blue fields subtle technical texture rather than flatness. A soft radial highlight (`radial-gradient(circle at 30% 20%, rgba(255,255,255,0.08), rgba(0,0,0,0) 60%)`) washes the upper-left of hero-type sections, and a matching yellow-tinted radial (`radial-gradient(circle at 50% 0px, rgba(255,236,1,0.08), rgba(0,0,0,0) 50%)`) sits behind CTA bands — both small localized washes, not full-canvas gradients. The hero's illustrated isometric pin-and-cityscape graphic carries its own scrim (`linear-gradient(to top, oklab(...)/0.8 0%, .../0.2 50%, transparent 100%)`) for label legibility, rendered as a static illustration, not a live canvas. Card shadows are consistently blue-tinted and soft: `rgba(9,80,246,0.06–0.15)` at 2–32px blur, reinforcing elevation without darkening the palette. Backdrop blurs (`blur(4px)/(8px)/(12px)`) apply only to the glass footer-adjacent cards.

## Motion
Interactions are fast and springy: color/fill transitions run at 150–200ms with `cubic-bezier(0.4,0,0.2,1)`; hover transforms (button scale, icon shift) use `cubic-bezier(0.23,1,0.32,1)` over 200ms for an eased-overshoot feel. Named keyframe loops (`float-slow`, `pulse-subtle`, `floaty`, `shuttle`) animate the hero's isometric illustration and its glow path continuously; `marquee-left` drives the dashed-bullet ticker rail infinitely leftward; `pulse-ring` pulses status-dot indicators in the footer CTA. Hover states favor glow-intensification (shadow blur growth) and subtle vertical lift/scale over color inversion, keeping the flat palette intact while signaling interactivity.

## Guardrails
- Never fill a full section background with the small decorative radial or scrim gradients — they belong only to the hero illustration and CTA-band accents.
- Keep yellow strictly rationed: one CTA, one headline clause, badge text, and chip accents only — it must never appear as a large fill.
- Preserve the navbar as a full-bleed, perfectly square-cornered bar — do not round or inset it.
- Do not substitute the glass navbar CTA's values for the hero's solid yellow primary button; they are different components with different roles.
- Maintain the alternating hard color-block rhythm between sections — do not smooth it into one continuous gradient background.
- Keep card radii distinct per family (16px vs 24px) — do not normalize all cards to one radius.