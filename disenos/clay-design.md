---
version: "superdesign-alpha"
name: "Claymation infrastructure"
description: "Light-mode-default editorial system built on a warm off-white canvas, sculpted 3D-toy illustration, one lime-chartreuse accent, and rationed color bands (blue/coral/sand) that partition a long feature scroll."
colors:
  background: "#FEFDFB"
  surface: "#F4F3F0"
  surface-alt: "#FFFFFF"
  text-primary: "#000000"
  text-secondary: "#55534E"
  text-tertiary: "#79756D"
  accent-lime: "#EEF773"
  accent-lime-deep: "#CBD810"
  ink-deep: "#1B1A18"
  border-hairline: "#D1CDC7"
typography:
  display-lg:
    fontFamily: "Roobertvf"
    fontSize: "88px"
    fontWeight: 575
    lineHeight: "1"
    letterSpacing: "-3.5px"
  headline-md:
    fontFamily: "Roobertvf"
    fontSize: "72px"
    fontWeight: 500
    lineHeight: "1"
    letterSpacing: "-2.2px"
  body-md:
    fontFamily: "Roobertvf"
    fontSize: "14px"
    fontWeight: 500
    lineHeight: "1.5"
  label-md:
    fontFamily: "Roobertvf"
    fontSize: "48px"
    fontWeight: 500
    lineHeight: "1"
    letterSpacing: "-1.9px"
  body-default:
    fontFamily: "Roobertvf"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "1.5"
  icon-accent:
    fontFamily: "Phosphor"
    fontWeight: 400
    lineHeight: "1"
spacing:
  base: "8px"
  gap-tight: "5px"
  gap-sm: "10px"
  gap-md: "16px"
  content-max-width: "479px"
  section-padding: "64px"
  section-gap: "479px"
rounded:
  control: "12px"
  control-alt: "8px"
  card: "18px"
  card-lg: "24px"
  card-sm: "14px"
  pill: "9999px"
components:
  button-nav-cta:
    background: "#000000"
    text-color: "#FFFFFF"
    radius: "12px"
    height: "39px"
    padding: "8px 16px"
    border: "1px solid rgba(0, 0, 0, 0)"
    hover-background: "#282C35"
  button-hero-primary:
    background: "#CBD810"
    text-color: "#000000"
    radius: "16px"
    height: "47px"
    padding: "9px 18px"
    border: "1px solid rgba(0, 0, 0, 0)"
  button-hero-secondary:
    background: "transparent"
    text-color: "#FFFFFF"
    radius: "16px"
    height: "47px"
    border: "1px solid rgba(255, 255, 255, 0.4)"
  button-accent-lime:
    background: "#EEF773"
    text-color: "#1B1A18"
    radius: "12px"
    height: "44px"
    padding: "10px 16px"
  button-ink-solid:
    background: "#1B1A18"
    text-color: "#FEFDFB"
    radius: "12px"
    height: "40px"
    padding: "0px"
  card-mini-tile:
    background: "#FEFDFB"
    radius: "18px"
    padding: "16px 20px"
    shadow: "rgba(255, 255, 255, 0.05) 0px 0px 0px 1px inset"
  card-panel-blue:
    background: "#F0F8FF"
    radius: "24px"
    padding: "0px"
    shadow: "rgb(240, 248, 255) 0px 0px 0px 2px inset"
  card-panel-coral:
    background: "#FFF3ED"
    radius: "24px"
    padding: "0px"
    shadow: "rgb(255, 243, 237) 0px 0px 0px 2px inset"
---
# Claymation infrastructure
Source: https://www.clay.com/

## Overview
This is a light-mode-default, editorial-illustrative system: an off-white/cream canvas (`#FEFDFB`, `#F4F3F0`) carries oversized tight-tracked display type and long-form product storytelling, while all visual richness is delegated to a recurring cast of glossy, soft-shadowed 3D-toy illustrations (matte clay geometry, primary-colored props on sand or gradient-sky grounds). It reads as a hybrid of Swiss-grid typographic confidence — huge negative-tracked headlines at -3.5px/-2.2px letter-spacing — and a claymorphism-adjacent illustration language, without the system itself adopting soft-shadow claymorphic chrome on its UI. Color is otherwise rationed: one chartreuse-lime accent (`#EEF773`/`#CBD810`) marks every primary action and active state, and alternating pastel section bands (dilute blue, coral, sand) segment an otherwise monochrome black-on-cream page.

