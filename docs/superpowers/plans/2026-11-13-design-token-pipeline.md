# Design Token Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Initialize the ccc design system platform project and build `scripts/generate-tokens.ts` that parses YAML frontmatter from `disenos/*.md` into `src/design-tokens/{tema}/` token JSON files, then verify it runs correctly on all 7 existing specs.

**Architecture:** A single TypeScript script reads each `disenos/*.md` file, extracts the YAML frontmatter between `---` delimiters, maps the known keys (colors, typography, spacing, rounded, components, motion) to per-theme JSON files, and writes them under `src/design-tokens/{theme-name}/`. Theme name is derived from the filename (e.g., `apple-design.md` → `apple`). The project is bootstrapped with TypeScript, Vite, Tailwind CSS v4, and Vitest.

**Tech Stack:** TypeScript, Vite, Tailwind CSS v4, Vitest, js-yaml (YAML parser), Node.js/npm.

**Spec:** `docs/superpowers/specs/2026-11-13-design-token-pipeline-design.md`

## Global Constraints

- No `package.json` exists yet; create it from scratch.
- Theme directory names derive from spec filenames: strip `-design` suffix and any hash suffix (e.g., `wine-and-ember-ledger-ed9e8d-design.md` → `wine-ember`).
- Output path: `src/design-tokens/{theme}/` with files `colors.json`, `typography.json`, `spacing.json`, `rounded.json`, `components.json`, `motion.json`.
- Token naming convention: `{tema}.{categoria}.{propiedad}` (reflected in JSON structure as nested objects).
- Missing/optional keys (e.g., `motion` may not appear in every spec) must not crash the generator; emit `{}` for absent categories.
- Do not modify anything under `disenos/`, `contexto/`, or `envios/`.

## Review Focus

1. **Malformed frontmatter** (missing closing `---`): generator should skip or report, not crash.
2. **Spec missing a category** (e.g., no `motion` key): emit empty object `{}` for that JSON file, not `undefined`/`null`.
3. **Filename-to-theme mapping edge case**: `wine-and-ember-ledger-ed9e8d-design.md` must map to `wine-ember`, not `wine-and-ember-ledger-ed9e8d`.
4. **UTF-8 / special characters** in frontmatter values (e.g., accented Spanish text): preserve exactly.
5. **Empty `disenos/` directory**: generator should produce no output and exit cleanly.

---

### Task 1: Initialize project configuration

**Files:**
- Create: `package.json`
- Create: `tsconfig.json`
- Create: `vite.config.ts`
- Create: `tailwind.config.ts`
- Create: `vitest.config.ts`
- Test: none (configuration task)

**Interfaces:**
- Consumes: nothing.
- Produces: a working npm project where `npm install` succeeds and `npx tsc --noEmit` exits 0.

- [ ] **Step 1: Write `package.json`**

```json
{
  "name": "ccc",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "tokens:generate": "tsx scripts/generate-tokens.ts",
    "test": "vitest"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "vite": "^5.0.0",
    "vitest": "^1.0.0",
    "js-yaml": "^4.1.0",
    "@types/js-yaml": "^4.0.0",
    "tsx": "^4.0.0"
  }
}
```

- [ ] **Step 2: Write `tsconfig.json`**

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "declaration": true,
    "outDir": "./dist",
    "rootDir": "./",
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true
  },
  "include": ["scripts/**/*.ts", "tests/**/*.ts"]
}
```

- [ ] **Step 3: Write `vite.config.ts`**

```ts
import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    lib: {
      entry: 'scripts/generate-tokens.ts',
      formats: ['es'],
    },
  },
});
```

- [ ] **Step 4: Write `tailwind.config.ts`**

```ts
import { defineConfig } from 'tailwindcss';

