---
version: "superdesign-alpha"
name: "Compute-noir lime"
description: "Near-black dark-mode-default system lit by a single rationed acid-lime accent, oversized condensed grotesk numerals, and quiet monospace data labels."
colors:
  background: "#09090B"
  surface: "#0E0E10"
  surface-alt: "#121215"
  text-primary: "#F4F4F1"
  text-secondary: "#A7A8A1"
  text-tertiary: "#8C8E86"
  accent: "#C6F24E"
  accent-deep: "#76B900"
  border: "#F3F3EF"
typography:
  display-lg:
    fontFamily: "Archivo Black"
    fontSize: "66px"
    fontWeight: 400
    lineHeight: "0.94"
    letterSpacing: "-2px"
  headline-md:
    fontFamily: "Archivo Black"
    fontSize: "52px"
    fontWeight: 400
    lineHeight: "1"
    letterSpacing: "-1px"
  body-md:
    fontFamily: "Space Grotesk"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: "1.63"
  label-md:
    fontFamily: "Archivo Black"
    fontSize: "38px"
    fontWeight: 400
    lineHeight: "1.05"
    letterSpacing: "-0.8px"
  body-base:
    fontFamily: "Space Grotesk"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "1.6"
  label-mono:
    fontFamily: "JetBrains Mono"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: "1.4"
    letterSpacing: "0.06em"
spacing:
  base: "8px"
  gap: "48px"
  micro: "10px"
  tight: "14px"
  hairline: "2px"
  section-padding: "96px"
rounded:
  control: "8px"
  card: "4px"
  panel: "12px"
  pill: "9999px"
components:
  navbar:
    background: "rgba(10, 10, 12, 0.4)"
    backdrop-filter: "blur(24px)"
    radius: "0px"
    height: "64px"
    width: "100% (edge-to-edge)"
  button-primary:
    background: "#C6F24E"
    text-color: "#0B0B0C"
    radius: "9999px"
    height: "40px"
    padding: "10px 20px"
    hover-background: "#E4FFA3"
  button-nav-cta:
    background: "#C6F24E"
    text-color: "#F4F4F1"
    radius: "9999px"
    height: "40px"
  button-secondary-glass:
    background: "#121215"
    text-color: "#A7A8A1"
    radius: "8px"
    height: "34px"
    padding: "8px 14px"
    border: "1px solid lab(96.1271 -0.392228 1.44876 / 0.12)"
    hover-color: "#C1E65B"
  card-media-bleed:
    background: "transparent"
    radius: "0px"
    padding: "0px"
  card-data-panel:
    background: "#0E0E10"
    radius: "0px"
    padding: "20px 22px 12px"
  card-data-simple:
    background: "#0E0E10"
    radius: "0px"
    padding: "20px 22px"
---
# Compute-noir lime
Source: https://artificialinu.com/

## Overview
A dark-mode-default, terminal-adjacent system: near-black surfaces (`#09090B` dominant), condensed all-caps Archivo Black display type sitting directly on the void, and a single acid-lime (`#C6F24E`) accent rationed to CTAs, numerals, and hairline glows. It reads as trading-terminal aesthetics crossed with illustrated character art — a HUD-grade data panel (ticker chart, grid of compute "racks") paired with painterly cartoon-mascot scenes. The mood is engineered restraint: everything is either pure structural neutral or the one acid hue, with a soft green radial glow standing in for ambient light rather than any gradient wash.

## Composition
The first screen is a two-column hero: left column stacked left-aligned text block (headline, one accent-colored line, body, primary pill CTA + two secondary buttons + copyable address chips), right column an illustrated character bleeding past the fold. A full-bleed marquee ticker band immediately breaks the hero's rhythm with a lime-filled strip. Below, a giant single numeral statement (an oversized lime figure, near the width of the display type but multiples larger) anchors a "live stat" band, flanked by a two-column stat pair. Mid-page shifts to a 2-column asymmetric split (35/56 width) pairing editorial copy against a data-panel duo (line chart above, a grid/cluster panel below). The "three things" section drops into a strict alternating-image pattern — text-left/media-right, then media-left/text-right, then text-left/media-right — each row divided by hairline separators, single column, generous vertical gap. The page closes on a full-bleed illustrated cosmic scene with a text/CTA cluster overlaid top-right, then a plain transparent footer. Deliberate choice: keep the grid mostly single-column/alternating rather than a dense card grid — the site trades card density for large sequential storytelling blocks, rejecting a bento-style overview in favor of a linear, scroll-paced narrative.