## Composition
The first screen opens on a full-bleed illustrated diorama (grass hills, sky gradient, toy props) with a transparent 59px navbar overlaid on it; headline and CTA cluster sit in the lower third against a solid dark-green illustration ground, so the type reads white-on-color rather than on the page's true off-white base. Immediately below, a large cream card overlaps the hero's bottom edge, introducing a logo-strip band — the page's actual dominant surface (near-white/cream, ~50%+ of pixels) begins here and persists for the rest of the scroll. From there the rhythm is a repeating unit: eyebrow label → two-tone headline (black + one color-word) → body copy → small logo-cluster proof line → button pair → large illustration or product-screenshot panel, alternating a pastel-tinted background band (blue, then coral/rust) with plain cream bands between. The deliberate choice is illustration-carries-density: sections are sparse in text and UI chrome, letting one big render do the explaining, rather than a dense bento of stat cards — this keeps the page feeling like a picture book of a technical system, not a dashboard screenshot wall.

## Colors
`#FEFDFB` and `#F4F3F0` are the true background/surface roles — confirmed by the pixel field's ~50%+ near-white dominance — with `#FFFFFF` used for card fills sitting on the cream page. `#000000`/`#1B1A18` is the universal text-primary and default UI-fill ink (nav CTA, solid buttons); `#55534E` and `#79756D` step down for secondary/tertiary copy. `#EEF773`/`#CBD810` chartreuse-lime is the single rationed accent — it appears only on the hero primary button, one mid-page filter chip's active state, and one mid-page CTA, never as a background wash. Pastel section bands (a diluted blue near `#F0F8FF`, a coral/blush near `#FFF3ED`) rotate to separate feature bands without introducing new ink colors — text inside them stays black. The hero's green illustration ground is the only large saturated fill on the page, and it is illustration, not chrome — the system deliberately leaves its actual UI surfaces uncolored (cream/white/black only) so the accent and the illustrations do all color signaling.

## Typography
Display headlines run Roobertvf at 88px/575 weight, line-height 1, tracked in tight to -3.5px — used once, hero-only. A secondary headline size (72px/500, -2.2px tracking) repeats at the top of every mid-page feature band, frequently with one clause set in the color of that section's accent (blue, orange/rust, teal) rather than black — a two-tone headline treatment covering roughly one line or phrase per heading, never the whole sentence. A 48px/500 label size (-1.9px tracking) serves oversized standalone statements. Body copy sits at 14–16px/400–500, regular tracking, 1.5 line-height, in `#000000` with `#55534E` for secondary/proof-line text. Phosphor supplies all inline iconography (arrows, search, chat) at small sizes matched to adjacent text.

## Layout
Content is capped at a 1280px max-width, centered, with generous 64px section padding and very large (measured ~479px) gaps between major bands — confirming the sparse, one-idea-per-scroll rhythm. Two grid families recur: a 2-column 50/50 split (media panel + text panel, alternating sides) used for each feature band, and a small icon-plus-caption tile grid used for proof/logo strips — rows composed as [12] then [20/13/14] in one instance and [14] then [11/12] in another, i.e., one full-width lead row followed by a row of 2–3 uneven tiles, not a uniform bento. A transparent full-width panel wrapping 3–4 tiles appears at the top of the page (logo/proof band) and again mid-page (filter-chip rail), padding 80px top / 0 sides / 24px bottom on the wider instance. Card tiles proper are consistently `#FEFDFB`, 18px radius, 16px/20px padding — small, low-elevation, icon-plus-text units, never image-heavy.

