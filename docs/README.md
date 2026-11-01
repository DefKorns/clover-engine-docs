# Clover engine notes (SNES, NES, Shonen)

Reverse engineering notes on the console UI engine, `ReedPlayer-Clover`, and its supervisor `clover-mcp`. They are
for understanding the theme format. They contain no pseudocode and no binaries. Status: work in progress, kept on disk
only.

## Start here

`clover-engine-reference.md` is the complete reference: architecture, supervisor, file formats, components, Lua layer,
subsystems and family differences. The pages below are the topic details it condenses.

## Pages

- `file-formats.md`: `init.json`, `dependencies.json`, nodes, textures, animation tracks and strings, with the `engineFormat` of each family.
- `scene-components.md`: the keys each component reads from a `.scn` file.
- `lua-api.md` and `lua-api.json`: every Lua class and method with its signature and the families that bind it; the
  *API explorer* page of `index.html` is the interactive version.
- `family-differences.md`: what changes between SNES, NES and Shonen.
- `boot-music.md`: how `bgm_boot` plays and how it can be silenced.
- `supervisor.md`: the supervisor `clover-mcp`: state machine, settings, game scan, splash and error screens.
- `c8-error.md`: what the C8 error screen is and when it appears.
- `lua-toolchain.md`: which LuaJIT reproduces the console's bytecode.

## Method

- Binaries: `/usr/bin/ReedPlayer-Clover` and `/usr/bin/clover-mcp` from the stock firmware images (`.hsqs`).
- Decompilation: REA 6.8.0 with Ghidra 12.1.4 in Docker (`ghcr.io/alexmi256/rea-agent-ghidra`), offline.
  Function names are mostly `FUN_xxxx` (about 30% carry a name): each claim cites a function address of the SNES EUR
  2.0.14 build.
- Lua scripts: decompiled with luajit-decompiler-v2 (the scripts are stripped LuaJIT 2.0 bytecode, header
  `1b 4c 4a 01 02`).
- Firmware versions: sneseur 2.0.14, nes 1.0.7, hvcj-shonen 3.0.1 decompiled; snesusa, shvc, hvc extracted only.

## Confidence

Each page separates what the code shows from what is inferred or untested. Nothing here was run on a console.
