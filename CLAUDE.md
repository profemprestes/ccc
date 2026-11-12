# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **multi-theme design system** repository containing 6 distinct visual languages (design systems) specified in the `disenos/` directory. Each system is a complete, self-contained design language with its own color palette, typography, spacing, components, motion curves, and guardrails.

**Purpose**: Build a design system platform that can serve all 6 visual languages, enabling theme switching, component variants per theme, and strict adherence to each system's guardrails.

## Design Systems Reference

Located in `disenos/` — each `.md` file follows the `superdesign-alpha` schema with YAML frontmatter + prose documentation:

| System | Mode | Accent | Display Font | Container | Key Characteristic |
|--------|------|--------|--------------|-----------|-------------------|
| **Apple** | Light | Blue `#0071E3` | SF Pro | 1024px | Flat 0px radius panels, retail minimalism |
| **Framer (Void-canvas)** | Dark | Electric Blue `#0099FF` | GT Walsheim / Inter / Input Mono | 1200px | Glass tiles, bento/masonry grids, IDE-like |
| **Compute-noir** | Dark | Acid Lime `#C6F24E` | Archivo Black / Space Grotesk / JetBrains Mono | 1240px | Terminal/trading aesthetic, hairline dividers |
| **Clay** | Light | Chartreuse Lime `#EEF773`/`#CBD810` | Roobertvf / Phosphor | 1280px | 3D clay illustrations, pastel section bands |
| **Orb-lit** | Light | Orange `#F75D00` | Formular / Formular Mono | 1440px | Rendered sphere hero, horizontal scroll rails |
| **Wine & Ember** | Light (paper) / Dark (wine bands) | Ember Orange `#F7972C` | Epilogue (760-780 wt) | 1260px | Alternating light/dark bands, editorial rhythm |

Each system defines: `colors`, `typography`, `spacing`, `rounded`, `components` (buttons, cards, navbars), `graphics`, `motion` (cubic-bezier curves, keyframes), and `guardrails` (strict do-not rules).

## Development Commands

*Assumed modern web stack: TypeScript + React + Vite + Tailwind CSS + Storybook + Vitest*

```bash
# Install dependencies
npm install

# Development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run tests
npm run test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage

# Type checking
npm run typecheck

# Lint
npm run lint

# Format code
npm run format

# Storybook
npm run storybook

# Build Storybook
npm run build-storybook

# Generate design tokens (from disenos/ specs)
npm run tokens:generate

# Validate tokens against guardrails
npm run tokens:validate
```

## Architecture Notes

### High-Level Structure

```
ccc/
├── disenos/                    # Source design specifications (6 .md files)
├── src/
│   ├── design-tokens/          # Generated token files (JSON/CSS/TS)
│   │   ├── apple/
│   │   ├── framer/
│   │   ├── compute-noir/
│   │   ├── clay/
│   │   ├── orb-lit/
│   │   └── wine-ember/
│   ├── themes/                 # Theme configuration & providers
│   │   ├── ThemeProvider.tsx
│   │   ├── useTheme.ts
│   │   └── theme-registry.ts
│   ├── components/             # Base components with theme variants
│   │   ├── Button/
│   │   ├── Card/
│   │   ├── Navbar/
│   │   ├── Input/
│   │   └── ...
│   ├── guards/                 # Guardrail validation per theme
│   │   ├── apple-guards.ts
│   │   ├── framer-guards.ts
│   │   └── ...
│   ├── motion/                 # Motion curves & keyframes per theme
│   │   ├── curves.ts
│   │   └── keyframes.ts
│   └── utils/
│       ├── token-transformer.ts
│       └── theme-utils.ts
├── stories/                    # Storybook stories per component per theme
├── tests/
│   ├── unit/
│   ├── integration/
│   └── visual/                 # Visual regression tests
├── scripts/
│   ├── generate-tokens.ts      # Parses disenos/ → design-tokens/
│   └── validate-guards.ts
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.ts
├── .storybook/
└── vitest.config.ts
```

### Design Token Pipeline

1. **Source**: `disenos/*.md` (YAML frontmatter = machine-readable tokens)
2. **Transform**: `scripts/generate-tokens.ts` parses frontmatter → structured JSON/TS/CSS
3. **Output**: `src/design-tokens/{theme}/` — `colors.json`, `typography.json`, `spacing.json`, `rounded.json`, `components.json`, `motion.json`
4. **Consume**: Components import tokens via theme context; Tailwind config extends with theme tokens

### Component Architecture

- **Base components** accept a `variant` prop that maps to theme-specific specs
- **Theme context** provides current theme's tokens, components, guards, motion
- **Guardrails** enforced at build-time (token validation) and runtime (dev warnings)
- **Each theme** can have unique component anatomy (e.g., Wine & Ember's alternating bands, Orb-lit's horizontal scroll rail)

### Theme Switching

- `ThemeProvider` wraps app, exposes `useTheme()` hook
- Theme change = swap token context + component variant defaults
- No CSS-in-JS — uses CSS custom properties + Tailwind utility classes
- Persisted in `localStorage` + respects `prefers-color-scheme` where applicable

### Motion System

Each theme defines:
- **Transition curves**: cubic-bezier strings (e.g., Framer: `cubic-bezier(0.22, 0.8, 0.24, 1)`)
- **Durations**: entrance (0.7-0.75s), hover (0.25-0.28s), etc.
- **Keyframes**: named animations (spin, marquee, pulse, bob, scan, etc.)
- Implemented as CSS `@keyframes` + utility classes per theme

### Guardrails Enforcement

Two layers:
1. **Build-time**: `scripts/validate-guards.ts` checks tokens don't violate rules (e.g., "never fill full page with wine gradient", "keep navbar 0px radius")
2. **Dev-time**: Runtime warnings in Storybook/Storybook controls when guardrails breached

## Key Conventions

- **Token naming**: `{theme}.{category}.{property}` — e.g., `apple.colors.blue`, `wine-ember.typography.display-lg.fontSize`
- **Component variants**: `{theme}-{variant}` — e.g., `button-apple-primary`, `card-framer-glass-tile`
- **CSS custom properties**: `--{theme}-{category}-{property}` — scoped to `[data-theme="{theme}"]`
- **No shared accent usage**: Each theme's accent is strictly rationed per its guardrails
- **Typography isolation**: Display vs body font families never mixed across themes

## Adding a New Design System

1. Add `.md` spec to `disenos/` following `superdesign-alpha` schema
2. Run `npm run tokens:generate`
3. Add theme entry to `src/themes/theme-registry.ts`
4. Create guard file in `src/guards/`
5. Add motion config in `src/motion/`
6. Document component variants in Storybook

## Testing Strategy

- **Unit**: Token generation, theme context, guard validation
- **Integration**: Theme switching, component variant resolution
- **Visual**: Storybook + Chromatic / Playwright for per-theme visual regression
- **Guardrail**: Automated checks in CI for each theme's rules

---

*This CLAUDE.md was created during project initialization and updated after analyzing all 6 design specifications in `disenos/`. Update as the codebase evolves.*