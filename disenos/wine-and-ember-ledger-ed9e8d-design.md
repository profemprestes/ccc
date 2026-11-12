---
version: "superdesign-alpha"
name: "Wine & Ember Ledger"
description: "Warm-paper editorial system anchored by a wine-gradient hero and framing bands, with a rationed ember-orange accent driving every primary action and a tight rounded-geometric display face."
colors:
  background: "#F3EFEA"
  surface: "#FFFFFF"
  surface-alt: "#F3EFEA"
  band-wine: "#6D0633"
  band-wine-dark: "#4E0524"
  band-plum: "#45063B"
  text-primary: "#190A13"
  text-on-wine: "#FFF4EA"
  accent: "#F7972C"
  accent-dark: "#B96409"
typography:
  display-lg:
    fontFamily: "Epilogue"
    fontSize: "56px"
    fontWeight: 780
    lineHeight: "1.03"
    letterSpacing: "-2.1px"
  headline-md:
    fontFamily: "Epilogue"
    fontSize: "38px"
    fontWeight: 760
    lineHeight: "1.1"
    letterSpacing: "-1.2px"
  body-md:
    fontFamily: "Epilogue"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: "1.74"
  label-md:
    fontFamily: "Epilogue"
    fontSize: "12px"
    fontWeight: 640
    lineHeight: "1.74"
    letterSpacing: "2.3px"
  accent-serif:
    fontFamily: "Times New Roman"
    fontStyle: "normal"
    role: "occasional editorial serif accent, used sparingly against Epilogue's geometric grotesk"
spacing:
  base: "7px"
  gap: "24px"
  gap-lg: "68px"
  section-padding: "132px"
rounded:
  control: "13px"
  card-lg: "24px"
  card-sm: "16px"
  pill: "100px"
  chip: "50px"
components:
  button-hero-primary:
    background: "#F7972C"
    text-color: "#2A0110"
    radius: "100px"
    height: "55px"
    padding: "18px 34px"
    border: "1px solid rgba(0,0,0,0)"
    shadow: "rgba(247, 151, 44, 0.66) 0px 14px 34px -14px"
    hover-background: "#FFB050"
  button-nav-cta:
    background: "#6D0633"
    text-color: "#FFFFFF"
    radius: "100px"
    height: "37px"
    padding: "11px 20px"
    border: "1px solid rgba(0,0,0,0)"
    shadow: "rgba(109, 6, 51, 0.75) 0px 12px 28px -14px"
    hover-background: "#4E0524"
  button-glass-secondary:
    background: "rgba(24, 4, 14, 0.42)"
    backdrop-filter: "blur(12px) saturate(1.2)"
    text-color: "#FFF4EA"
    radius: "100px"
    height: "55px"
    padding: "18px 34px"
    border: "1px solid rgba(255, 244, 234, 0.34)"
    shadow: "rgba(255, 244, 234, 0.14) 0px 1px 0px 0px inset"
    hover-background: "rgba(24, 4, 14, 0.6)"
  button-midpage-primary:
    background: "#F7972C"
    text-color: "#2A0110"
    radius: "100px"
    height: "62px"
    padding: "15px 30px"
    border: "1px solid rgba(0,0,0,0)"
    shadow: "rgba(247, 151, 44, 0.7) 0px 12px 28px -14px"
  card-media-top:
    background: "#FFFFFF"
    radius: "24px"
    padding: "0px"
    shadow: "rgba(25, 10, 19, 0.04) 0px 1px 2px 0px"
  card-feature-panel:
    background: "#FFFFFF"
    radius: "16px"
    padding: "32px"
    shadow: "rgba(25, 10, 19, 0.05) 0px 1px 2px 0px, rgba(25, 10, 19, 0.08) 0px 4px 14px -6px"
  card-testimonial:
    background: "#F3EFEA"
    radius: "24px"
    padding: "38px"
    shadow: "none"
  navbar:
    background: "rgba(255, 255, 255, 0.72)"
    backdrop-filter: "blur(20px) saturate(1.4)"
    height: "77px"
    radius: "0px 0px 0px 0px"
---
# Wine & Ember Ledger
Source: https://mozwebsites.com/index.html

## Overview
This is a warm-paper editorial system: an off-white "paper" surface (`#F3EFEA`) carries the bulk of the page, punctuated by deep wine-gradient bands that bracket the hero and the closing conversion strip. It reads as minimalism with a confident accent discipline — flat white cards, generous line-height body copy, and a single ember-orange (`#F7972C`) reserved exclusively for calls to action and numbered/labelled highlights. The display face, Epilogue at very heavy weight (760–780) with tight negative tracking, gives headlines a compact, geometric-grotesk authority; body text drops to regular weight at a comfortable 1.74 line-height, producing a magazine-like rhythm rather than an app-like density. The wine tone doubles as both a "premium editorial" backdrop color and a structural device separating the page into alternating light/dark bands.

