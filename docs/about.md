<!-- nav -->
[Home](../README.md) · [Reference](clover-engine-reference.md) · [Supervisor](supervisor.md) · [File formats](file-formats.md) · [Scene components](scene-components.md) · [Lua API](api/README.md) · [Boot music](boot-music.md) · [Error C8](c8-error.md) · [Family differences](family-differences.md) · [Lua toolchain](lua-toolchain.md) · [About](about.md)

---

# About these notes

Reverse engineering notes on the console UI engine, `ReedPlayer-Clover`, and its supervisor `clover-mcp`. They are
for understanding the engine and the format of its UI package. They contain no pseudocode and no binaries. Status: work in progress.

## Method

- Binaries: `/usr/bin/ReedPlayer-Clover` and `/usr/bin/clover-mcp` from the stock firmware images (`.hsqs`).
- Decompilation: REA 6.8.0 with Ghidra 12.1.4 in Docker (`ghcr.io/alexmi256/rea-agent-ghidra`), offline.
  Function names are mostly `FUN_xxxx` (about 30% carry a name): each claim cites a function address of the SNES EUR
  2.0.14 build.
- Lua scripts: decompiled with luajit-decompiler-v2 (the scripts are stripped LuaJIT 2.0 bytecode, header
  `1b 4c 4a 01 02`).
- UI package files: the stock `resources/` folders of each firmware family, from extracted copies (the exact
  versions of the NES, HVC and Shonen copies were not re-checked against the images the binaries came from).
- Open-source release: Nintendo's published sources for the consoles ([Nintendo Open Source Software](https://support.nintendo.com/jp/oss/index.html)),
  used for the LuaJIT source and for the names and versions of the bundled libraries (SoLoud 111, LZ4, SDL2). It does not
  contain the supervisor or the engine.
- Lua API: the binding tables were read from the engines; argument and result types come from matching the small
  helper functions each binding calls. The NES build inlines its result pushes, so only `VideoComponent` was typed there
  (by hand); the other NES-only methods have an argument count only.
- Firmware versions: sneseur 2.0.14, nes 1.0.7, hvcj-shonen 3.0.1 decompiled; snesusa, shvc, hvc extracted only.

## Confidence

Each page separates what the code shows from what is inferred or untested. Nothing here was run on a console.
In the Lua API pages, a method summary is derived from its name only for getters and setters; "Not described (name only)"
means nothing beyond the name is known, and a **Note** was checked in the code or in the stock scripts. About 30 of 436
methods have a note.
