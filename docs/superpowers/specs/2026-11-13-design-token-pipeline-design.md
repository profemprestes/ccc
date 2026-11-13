# Diseño: pipeline de tokens de diseño

**Fecha:** 2026-11-13  
**Autor:** Claude Code (asistente)  
**Estado:** Aprobado por el usuario ("procede")

## Intent y por qué

El repositorio `ccc` contiene 7 especificaciones de sistemas de diseño en `disenos/*.md` (frontmatter YAML + prosa), una configuración Tailwind v4 en `contexto/globals.css` y 15 páginas HTML estáticas en `envios/`. Lo que falta es la plataforma de diseño sistema descrita en `CLAUDE.md`: generación de tokens, proveedor de temas, componentes con variantes, guardrails y motion.

El pipeline de tokens es la cimentación: sin tokens no hay contexto de tema que consumir, nada contra lo que validar variantes de componentes, y nada que los guardrails puedan chequear. Por eso es el primer entregable concreto.

## Objetivos

1. Inicializar el proyecto con `package.json`, `tsconfig.json`, `vite.config.ts`, `tailwind.config.ts`, `vitest.config.ts` (TypeScript + Vite + Vitest).
2. Crear `scripts/generate-tokens.ts` que parse el frontmatter YAML de `disenos/*.md` y emite `src/design-tokens/{tema}/` con `colors.json`, `typography.json`, `spacing.json`, `rounded.json`, `components.json`, `motion.json`.
3. Ejecutar el generador sobre las 7 especificaciones existentes y verificar que los archivos de token se produzcan correctamente.

## No-objetivos (por ahora)

- `src/themes/` (ThemeProvider, useTheme, theme-registry)
- `src/components/` (Button, Card, Navbar, Input con variantes)
- `src/guards/` y `scripts/validate-guards.ts`
- `src/motion/` como sistema consumible por componentes (aunque `motion.json` se genere)
- Storybook, tests de integración, visual regression

## Restricciones

- No existe `package.json` ni tooling de build: hay que crear todo desde cero.
- El frontmatter YAML de `disenos/*.md` sigue el schema `superdesign-alpha`.
- Los nombres de token siguen la convención `{tema}.{categoria}.{propiedad}`.
- Los archivos de salida van en `src/design-tokens/{tema}/`.
- No se debe romper nada de lo que ya existe (`disenos/`, `contexto/`, `envios/`).

## Enfoque elegido (aprobado por el usuario)

**Un solo enfoque sensible:** inicializar el proyecto y construir `scripts/generate-tokens.ts` primero. Las alternativas (componentes primero, temas primero, todo de una vez) se descartan porque dependen de los tokens y construirían sobre supuestos no verificados sobre la forma del token.

## Partes del cómo ya decididas

- Gestor de paquetes: npm (el repo ya usa `npx --yes hyperframes@0.9.41` en `diseno-envios/package.json`, así que npm está disponible).
- Lenguaje: TypeScript.
- Runner de build/dev: Vite.
- Framework de estilos: Tailwind CSS v4 (coherente con `contexto/globals.css`).
- Tests: Vitest.
- Parser de YAML: `js-yaml` (dependencia ligera y estándar).
- Escritura de JSON de salida: `fs.writeFileSync` con `JSON.stringify(..., null, 2)`.

## Qué le queda al builder

- Ejecutar `npm install` para instalar dependencias.
- Ejecutar `npx tsc --noEmit` o similar para tipar.
- Ejecutar `npm run tokens:generate` (script definido en `package.json`) y revisar la salida en `src/design-tokens/`.
- Correr `npm test` para confirmar que Vitest pasa.