## Colors
Background is `#09090B` (~48% of pixels) with `#0B0B0C` and `#121215` as slightly-lifted panel neutrals — this is the surface, not any declared "card" color, confirming dark-mode-default. Pure black `#000000` and near-black `#000018`/`#181818` account for the remaining pixel mass, meaning the page is genuinely near-monochrome dark, not colorful. `#C6F24E` (bright acid-lime) is the sole accent — it appears only on the primary CTA fill, the marquee band fill, the giant numeral, and thin glow rings — measured at just 4.1% of area, proof it is heavily rationed against the black field. `#76B900` (deeper NVIDIA-adjacent green) appears at 1.5%, used for secondary glow dots and a darker gradient stop, never as a fill. Text ink is `#F4F4F1` (primary) and `#A7A8A1`/`#8C8E86` (secondary/tertiary), with borders drawn in near-white `#F3F3EF`/`#F7F7EF` at low opacity. Everything outside the lime accent and off-white text is left pure neutral — no secondary brand hue exists.

## Typography
Display and headline sizes use Archivo Black — a heavy grotesque with tight negative tracking (`-2px` at 66px, `-1px` at 52px, `-0.8px` at 38px) and near-1 line-height, giving headlines a blunt, condensed-poster weight; this face also carries the giant standalone numeral statements. Body copy runs in Space Grotesk at 18px/1.63 (and 16px/1.6 for denser paragraphs) — a geometric sans with more air, used for all supporting copy, labels, and secondary text at `#A7A8A1`. A monospace face (JetBrains Mono, small, wide-tracked) is the signature accent for data-chrome: ticker labels, address strings, and eyebrow tags in uppercase — this is the "instrument panel" voice that differentiates the system from generic marketing type.

## Layout
Content is capped at a 1240px max-width with 96px section padding and 42px section gaps. Grid rhythm is loose: a 2-column 48px-gap hero split, a 2-column 56px-gap stat/chart split (45/45), and a 3-column 44px-gap comparison grid (48/48) elsewhere — none are uniform card grids; each is a bespoke asymmetric pairing (e.g. 35/56) rather than equal-width columns, reinforcing the editorial pacing over dashboard density. Cards themselves are unusually flat: 0px radius, transparent or `#0E0E10` fill, padding 20px 22px (12px bottom variant) — structure comes from hairline dividers and whitespace, not container chrome. The marquee ticker is a horizontal scrolling-rail band, full-bleed edge-to-edge, breaking the container constraint entirely.

## Components
- **Navbar** — edge-to-edge square bar, 64px tall, 100% viewport width (0/0 inset), all four corners 0px (sharp full-bleed bar), sticky, fill `rgba(10, 10, 12, 0.4)` with `backdrop-filter: blur(24px)` (glassmorphism). Contains 9 items: logo mark + wordmark, a live price pill, a 3-item center nav cluster, two circular icon-glass utility buttons, and a lime pill CTA (`#C6F24E` fill, `#F4F4F1` text, radius 9999px, height 40px). This CTA is a nav utility, not the hero primary.
- **Button — primary (hero)** — the large lime pill under the headline: observed near-`#C6F24E` fill, dark text, full pill radius (~9999px), height ~44px, the single highest-contrast control on the first screen. This is the hero primary; the measured nav CTA shares its fill but is a separate, smaller instance.
- **Button — secondary outline (hero)** — dark-filled pill beside the primary, off-white text, same pill radius, no glass blur, lower visual weight.
- **Button — glass utility (secondary, measured)** — fill `#121215`, text `#A7A8A1`, radius 8px (slightly-rounded, not pill), height 34px, padding 8px 14px, border `1px solid lab(96.1271 -0.392228 1.44876 / 0.12)`; hover shifts text to `#C1E65B`. Used for tertiary link-style buttons (secondary links, "copy" chips) — never the hero focal point.
- **Button — prominent lime (page-end, measured)** — `#C6F24E` fill, `#0B0B0C` text, radius 9999px, height 40px, padding 10px 20px, hover → `#E4FFA3`; appears twice near the closing scene as the repeated Trade CTA.
- **Marquee ticker band** — full-bleed horizontal scrolling-rail directly beneath the hero, lime `#C6F24E`-toned fill, dark all-caps label text repeating in a loop; one per page, animated via `marquee` keyframe.
- **Stat/numeral band** — single oversized lime numeral (Archivo Black scale, far larger than headline-md) centered under an eyebrow/live-dot label, with a secondary smaller white numeral beneath and a 2-column stat pair (vault / liquidity) below a hairline divider; one instance, directly under the marquee.
- **Data-panel duo (chart + grid)** — two stacked cards on the right side of the mid-page split: top card is a line-chart panel (label row + mcap badge + timeframe tabs, lime line-chart on transparent/dark fill); bottom card is a grid/"rack" panel — a 4-row cluster of small squares in varying lime intensities signifying live status. Both `#0E0E10` fill, 0px radius, padding ~20px.
- **Alternating media/text row family (×3)** — the "three things" sequence: each row is text (eyebrow-numeral + heading + body) paired with one wide media block (illustration or bar-chart mini-panel) that bleeds to the row edge; rows alternate media-left/media-right; media covers roughly half the row width; separated by full-width hairlines; anatomy per measured spec is media-bleed + heading + body only, no CTA inside.
- **Closing illustrated scene band** — full-bleed cosmic illustration with an overlaid text/CTA cluster (headline with one lime line, primary + secondary buttons, two dark address-chip cards with copy buttons) anchored right; one instance closing the page before the footer.
- **Address/copy chip cards** — dark rounded rectangles (`#0E0E10`-family fill, small radius ~4-8px) holding a mono label, truncated address, and a lime pill "Copy" button (9999px, small height); appear ×2 in the hero and ×2 again in the closing band.
- **Footer** — transparent background, single row, 11 text links plus a small logo mark; no card chrome, sits directly on the page background.