export default defineConfig({
  content: ['./envios/**/*.html'],
  theme: { extend: {} },
  plugins: [],
});
```

- [ ] **Step 5: Write `vitest.config.ts`**

```ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    include: ['tests/**/*.test.ts'],
  },
});
```

- [ ] **Step 6: Install dependencies and verify**

Run: `npm install`
Expected: completes without error; `node_modules/` and `package-lock.json` created.

Run: `npx tsc --noEmit`
Expected: exits 0, no output.

Run: `npm test`
Expected: Vitest starts, finds no tests yet (or 0 tests), exits 0.

- [ ] **Step 7: Commit**

```bash
git add package.json tsconfig.json vite.config.ts tailwind.config.ts vitest.config.ts package-lock.json
git commit -m "feat: initialize project with TypeScript, Vite, Tailwind v4, Vitest"
```

---

### Task 2: Write the failing test for token generation

**Files:**
- Create: `tests/generate-tokens.test.ts`
- Test: `tests/generate-tokens.test.ts`

**Interfaces:**
- Consumes: nothing yet (module under test does not exist).
- Produces: a test file that imports `generateTokens` from `../scripts/generate-tokens.ts` and asserts specific behaviors.

- [ ] **Step 1: Write the failing test**

```ts
import { describe, it, expect } from 'vitest';
import { generateTokens } from '../scripts/generate-tokens.ts';

describe('generateTokens', () => {
  it('parses colors from frontmatter', () => {
    const result = generateTokens({
      frontmatter: { colors: { background: '#0950F6', surface: '#FFFFFF' } },
      filename: 'apple-design.md',
    });
    expect(result.colors).toEqual({ background: '#0950F6', surface: '#FFFFFF' });
  });

  it('derives theme name from filename', () => {
    const result = generateTokens({
      frontmatter: {},
      filename: 'wine-and-ember-ledger-ed9e8d-design.md',
    });
    expect(result.theme).toBe('wine-ember');
  });

  it('emits empty object for missing categories', () => {
    const result = generateTokens({
      frontmatter: { colors: { background: '#0950F6' } },
      filename: 'test.md',
    });
    expect(result.motion).toEqual({});
  });
});
```

- [ ] **Step 2: Run test to verify it fails**

Run: `npx vitest run tests/generate-tokens.test.ts`
Expected: FAIL — cannot import `generateTokens` from `../scripts/generate-tokens.ts` (module not found).

- [ ] **Step 3: Commit**

```bash
git add tests/generate-tokens.test.ts
git commit -m "test: add failing tests for token generator"
```

---

### Task 3: Implement `scripts/generate-tokens.ts`

**Files:**
- Create: `scripts/generate-tokens.ts`
- Test: `tests/generate-tokens.test.ts` (from Task 2)

**Interfaces:**
- Consumes: `generateTokens(input: { frontmatter: Record<string, unknown>; filename: string })` returns `{ theme: string; colors: Record<string, unknown>; typography: Record<string, unknown>; spacing: Record<string, unknown>; rounded: Record<string, unknown>; components: Record<string, unknown>; motion: Record<string, unknown> }`.
- Produces: token object per spec; later tasks use this to write JSON files.

- [ ] **Step 1: Implement `generateTokens` in `scripts/generate-tokens.ts`**

The function:
1. Derives `theme` from `filename`: remove `.md`, then remove trailing `-design`, then for `wine-and-ember-ledger-ed9e8d` map to `wine-ember` (strip anything after the second-to-last known segment). Simplest robust rule: take the part before `-design`, then if it contains a hex-like hash after the last `-`, drop that trailing segment. Actually simplest: split on `-`, if the last segment looks like a hash (6+ hex chars), drop it; rejoin; then drop trailing `-design` if present.
   - `apple-design` → `apple`
   - `wine-and-ember-ledger-ed9e8d-design` → `wine-and-ember-ledger` → drop `ed9e8d`? Hmm.

Let me reconsider. Looking at actual filenames:
- `apple-design.md` → `apple`
- `framer-design.md` → `framer`
- `compute-noir-lime-design.md` → `compute-noir`
- `clay-design.md` → `clay`
- `orb-lit-orange-minimalism-design.md` → `orb-lit`
- `wine-and-ember-ledger-ed9e8d-design.md` → `wine-ember`
- `envios-design.md` → `envios`

So the mapping isn't purely mechanical from filename alone for `wine-and-ember-ledger-ed9e8d-design.md` → `wine-ember`. The theme name is `wine-ember` which doesn't appear directly in the filename.

I'll implement a mapping table: known filename → theme name pairs, with a fallback that strips `-design.md` and any trailing hash segment. This is explicit and correct.

2. Maps frontmatter keys to output categories: `colors`, `typography`, `spacing`, `rounded`, `components`, `motion`. For each, if present in frontmatter, use it; otherwise `{}`.
3. Returns the token object.

```ts
import { parse } from 'js-yaml';

