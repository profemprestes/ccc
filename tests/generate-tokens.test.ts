import { describe, it, expect, beforeEach } from 'vitest';
import { parseFrontmatter, generateTokens } from '../scripts/generate-tokens.ts';

describe('parseFrontmatter', () => {
  it('extracts valid YAML between --- delimiters', () => {
    const content = `---\ncolors:\n  primary: '#0071E3'\ntypography:\n  fontFamily: 'SF Pro'\n---\n\n# Content here`;

    const result = parseFrontmatter(content);

    expect(result).not.toBeNull();
    expect(result).toEqual({
      colors: { primary: '#0071E3' },
      typography: { fontFamily: 'SF Pro' },
    });
  });

  it('returns null on malformed frontmatter', () => {
    const noDelimiters = 'colors:\n  primary: "#0071E3"\n\n# Content';
    const unclosedDelimiters = '---\ncolors:\n  primary: "#0071E3"\n\n# Content';
    const invalidYaml = `---\ncolors:\n  primary: '#0071E3'\n  invalid: [\n---\n\n# Content`;

    expect(parseFrontmatter(noDelimiters)).toBeNull();
    expect(parseFrontmatter(unclosedDelimiters)).toBeNull();
    expect(parseFrontmatter(invalidYaml)).toBeNull();
  });
});

describe('generateTokens', () => {
  it('maps 6 categories to nested JSON {theme}.{category}.{property}', () => {
    const frontmatter = {
      colors: { blue: '#0071E3', gray: '#F5F5F7' },
      typography: { display: 'SF Pro', body: 'SF Pro' },
      spacing: { base: 4, scale: [0, 4, 8, 16, 24, 32, 48, 64] },
      rounded: { none: 0, sm: 4, md: 8, lg: 12, full: 9999 },
      components: {
        button: { primary: { background: 'blue', radius: 'none' } },
        card: { default: { padding: 'base', radius: 'sm' } },
      },
      motion: {
        curves: { default: 'cubic-bezier(0.22, 0.8, 0.24, 1)' },
        durations: { entrance: 700, hover: 250 },
        keyframes: { fadeIn: 'fadeIn 0.3s ease-out' },
      },
    };

    const result = generateTokens('apple', frontmatter);

    expect(result).toEqual({
      apple: {
        colors: { blue: '#0071E3', gray: '#F5F5F7' },
        typography: { display: 'SF Pro', body: 'SF Pro' },
        spacing: { base: 4, scale: [0, 4, 8, 16, 24, 32, 48, 64] },
        rounded: { none: 0, sm: 4, md: 8, lg: 12, full: 9999 },
        components: {
          button: { primary: { background: 'blue', radius: 'none' } },
          card: { default: { padding: 'base', radius: 'sm' } },
        },
        motion: {
          curves: { default: 'cubic-bezier(0.22, 0.8, 0.24, 1)' },
          durations: { entrance: 700, hover: 250 },
          keyframes: { fadeIn: 'fadeIn 0.3s ease-out' },
        },
      },
    });
  });

  it('emits empty object for missing optional categories', () => {
    const frontmatter = {
      colors: { primary: '#0071E3' },
      // typography, spacing, rounded, components, motion are missing
    };

    const result = generateTokens('apple', frontmatter);

    expect(result.apple.colors).toEqual({ primary: '#0071E3' });
    expect(result.apple.typography).toEqual({});
    expect(result.apple.spacing).toEqual({});
    expect(result.apple.rounded).toEqual({});
    expect(result.apple.components).toEqual({});
    expect(result.apple.motion).toEqual({});
  });
});