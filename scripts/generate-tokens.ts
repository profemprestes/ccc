import { load } from 'js-yaml';

export function parseFrontmatter(content: string): Record<string, unknown> | null {
  const frontmatterRegex = /^---\n([\s\S]*?)\n---/;
  const match = content.match(frontmatterRegex);

  if (!match) {
    return null;
  }

  try {
    const parsed = load(match[1]);
    if (parsed && typeof parsed === 'object' && !Array.isArray(parsed)) {
      return parsed as Record<string, unknown>;
    }
    return null;
  } catch {
    return null;
  }
}

export function generateTokens(
  theme: string,
  frontmatter: Record<string, unknown>
): Record<string, Record<string, unknown>> {
  const categories = [
    'colors',
    'typography',
    'spacing',
    'rounded',
    'components',
    'motion',
  ] as const;

  const result: Record<string, Record<string, unknown>> = {
    [theme]: {},
  };

  for (const category of categories) {
    const value = frontmatter[category];
    if (value && typeof value === 'object' && !Array.isArray(value)) {
      result[theme][category] = value;
    } else if (Array.isArray(value)) {
      result[theme][category] = value;
    } else {
      result[theme][category] = {};
    }
  }

  return result;
}