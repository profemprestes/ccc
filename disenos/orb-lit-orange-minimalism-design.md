---
version: "superdesign-alpha"
name: "Orb-lit orange minimalism"
description: "Light, near-white editorial system pierced by one saturated orange ration, carried by a rendered sphere hero, tight condensed display type, and flat off-white utility cards."
colors:
  background: "#EFF0F0"
  surface: "#FFFFFF"
  surface-sunken: "#EFF0F0"
  text-primary: "#000000"
  text-on-dark: "#FFFFFF"
  border: "#C5C7C8"
  brand-accent: "#F75D00"
  success: "#00502F"
  neutral-black: "#000000"
typography:
  display-lg:
    fontFamily: "Formular"
    fontSize: "50px"
    fontWeight: 400
    lineHeight: "1.1"
    letterSpacing: "-2.5px"
  headline-md:
    fontFamily: "Formular"
    fontSize: "50px"
    fontWeight: 400
    lineHeight: "1.1"
    letterSpacing: "-2.5px"
  body-md:
    fontFamily: "Formular"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: "1.4"
  label-md:
    fontFamily: "Formular"
    fontSize: "36px"
    fontWeight: 400
    lineHeight: "1.1"
    letterSpacing: "-1.8px"
  body-sm:
    fontFamily: "Formular"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "1.4"
  label-mono:
    fontFamily: "Formular Mono"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: "1.2"
spacing:
  base: "8px"
  gap-sm: "4px"
  gap-md: "12px"
  gap-lg: "20px"
  gap-xl: "60px"
  section-padding: "68px"
  section-gap-sm: "156px"
  section-gap-md: "176px"
  section-gap-lg: "388px"
rounded:
  control: "10px"
  card: "10px"
  chip: "4px"
  capsule: "50px"
  pill: "9999px"
components:
  button-hero-primary:
    background: "#F75D00"
    text-color: "#000000"
    radius: "10px"
    height: "43px"
    border: "1px solid rgba(0, 0, 0, 0)"
  button-hero-secondary:
    background: "#000000"
    text-color: "#FFFFFF"
    radius: "10px"
    height: "43px"
    border: "1px solid rgba(0, 0, 0, 0)"
  button-nav-cta:
    background: "#F75D00"
    text-color: "#000000"
    radius: "10px"
    height: "36px"
    border: "1px solid rgba(0, 0, 0, 0)"
  button-nav-utility:
    background: "transparent"
    text-color: "#000000"
    radius: "0px"
    height: "41px"
    border: "none"
  card-editorial-media:
    background: "transparent"
    radius: "0px"
    padding: "0px"
  card-utility-panel:
    background: "#EFF0F0"
    radius: "10px"
    padding: "0px"
  card-dark-quote:
    background: "#000000"
    text-color: "#FFFFFF"
    radius: "10px"
    padding: "0px"
  card-logo-tile:
    background: "#EFF0F0"
    radius: "10px"
    padding: "0px"
---
# Orb-lit orange minimalism
Source: https://trymeridian.com/?ref=fountn.design