## Graphics & Effects
Two soft radial glows sit behind the hero/upper sections rather than a full-frame gradient: `radial-gradient(1100px 620px at 20% 0px, rgba(198, 242, 78, 0.09), rgba(0, 0, 0, 0) 70%)` (17.6% of page area, upper-left hero zone) and `radial-gradient(700px 380px at 82% 78%, rgba(118, 185, 0, 0.08), rgba(0, 0, 0, 0) 70%)` (15.6% of page, lower-right) — both are faint lime/olive washes fading to transparent, not saturated backgrounds; the page stays black between and around them. A vertical scrim `linear-gradient(to top, lab(3.04095 0.11275 -0.413606 / 0.7) 4%, lab(3.04095 0.11275 -0.413606 / 0.3) 55%, rgba(0,0,0,0) 100%)` (16.4% of page) darkens the base of the closing illustrated scene for text legibility. A small angled panel fill `linear-gradient(to right bottom in oklab, rgb(27,29,21) 0%, rgb(11,11,12) 100%)` (1.9%) tints one data-panel corner. A 1px repeating lime line pattern `linear-gradient(rgba(198,242,78,0.05) 1px, rgba(0,0,0,0) 1px)` (1.9%) forms a faint grid texture over the rack/data panel. A scattered white dot star-field texture is visible across the black background throughout the page, reinforcing the "compute/cosmos" motif. Shadows are all lime-tinted glow rings at near-zero blur/spread (`rgba(198,242,78,0.44–0.447) 0px 0px 0px ~0.1-0.4px`, plus a soft `rgba(198,242,78,0.05) 0px 0px 0px 15.96px` ambient halo) — used as glow outlines on icons/badges, not drop shadows. Backdrop blur appears at `blur(24px)` (navbar glass) and `blur(8px)` (smaller glass chips).

## Motion
Color and background transitions run fast and linear-out: `0.15s cubic-bezier(0.4,0,0.2,1)` for hover color/fill shifts, `0.3s cubic-bezier(0.4,0,0.2,1)` for slower state changes, and general `all` transitions at `0.2s`/`0.3s cubic-bezier(0,0,0.2,1)` for layout-adjacent hovers. Named keyframes: `marquee` drives the continuous horizontal ticker loop; `bob` gives the illustrated mascot a slow idle float; `pulse-glow` and `fx-glow` breathe opacity/blur on lime glow elements (live dots, CTA halos); `scan` sweeps a highlight across data panels; `die-flicker` adds irregular flicker to small light/status elements. Motion overall is short, snappy, and glow-based rather than large spatial transforms — it animates light and loop, not position.

## Guardrails
- Never fill the hero background with a full-frame lime or green gradient — lime stays confined to two soft radial glows covering roughly a third of the page and to accent fills; the base must stay black.
- Do not round the navbar or its card families — they are sharp/square (0px); only buttons and small chips get radius.
- Do not substitute the 8px-radius glass utility button's values for the hero's pill-shaped primary CTA — they are different variants with different radii and roles.
- Keep body copy in Space Grotesk and reserve Archivo Black exclusively for display/headline/numeral roles; don't blend the two into one hierarchy level.
- Preserve the mono, uppercase, wide-tracked label voice for eyebrows/data tags — it is the system's instrument-panel signature and must not be swapped for the body sans.
- Keep card surfaces flat (0px radius, `#0E0E10` or transparent) — do not introduce rounded card chrome; structure comes from hairlines and spacing, not containers.