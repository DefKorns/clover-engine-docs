# Clover engine documentation

Reverse engineering notes on the user interface stack of the Nintendo Classic Mini consoles: the Super NES Classic
Edition, the NES Classic Edition / Nintendo Classic Mini Family Computer, and the Shonen Jump Famicom Mini.

**The documentation is in the [wiki](https://github.com/DefKorns/clover-engine-docs/wiki).**

## What this project is

The consoles run a small Linux system whose interface is not a program with hard-coded screens. A supervisor starts a
player, and the player runs a package of scenes, sprites, sounds and Lua scripts. These notes describe how that works:

- the supervisor `clover-mcp`: its state machine, the game scan, the splash and error screens (including the C8 screen),
  and the transition time-outs;
- the engine `ReedPlayer-Clover`: the scene and component formats, the UI package files, and the version check between
  a package and the engine;
- the Lua layer: the 40 classes and 436 methods the engine exposes to the scripts, with signatures where they could be
  recovered, and the bytecode toolchain that reproduces the console's compiled scripts;
- how the three families (SNES, NES/HVC, Shonen) differ.

Start with the wiki's [Home](https://github.com/DefKorns/clover-engine-docs/wiki) and the
[Reference](https://github.com/DefKorns/clover-engine-docs/wiki/Reference).

## How it was done

1. The supervisor and engine binaries were taken from the stock firmware images of the three families.
2. They were decompiled offline with [REA](https://github.com/morluto/rea) driving [Ghidra](https://ghidra-sre.org),
   in a Docker container with no network. Where Ghidra did not define a function (the Lua binding lambdas), the code
   was disassembled with [Capstone](https://www.capstone-engine.org).
3. The NES supervisor is not stripped, so its function names were used to understand the other two builds, which were
   matched to it through their messages and strings.
4. The Lua scripts of the UI packages are LuaJIT bytecode. They were decompiled with
   [luajit-decompiler-v2](https://github.com/DefKorns/luajit-decompiler-v2) to see how the stock interface calls the API.
5. Nintendo's published sources for the consoles ([Nintendo Open Source Software](https://support.nintendo.com/jp/oss/index.html))
   gave the exact LuaJIT the consoles ship (2.0.4), which reproduces a console script byte for byte, and the names and
   versions of the bundled libraries. They do not contain the supervisor or the engine.

## Limits

Nothing here was run on a console. Each page separates what the code shows from what is inferred, and the open
questions are listed in the Reference. Of the 436 API methods only about 30 have a verified description; the rest
are listed by signature.

## What this repository contains

- [`docs/lua-api.json`](docs/lua-api.json): the Lua API as data (classes, methods, signatures, binding addresses per
  family), which the wiki's API pages are generated from.

No firmware, no binaries, no decompiled code or pseudocode, and no extracted game or UI assets. The engine and the
firmware belong to Nintendo, and this project is not affiliated with or endorsed by Nintendo. The notes describe
formats, interfaces and behaviour, and cite function addresses of the analysed builds as evidence.

## License

The notes and the data in this project are licensed under [Creative Commons Attribution 4.0 International](LICENSE)
(CC BY 4.0). The license covers only what is written here; it gives no rights over Nintendo's firmware or software.