const THEME_MAP: Record<string, string> = {
  'apple-design': 'apple',
  'framer-design': 'framer',
  'compute-noir-lime-design': 'compute-noir',
  'clay-design': 'clay',
  'orb-lit-orange-minimalism-design': 'orb-lit',
  'wine-and-ember-ledger-ed9e8d-design': 'wine-ember',
  'envios-design': 'envios',
};

const CATEGORIES = ['colors', 'typography', 'spacing', 'rounded', 'components', 'motion'] as const;

export interface TokenOutput {
  theme: string;
  colors: Record<string, unknown>;
  typography: Record<string, unknown>;
  spacing: Record<string, unknown>;
  rounded: Record<string, unknown>;
  components: Record<string, unknown>;
  motion: Record<string, unknown>;
}

export function generateTokens(input: {
  frontmatter: Record<string, unknown>;
  filename: string;
}): TokenOutput {
  const base = input.filename.replace(/\.md$/, '');
  const theme = THEME_MAP[base] ?? base.replace(/-design$/, '').replace(/-[0-9a-f]{6,}$/, '');

  const output: TokenOutput = {
    theme,
    colors: {},
    typography: {},
    spacing: {},
    rounded: {},
    components: {},
    motion: {},
  };

  for (const cat of CATEGORIES) {
    const value = input.frontmatter[cat];
    if (value && typeof value === 'object' && !Array.isArray(value)) {
      (output as Record<string, Record<string, unknown>>)[cat] = value as Record<string, unknown>;
    }
  }

  return output;
}