## Composition
The first screen opens on a full-bleed wine-gradient hero: large display headline, orange-accented clause, a two-button pair, a floating device-mockup illustration, and a stat badge overlapping its corner. A thin horizontal rule below introduces a 4-up stat row. The page then drops onto the paper surface for a domain-lookup band (still wine-toned, an inset rounded panel), followed by a services introduction with a 3-column-equivalent card cluster (one dark hero card + a 2-column grid of white icon cards). A horizontally-scrolling portfolio rail follows on white. The page returns to a wine band for a 4-step numbered process row, then back to paper for a 3-up testimonial grid, and closes on a wine-gradient CTA band followed by a near-black footer. This alternation — paper / wine / paper / wine / paper / wine-black — is the deliberate rhythm; the alternative (one continuous dark or one continuous light page) is rejected in favor of using color blocks as section punctuation.

## Colors
`#F3EFEA` (paper) is the dominant light surface, hosting services, portfolio, and testimonial sections — roughly the visual majority of scroll area even though white (`#FFFFFF`) cards sit on top of it at high pixel share. The wine family (`#6D0633` base, `#4E0524` dark, `#45063B` plum) forms the hero, the domain-lookup band, the process band, and the CTA band — a deliberate near-black-adjacent depth that reads dark-mode-adjacent within an otherwise light page. `#190A13` is the primary text ink on paper/white; `#FFF4EA` is the inverted text/label tone on wine backgrounds. The ember accent `#F7972C` (with hover state `#FFB050`, and a darker `#B96409` for text-on-orange contexts) is tightly rationed to buttons, the "MAIS PROCURADO" chip, section eyebrows, numeral outlines, and quote marks — never a fill for large surfaces. Borders are near-black hairlines (`#1C0E0E`, `#190810`) used sparingly, since most separation comes from color-block contrast rather than strokes.

## Typography
Epilogue carries the entire system at two extremes: display-lg (56px/780/-2.1px tracking) for hero and section headlines, and body-md (17px/400/1.74 line-height) for supporting copy — a wide weight gulf that does all the hierarchy work without introducing a second family. headline-md (38px/760/-1.2px) steps down for section titles inside content bands. label-md (12px/640, +2.3px tracking, uppercase) marks eyebrows ("PORTFÓLIO"-style kickers) and step/stat captions. A Times New Roman appearance functions as an occasional serif accent layered against the otherwise all-grotesk system — treat it as a rare editorial interruption, not a body face.

## Layout
Content is capped at a 1260px max-width with 132px section padding, giving the page an unhurried, generously-margined editorial cadence. Card grids favor low column counts with wide gutters: a 2-column split (rows [45/41]) pairs a dark feature card against a lighter grid; a 3-column icon-card row (rows [32/32/32 | 32], gap 18px) stacks feature panels; a 3-column testimonial grid (rows [32/32/32], gap 24px) closes with even thirds. The portfolio section breaks from the grid into a horizontal scrolling rail of fixed-width cards with partial peek of the next item — a scroll-driven alternative to a static grid. Corner radii scale by surface: 24px on media cards, 16px on icon-panel cards, 100px pills on every button and input field, giving a soft, capsule-forward geometry throughout.

## Components
- **Navbar**: edge-to-edge, square-cornered bar (0px radius all four corners), 77px tall, spans full 1920px viewport width with zero side inset — not a floating or inset shape. Background `rgba(255, 255, 255, 0.72)` with `backdrop-filter: blur(20px) saturate(1.4)`, sticky on scroll. Carries 9 nav-area items (logo + 6 links + utility icons) plus one CTA pill: `#6D0633` fill, white text, 100px radius, 37px height, 11px 20px padding, hover darkens to `#4E0524` with a -2px lift transform.
- **Hero primary button**: the single most emphasized control on the first screen — an observed solid ember-orange pill (`#F7972C`, dark-plum text) with an arrow glyph, sized larger than any nav element; measured values confirm radius 100px, height 55px, padding 18px 34px, resting shadow `rgba(247, 151, 44, 0.66) 0px 14px 34px -14px`, hover fill `#FFB050` with -2px lift.
- **Hero secondary button (glass)**: seated beside the primary, translucent dark glass — `rgba(24, 4, 14, 0.42)` with `backdrop-filter: blur(12px) saturate(1.2)`, cream text `#FFF4EA`, 100px radius, 55px height, 1px border `rgba(255, 244, 234, 0.34)`, inset highlight shadow; hover deepens fill to `rgba(24, 4, 14, 0.6)`.
- **Mid-page CTA button**: same ember fill/text as hero primary but taller — 62px height, 15px 30px padding, radius 100px, shadow `rgba(247, 151, 44, 0.7) 0px 12px 28px -14px` — used to restate the primary action mid-scroll and in the closing band.
- **Domain-lookup panel**: an inset rounded band inside the wine hero-adjacent section; contains an input field, a `.co.mz` suffix selector, and an orange "Consultar" pill button, with a row of three checkmarked assurance lines below on a thin divider.
- **Service card — hero/dark variant**: one per services section, full-bleed wine-gradient fill, radius 24px, holds an icon chip in ember plus a "MAIS PROCURADO" pill label near the top and a heading toward the base — the visually dominant card of its row.
- **Service icon cards**: arranged 2-up beside the dark hero card; white fill, 24px radius, `rgba(25, 10, 19, 0.04) 0px 1px 2px 0px` shadow, top-anchored icon in a pale peach chip, heading, and 2–3 line body description — anatomy is icon → heading → body, no CTA.
- **Portfolio media cards**: arranged in a horizontal scrolling rail (partial 4th card visible), white fill, 24px radius, top image bleed showing a laptop-mockup screenshot inside a colored circular backdrop, followed below by an eyebrow label, a bold title, a muted subtitle line, and a text "Ver site →" link — media covers roughly the top 60% of the card.
- **Process step row**: 4 items in a single row on the wine band, each anatomy: large outlined numeral (01–04) in translucent wine-on-wine, bold short heading, 2–3 line body, and a small ember-colored duration label beneath a thin top rule — no card container, pure column layout with vertical divider rules above each.
- **Testimonial cards**: 3-up grid, `#F3EFEA` paper fill, 24px radius, no shadow, 38px padding; anatomy is an ember quotation-mark glyph, a multi-line quote in body copy, a thin rule, then a bold name/role line and a muted company/location line.
- **Closing CTA band**: single wide wine-gradient panel, rounded corners, containing an eyebrow label, headline, muted sub-line, the ember primary button paired with a dark glass/outline "WhatsApp-style" secondary button, and a plain-text phone link below.
- **Footer**: transparent background over a near-black wine-plum band, 18 links organized into labeled columns (pages / services / contacts), logo lockup and short description at left, social icon row beneath, thin divider, and a copyright line at the base.

