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
| `docs/index.html` | Generated viewer with the pages and an interactive API explorer. |
| `tools/` | The scripts that produced the data and the viewer. |

## What this repository does not contain

No firmware, no binaries, no decompiled code or pseudocode, and no extracted game or UI assets. The engine and the
firmware belong to Nintendo. The notes describe formats, interfaces and behaviour, and cite function addresses of the
analysed builds as evidence. No license is set.

## Method and confidence

Binaries come from the stock firmware images: SNES EUR 2.0.14, SNES USA 2.0.14, SHVC 2.0.14, NES 1.0.7, HVC 1.0.5 and
Shonen 3.0.1. They were decompiled with REA 6.8.0 (Ghidra 12.1.4, Docker image `rea-agent-ghidra`, offline), with
Capstone for the Lua binding lambdas Ghidra did not define as functions. Each page says what the code shows and what is
inferred or untested. Nothing was run on a console.

## Regenerating

The data scripts expect a working folder with the extracted engines and the Ghidra output (`<firmware>/ReedPlayer-Clover`
and `out/<firmware>/`), which is not part of this repository:

1. `decompile-all` of each engine with REA, into `out/<firmware>/`.
2. `python tools/reg.py <firmware>` then `python tools/sig.py <firmware>` for each of `sneseur-2.0.14`, `nes-1.0.7` and
   `hvcj-shonen-3.0.1`: bindings and their signatures.
3. `python tools/build_api.py` then `python tools/gen_api.py`: `docs/lua-api.json` and `docs/lua-api.md`.
4. `python tools/build_html.py` (needs the Python `markdown` package): `docs/index.html`. This step works from the
   repository alone.

`tools/keysets.py`, `fields2.py`, `splash2.py`, `xref.py` and `lz.py` are the helpers used for the component keys, the
error splash analysis and the splash image decoding.