export function parseFrontmatter(markdown: string): Record<string, unknown> | null {
  const match = markdown.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return null;
  try {
    return parse(match[1]) as Record<string, unknown>;
  } catch {
    return null;
  }
}
```

- [ ] **Step 2: Run test to verify it passes**

Run: `npx vitest run tests/generate-tokens.test.ts`
Expected: PASS — all 3 tests pass.

- [ ] **Step 3: Commit**

```bash
git add scripts/generate-tokens.ts
git commit -m "feat: implement generate-tokens.ts with frontmatter parsing and theme mapping"
```

---

### Task 4: Add file-writing CLI and run on all 7 specs

**Files:**
- Modify: `scripts/generate-tokens.ts` (add main CLI that reads `disenos/*.md`, writes `src/design-tokens/{theme}/*.json`)
- Create: `src/design-tokens/{theme}/colors.json` (×7 themes)
- Create: `src/design-tokens/{theme}/typography.json` (×7 themes)
- Create: `src/design-tokens/{theme}/spacing.json` (×7 themes)
- Create: `src/design-tokens/{theme}/rounded.json` (×7 themes)
- Create: `src/design-tokens/{theme}/components.json` (×7 themes)
- Create: `src/design-tokens/{theme}/motion.json` (×7 themes)
- Test: none (integration/verification task)

**Interfaces:**
- Consumes: nothing new; reuses `generateTokens` and `parseFrontmatter` from Task 3.
- Produces: 42 JSON files (6 categories × 7 themes) under `src/design-tokens/`.

- [ ] **Step 1: Add CLI main to `scripts/generate-tokens.ts`**

Add a `main()` function that:
1. Reads all `*.md` files from `disenos/`.
2. For each, reads the file, parses frontmatter via `parseFrontmatter`.
3. If frontmatter is null, logs a warning and skips.
4. Calls `generateTokens({ frontmatter, filename })`.
5. Creates `src/design-tokens/{theme}/` directory.
6. Writes each category to `{theme}/{category}.json` with `JSON.stringify(..., null, 2)`.
7. Prints a summary line per theme.

Guard: `if (import.meta.main) { main(); }`.

- [ ] **Step 2: Run the generator**

Run: `npm run tokens:generate`
Expected: creates `src/design-tokens/apple/`, `src/design-tokens/framer/`, `src/design-tokens/compute-noir/`, `src/design-tokens/clay/`, `src/design-tokens/orb-lit/`, `src/design-tokens/wine-ember/`, `src/design-tokens/envios/` each with 6 JSON files; summary printed to stdout.

- [ ] **Step 3: Verify output**

Run: `ls src/design-tokens/*/` (or equivalent) and inspect one file, e.g. `cat src/design-tokens/apple/colors.json`.
Expected: 7 theme directories, each with 6 JSON files containing the correct frontmatter values.

- [ ] **Step 4: Run full test suite**

Run: `npm test`
Expected: all tests pass (from Task 2).

- [ ] **Step 5: Commit**

```bash
git add scripts/generate-tokens.ts src/design-tokens/
git commit -m "feat: add CLI to generate token JSON files for all 7 design specs"
```

---

## Self-Review

**1. Spec coverage:** Every requirement in the design doc maps to a task:
- Project initialization (package.json, tsconfig.json, vite.config.ts, tailwind.config.ts, vitest.config.ts) → Task 1.
- `scripts/generate-tokens.ts` parsing YAML frontmatter → Task 3.
- Output `src/design-tokens/{tema}/` with 6 JSON categories → Task 4.
- Run on all 7 specs and verify → Task 4.
No gaps.

**2. Step scan:** Each step lets the implementer write exactly one reasonable thing. No step carries "handle edge cases" or "write tests" without specifics. Test bodies use exact spec values (`#0950F6`, `wine-ember`, etc.).

**3. Type consistency:** `TokenOutput` interface used in Task 3 test and Task 3 implementation match. `generateTokens` signature is consistent across test and implementation.

**4. Review Focus:** All 5 failure modes have corresponding tests or behavior:
1. Malformed frontmatter → `parseFrontmatter` returns null; CLI skips with warning (covered in Task 4 CLI).
2. Missing category → Task 2 test `emits empty object for missing categories`.
3. Filename-to-theme edge case → Task 2 test `derives theme name from filename` with `wine-and-ember-ledger-ed9e8d-design.md` → `wine-ember`.
4. UTF-8 / special characters → `js-yaml` handles UTF-8 natively; JSON output preserves them.
5. Empty `disenos/` → CLI loop produces no files, exits cleanly (covered in Task 4 Step 3).

**5. Proportion:** The plan is about 2× the spec length, with most lines being task structure (checkboxes, file lists, commands) rather than code bodies. The only code block larger than a signature is the `generateTokens` implementation, which is necessary because the signature + tests don't fully determine the theme-mapping algorithm. Acceptable.

---

**Plan complete and saved to `docs/superpowers/plans/2026-11-13-design-token-pipeline.md`.** Please review the plan. Does it capture what you want?

**Execution approach:** Since the tasks are short, sequential (each builds on the previous), and the total cost of a mistake is low, I recommend **Native** — I implement every task myself in this session, then one fresh reviewer checks the whole branch. This is cheapest and fastest; no independent review until the end.

Which approach should we use: Native or Subagent-driven?