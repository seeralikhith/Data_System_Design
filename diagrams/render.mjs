// Renders every diagram source in diagrams/src to two SVG files in
// docs/assets/diagrams: NAME-light.svg and NAME-dark.svg.
//
// Each source is a small React component that returns an <svg>. Colours are
// written as theme tokens such as var(--cds-text-primary); this script swaps
// them for real colours, once for the light theme and once for the dark theme.
//
// Usage: npm run diagrams            (all diagrams)
//        npm run diagrams -- 04-1    (only names that start with 04-1)

import { readdir, readFile, writeFile, mkdir, rm } from 'node:fs/promises';
import { join, dirname, basename } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { transform } from 'esbuild';
import React from 'react';
import { renderToStaticMarkup } from 'react-dom/server';

const here = dirname(fileURLToPath(import.meta.url));
const srcDir = join(here, 'src');
const buildDir = join(here, '.build');
const outDir = join(here, '..', 'docs', 'assets', 'diagrams');

const palettes = {
  light: {
    'text-primary': '#1f1e1d',
    'text-secondary': '#5e5d59',
    'chart-axis': '#a9a79f',
    'chart-grid': '#e3e1da',
    'chart-reference-tint': '#eeede8',
    'chart-categorical-1': '#2a6fd6',
    'chart-categorical-2': '#e0683b',
    'chart-status-good': '#1e9e3a',
    'chart-status-warning': '#c98a0b',
    'chart-status-critical': '#d13b3b',
  },
  dark: {
    'text-primary': '#ecebe7',
    'text-secondary': '#a9a7a0',
    'chart-axis': '#76746d',
    'chart-grid': '#3a3936',
    'chart-reference-tint': '#2b2a27',
    'chart-categorical-1': '#5b9bf2',
    'chart-categorical-2': '#f08c5f',
    'chart-status-good': '#4cc566',
    'chart-status-warning': '#e8b23e',
    'chart-status-critical': '#f06a6a',
  },
};

const fontFamily = "Inter, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif";

function themed(svg, palette) {
  return svg.replace(/var\(--cds-([a-z0-9-]+)\)/g, (match, name) => {
    if (!(name in palette)) throw new Error(`Unknown colour token: ${match}`);
    return palette[name];
  });
}

function tidy(svg) {
  // An explicit width and height give the <img> a natural size; CSS scales it down on small screens.
  const viewBox = svg.match(/viewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"/);
  if (!viewBox) throw new Error('Every diagram needs a viewBox="0 0 W H" on its <svg>');
  const [, width, height] = viewBox;
  return svg
    .replace(/ data-claude-[a-z-]+="[^"]*"/g, '')
    .replace(
      /^<svg /,
      `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" font-family="${fontFamily}" `,
    );
}

async function main() {
  const filter = process.argv[2] ?? '';
  const files = (await readdir(srcDir)).filter((f) => f.endsWith('.jsx') && f.startsWith(filter)).sort();
  if (files.length === 0) throw new Error(`No diagram sources match "${filter}"`);
  await mkdir(buildDir, { recursive: true });
  await mkdir(outDir, { recursive: true });

  for (const file of files) {
    const name = basename(file, '.jsx');
    const source = await readFile(join(srcDir, file), 'utf8');
    const { code } = await transform(`import React from 'react';\n${source}`, {
      loader: 'jsx',
      format: 'esm',
      jsxFactory: 'React.createElement',
      jsxFragment: 'React.Fragment',
    });
    const modulePath = join(buildDir, `${name}.mjs`);
    await writeFile(modulePath, code);
    const { default: Diagram } = await import(`${pathToFileURL(modulePath).href}?t=${Date.now()}`);
    const svg = tidy(renderToStaticMarkup(React.createElement(Diagram)));
    for (const [theme, palette] of Object.entries(palettes)) {
      await writeFile(join(outDir, `${name}-${theme}.svg`), `${themed(svg, palette)}\n`);
    }
    console.log(`rendered ${name}`);
  }
  await rm(buildDir, { recursive: true, force: true });
  console.log(`${files.length} diagrams rendered to docs/assets/diagrams`);
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