## Graphics & Effects
The hero and CTA-band backgrounds render `linear-gradient(118deg, rgb(109, 6, 51) 0%, rgb(69, 6, 59) 100%)`, covering an estimated 13% of total page area — this is a large but still bounded band, not the entire page background, since paper sections dominate between them. A secondary warm glow, `radial-gradient(120% 90% at 82% 18%, rgba(247, 151, 44, 0.16), rgba(0, 0, 0, 0) 58%)`, washes the upper-right quadrant of the hero only, at ~12% page coverage — this is the sole source of orange tint in the hero, rationed to one corner rather than a full-frame saturated field. A deep near-black vertical fade, `linear-gradient(rgb(31, 4, 23) 0%, rgb(22, 3, 16) 58%, rgb(16, 2, 11) 100%)`, underlies the footer at ~7% coverage. Diagonal wine-to-plum gradients (`linear-gradient(135deg, rgb(122, 10, 59) 0%, rgb(90, 6, 48) 46/48%, rgb(60, 5, 52) 100%)`) fill the process-step band and one service hero card, each around 4–5% of page area. A soft radial scrim, `radial-gradient(closest-side, rgba(247, 151, 44, 0.34), rgba(247, 151, 44, 0.08) 62%, rgba(0, 0, 0, 0) 78%)`, glows behind the device-mockup illustration in the hero to lift it off the wine backdrop. Card elevation stays extremely subtle on white surfaces (`rgba(25, 10, 19, 0.04) 0px 1px 2px 0px`), rising only slightly for feature panels (`rgba(25, 10, 19, 0.05) 0px 1px 2px 0px, rgba(25, 10, 19, 0.08) 0px 4px 14px -6px`) — shadows are used for material separation, not dramatic depth.

## Motion
Transitions favor a shared custom curve, `cubic-bezier(0.22, 0.8, 0.24, 1)`, applied to opacity/transform pairs at 0.7–0.75s for large entrance moves (hero content, section reveals) and to color/gap changes at a snappier 0.25–0.28s for hover feedback (link color shifts, button icon-gap tightening). Buttons universally lift with a -2px vertical transform on hover alongside their fill/shadow deepening — a consistent, restrained "float up" micro-interaction rather than scale or bounce. Named keyframes (pulse, snap, blip, enter) suggest a small library of entrance and attention-pulse effects used for staged content reveals and interactive glyphs (likely the stat badge, chip highlights, and step numerals) rather than continuous ambient motion.

## Guardrails
- Never fill more than a bounded hero/CTA band with the wine gradient — the page's true ground is the light paper surface; do not darken the whole page.
- Keep the ember accent confined to buttons, chips, eyebrows, quote glyphs, and numerals — never use it as a large card or section fill.
- Preserve the navbar as an edge-to-edge, square-cornered, blurred glass bar — do not round its corners or inset it as a floating capsule.
- Do not substitute the glass secondary button's translucent rgba/blur fill with a solid color; it must stay a frosted glass surface.
- Keep button radius at full pill (100px) across all variants; do not shrink hero buttons to the smaller card-radius values (16–24px).
- Maintain the heavy-weight Epilogue display versus regular-weight Epilogue body contrast as the sole hierarchy driver; do not introduce a third body-copy family.