## Overview
This is a light-mode-default editorial system built on an almost-white canvas (#EFF0F0), where a single saturated orange (#F75D00) is rationed out as the sole chromatic signal against black ink and white cards. The dominant carrier of identity is a large rendered 3D sphere — a dot-matrix globe lit half in black shadow, half in orange glow, with a floating dark capsule label overlaid on it — establishing a data-visualization-meets-generative-art tone rather than flat corporate SaaS. Typography is a single condensed grotesque (Formular) doing all the work: tight negative tracking on display sizes gives headlines a compressed, engineered feel, while body copy relaxes to loose, readable leading. The system is Swiss-adjacent in its grid discipline and restraint, but the orb, the orange gradient washes, and the barberpole/marquee motion keep it feeling like a modern AI-product page rather than a print-derived grid.

## Composition
The first screen is a strict two-column split: a left-aligned text block (eyebrow-free headline, two-line subhead, two buttons) against a right-hand hero visual — the illuminated sphere — that bleeds into a warm orange gradient wash filling the entire bottom half of the viewport. Below the fold, the rhythm alternates dense card bands with big black headline lines: a horizontally-scrolling logo strip feeds into a 3-up case-study rail with wide sunset/product photography; then a bento-style product-capability grid with orange-tinted analytics panels; then a 4-up proof-metric row with progress bars and colored status pills; then a testimonial band mixing empty greyscale placeholder tiles with one dark photographic quote card; the page closes on a solid black band before the footer. Section gaps are large and irregular (176px/388px/156px), giving each band room to breathe rather than a uniform stack — the deliberate choice is generous vertical isolation per section over a tight, continuously-scrolling feed, trading density for a slower, more deliberate narrative pace.

## Colors
Background reads overwhelmingly near-white: the pixel field confirms ~78% pure white and ~10% off-white (#F0F0F0), meaning white/near-white canvas is the true dominant surface despite orange being the system's visual signature — orange itself occupies only a thin ration (the declared #F75D00 area is under 1%, concentrated in buttons, chart lines, and gradient washes at the base of sections). Black (#000000) is the second major mass at ~29% declared / ~6% pixel share, carrying the navbar text weight, dark utility cards, the footer, and the hero's shadowed hemisphere. #EFF0F0 is the sunken-surface token for utility/analytics cards, distinguishing them softly from pure-white editorial cards. Borders are a pale #C5C7C8 hairline. Deliberately uncolored: no blues, no purples despite a declared unused `--secondary: #EBE6FF` token — the system commits to monochrome-plus-one-accent and leaves everything else in black/white/grey.

## Typography
Formular is the only family in service, used at radically different tracking depending on role: display and headline sizes sit at 50px/400 weight with lh 1.1 and an aggressive -2.5px letter-spacing, compressing large type into a dense, technical mass; a label size at 36px carries -1.8px tracking for mid-weight section titles. Body copy drops all compression — 20px/1.4 for lead paragraphs, 16px/1.4 for dense card copy — reading conversationally against the tight display type. A monospace cut of Formular appears as the signature accent, used in small uppercase eyebrow labels (all-caps card headers like brand-analytics-style tags) — this mono label face is the one deliberate typographic accent against an otherwise single-family system.

## Layout
Content is capped at a 1440px max-width with 68px section padding. The card grids are genuinely irregular, not uniform: the case-study rail runs 3 cards per row at unequal widths (a narrow flanking pair bleeding off-screen against one full center card); the mid-page analytics band composes as an asymmetric bento — one large left panel, one large right panel, then two more stacked below at similar proportions (rows scaling from ~107% to ~32% of container width across breakpoints), never a clean uniform 3-up. The proof-metric band is a strict 4-column grid at equal 24% spans with 20px gaps. The logo-tile testimonial row runs 6 across at increasingly narrow widths tapering toward the trailing edge (rows 97/97/78/78/37 down to 91), confirming an intentional mosaic taper rather than equal cards. Card density is low — most cards carry a single stat, chart, or checklist, not dense data tables — and the grid response favors horizontal scroll/bleed (case studies, logo strip) over reflow at this breakpoint.

## Components
- **Navbar**: edge-to-edge square-cornered bar (0px radius all four corners), 84px tall, full 1920px viewport width with zero inset, transparent background, sticky on scroll. Holds 17 total items: a rotating dot-pattern logo mark + wordmark at left, four text nav links (Platform, Docs, Resources, Careers) centered-right, then an outlined Login button and a solid orange Get Started capsule CTA at far right (radius 10px, height 36px, fill #F75D00, text #000000, transparent border).
- **Hero primary button**: an observed near-solid orange fill matching #F75D00 with black text, ~10px corners (slightly-rounded, not pill), 43px tall — this is the emphasized "Get Started" pairing on the first screen, distinct from and more prominent than the nav's smaller 36px version.
- **Hero secondary button**: solid black fill (#000000), white text, same 43px height and 10px radius, sitting beside the primary as a lower-emphasis dark twin — used for a demo/secondary action.
- **Nav utility links / text buttons**: transparent fill, black text, 0px radius, 41px tall, no border — the plain nav link style, ×14 across the page including footer-adjacent utility rows.
- **Case-study media cards** (×3, first-screen rail): transparent background, 0px radius, full-width-panel anatomy with a large left-bleed photograph (sunset/pool or hands-exchanging imagery) covering roughly half the card, paired with a large left-aligned headline, small metadata row (employee count + region, separated by a dot), and one solid orange CTA button beneath.
- **Analytics/bento panels** (×6, mid-page): transparent or #EFF0F0 fill, 0px–10px radius, anatomy of icon+mono-label eyebrow, a headline sentence, dense body copy, and an embedded data visual — a line chart with orange gradient fill-under-curve and a floating stat badge, or stacked product-thumbnail cards with numeric badges and star ratings, or a chat-input mock with an orange send button.
- **Proof-metric cards** (×4, 4-column grid): #EFF0F0 sunken fill for two, white for two, 0px radius, each holding an all-caps mono-style label, a short body line, and either horizontal progress bars (orange fill on hatched track, percentage at right) or a numbered checklist with orange circular check icons and a bottom progress-tracker bar, or a metric-vs-change table with dark green pill badges for percentage lift.
- **Testimonial/logo mosaic** (×6, tapering row): #EFF0F0 tile fill, 10px radius, most tiles empty circular logo placeholders on light ground; one tile is a dark (#000000) quote card with a top-bleed close-up photograph (covering roughly 40% of card height), a large orange quotation glyph, quote body in white text, and an attribution line.
- **Footer**: solid black (#000000) background, 18 text links arranged in columns, full-bleed edge-to-edge band closing the page.

## Graphics & Effects
The hero sphere is the system's signature graphic: a dot-matrix-textured 3D orb lit by a soft radial treatment — `radial-gradient(circle at 35% 35%, rgb(0,0,0), rgb(15,15,15) 0%, rgb(255,255,255))` — occupying roughly the right half of the first viewport, with scattered orange dots standing in for illuminated data points and a soft white glow-halo (`rgba(255,255,255,0.75) 0px 4px 54px 40px` plus an inset echo) bleeding around its edge. Below the sphere, an orange-to-off-white vertical wash (`linear-gradient(0deg, rgb(247,93,0), rgb(239,240,240) 50%)`) fills the lower half of the hero viewport only — not the full page — establishing warmth before the content returns to white. That same gradient pattern recurs at smaller scale as background wash inside individual analytics cards (the chart panel, the product-tracking panel) and as a scrim `linear-gradient(126deg, rgb(247,93,0) 10%, rgb(0,0,0))` behind a testimonial card's inset corner. Live/canvas-driven elements (the rotating dot sphere, marquee logo strip) should be rebuilt as a static gradient-and-dot-pattern image stand-in. Backdrop blur is used sparingly at small radii (blur(8px) down to blur(0.512px)) for subtle depth on floating labels like the search-query capsule over the orb.

## Motion
Interactive transitions favor short, snappy timing: `color 0.2s ease` for link hovers, `transform, opacity 0.3s`/`0.15s cubic-bezier(0.17, 0.25, 0.3, 1)` for card and button micro-interactions, and a slower `0.5s cubic-bezier(0.165, 0.84, 0.44, 1)` for width-based reveals (progress bars filling). Named keyframe animations — `spin` (the navbar logo mark's continuous rotation), `nav-banner-marquee` and `logoloop` (the horizontal logo-strip scroll), `barberpole` (diagonal stripe motion on gradient fills), `footerGlobeRotate`, and `dash-move` (animated dashed chart lines) — drive the page's generative, always-slightly-alive feel. Scrolling is handled by Lenis for smoothed inertial scroll. Overall the motion reads as continuous ambient animation (spinning logo, looping marquee, rotating footer element) layered under discrete, quick UI-state transitions.

## Guardrails
- Never let the orange accent become a full-bleed background — it is a rationed gradient wash confined to the lower hero half, card corners, and buttons; the page's true ground is near-white.
- Do not swap the nav's 36px glass-adjacent CTA values onto the hero's primary button — the hero primary is a separate, larger (43px) orange/black pairing.
- Preserve the navbar as an edge-to-edge, perfectly square-cornered (0px all corners) transparent bar — do not round it or inset it into a floating capsule.
- Keep display type at the compressed -2.5px tracking; loosening it dilutes the system's engineered, condensed character.
- Do not average the tapering logo/testimonial row into equal-width tiles — the measured widths decrease across the row and that mosaic taper is structural, not incidental.
- Reserve the monospace cut of Formular strictly for small all-caps eyebrow labels — it is an accent, not a body or display face.