## Components
- **Navbar**: 59px tall, sticky, transparent background over the hero illustration; 6 primary nav items plus a search trigger, session link, and two right-aligned actions. Secondary button ("Get a demo"-role) is an outline/light pill; primary CTA is solid `#000000` fill, `#FFFFFF` text, 12px radius, 39px height, 8px 16px padding, hover shifts fill to `#282C35`. Logo is a small wordmark with a colored circular glyph, left-aligned.
- **Hero primary button**: an observed solid lime-chartreuse pill (~`#CBD810` fill, black text), 16px radius, 47px height, 9px 18px padding — the single most emphasized control on the first screen, paired with a lower-emphasis outline/ghost button beside it (white text, translucent border) for the secondary action.
- **Filter-chip rail**: a horizontal row of pill-shaped text chips mid-page; inactive chips sit on a light-gray fill, the active chip fills solid lime (`#EEF773`) with dark ink text — a selected-state pattern for switching displayed feature content.
- **Feature band (×3+, one per scroll section)**: alternating 2-column 50/50 layout; text column carries a small pill eyebrow label (colored fill, e.g. deep blue or rust, white/dark text, uppercase), a two-tone headline, body paragraph, a tiny 3-icon logo row with a one-line customer-proof caption, and a CTA pair (one filled lime/ink button + one plain outline or underlined text-link with arrow). Media column is a single large clay-illustration render on a warm sand/gradient ground, rounded ~24px corners, filling the full column height.
- **Mini icon-tile card (×3–4 per grid)**: `#FEFDFB` fill, 18px radius, 16px/20px padding, inset hairline shadow (`rgba(255,255,255,0.05) 0 0 0 1px inset`); anatomy is a small icon glyph followed by one to two lines of dense body text — used in proof-strip and integration-style grids.
- **Data/table showcase card**: a large cream panel containing a simulated spreadsheet-style table (checkbox column, ~10 data columns, alternating row tint on the active row) with a floating smaller form-panel and a floating email-preview panel overlapping its lower edge — a compound layered composition, not a simple card.
- **Video/media showcase card**: full-width rounded panel (~24px radius) containing a color-gradient illustrated still with a centered translucent circular play-button glyph; flanked left/right by narrow partially-cropped sibling panels in different tint gradients, implying a horizontal rail.
- **Logo/proof strip band**: a full-bleed cream card overlapping the hero's base; contains a centered proof sentence and a row of grayscale/full-color partner wordmarks at uniform baseline height, some paired with a small stat badge card beside them.
- **Article/link tile row (bottom-of-page)**: 2–3 wide low cards, left one carrying a dark gradient corner-swoosh graphic, others plain cream with a title line and small thumbnail — a simple link-out card family distinct from the icon tiles.
- **Footer**: `#FFFDF9`-toned background sitting on a full-bleed illustrated ball-pit/hill graphic; five label-headed link columns (uppercase small labels, ~64 links total), a small "hiring" pill badge on one link, wordmark + copyright line centered below, three circular social icon buttons bottom-right.

## Graphics & Effects
The signature graphic mode is rendered 3D clay/toy illustration (matte plastic geometry, soft ambient shadows, warm neutral or sky-gradient grounds) used as the dominant visual carrier in the hero and in every feature band's media column — these are static illustrated stills, not photography. A vertical scrim `linear-gradient(rgba(0,0,0,0) 14%, rgba(0,0,0,0.45) 77%)` darkens the base of hero/media illustrations to hold white headline text legible over the green ground — this covers only the lower ~85% of that one illustration panel, not the full viewport. A soft top-fade `linear-gradient(rgba(255,255,255,0) , rgb(255,255,255))` blends the hero's illustration into the cream page below, covering a thin band (~2% of page height) at the hero/body seam. Card and panel edges use inset hairline "shadows" rather than drop shadows — `rgba(255,255,255,0.05) 0 0 0 1px inset` on plain tiles, colored 2px insets (`rgb(240,248,255)`, `rgb(255,243,237)`) on the tinted section panels — giving a flat, bordered-card feel rather than floating elevation. A `blur(50px)` backdrop-filter appears on an overlay surface (cookie-consent style panel), producing a frosted glass panel over the busy hero art. Where the source uses live video, substitute a static illustrated-gradient still cropped to the same rounded panel.

## Motion
Transitions are short and purposeful: `background-color 0.3s cubic-bezier(0.075, 0.82, 0.165, 1)` for hover fills, `transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1)` and a quicker `transform 0.3s ease-out` for hover lifts/scales, and `color 0.1s ease-out` for near-instant text-color swaps on hover. Keyframe animations (`spin`, `load`, `marquee`, `marquee-up`, `marquee-down`, `fadein`) drive continuous logo-marquee rails and loading spinners. GSAP with ScrollTrigger plus native CSS scroll-driven animations stage the section-by-section reveals as the page scrolls — content fades/slides in per band rather than animating continuously, reinforcing the one-idea-per-scroll composition.

## Guardrails
- Keep the page background cream/white (`#FEFDFB`/`#F4F3F0`) — never default to a dark or saturated full-page fill; only the hero illustration ground carries saturated color.
- Reserve chartreuse-lime strictly for primary CTAs and active chip/filter states — do not tint cards, backgrounds, or body text with it.
- Never render illustration panels as photography or screenshots; they must read as glossy clay/toy 3D renders with soft grounded shadows.
- Keep card elevation flat (hairline inset shadows), not drop-shadow-floating — this system does not use soft outer glows or heavy elevation.
- Preserve the tight negative letter-spacing (-3.5px/-2.2px) on all large headlines; loosened tracking breaks the display identity.
- Do not merge the icon-tile grid and the feature-band media panel into one card type — they have distinct radii, fills, and internal anatomy.