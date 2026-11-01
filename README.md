# Clover engine documentation

Reverse engineering notes on the console UI stack of the SNES Classic, NES Classic, Famicom Mini and the Shonen Jump
Famicom Mini: the supervisor `clover-mcp`, the engine `ReedPlayer-Clover`, the UI package formats and the Lua API the
engine exposes.

Open `docs/index.html` in a browser for the readable version (it is one self-contained file). The reference page is
`docs/clover-engine-reference.md`.

## Contents

| Path | What |
|---|---|
| `docs/clover-engine-reference.md` | The complete reference: architecture, supervisor, file formats, components, Lua layer, subsystems, family differences. |
| `docs/lua-api.md`, `docs/lua-api.json` | Every Lua class and method with its signature and the families that bind it. |
| `docs/supervisor.md`, `file-formats.md`, `scene-components.md`, `boot-music.md`, `c8-error.md`, `family-differences.md`, `lua-toolchain.md` | Topic pages. |
| `docs/index.html` | Viewer with all the pages and an interactive API explorer (one self-contained file). |

## What this repository does not contain

No firmware, no binaries, no decompiled code or pseudocode, and no extracted game or UI assets. The engine and the
firmware belong to Nintendo. The notes describe formats, interfaces and behaviour, and cite function addresses of the
analysed builds as evidence. No license is set.

## Method and confidence

Binaries come from the stock firmware images: SNES EUR 2.0.14, SNES USA 2.0.14, SHVC 2.0.14, NES 1.0.7, HVC 1.0.5 and
Shonen 3.0.1. They were decompiled with REA 6.8.0 (Ghidra 12.1.4, Docker image `rea-agent-ghidra`, offline), with
Capstone for the Lua binding lambdas Ghidra did not define as functions. Each page says what the code shows and what is
inferred or untested. Nothing was run on a console.
