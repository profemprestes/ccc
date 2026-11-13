import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    lib: {
      entry: 'scripts/generate-tokens.ts',
      formats: ['es'],
    },
  },
});
