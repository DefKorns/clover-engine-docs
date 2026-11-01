<!-- nav -->
[Home](../README.md) · [Reference](clover-engine-reference.md) · [Supervisor](supervisor.md) · [File formats](file-formats.md) · [Scene components](scene-components.md) · [Lua API](api/README.md) · [Boot music](boot-music.md) · [Error C8](c8-error.md) · [Family differences](family-differences.md) · [Lua toolchain](lua-toolchain.md) · [About](about.md)

---

# LuaJIT toolchain

The console scripts are LuaJIT 2.0 bytecode, version 1, stripped (`1b 4c 4a 01 02`). The engine reports
"LuaJIT 2.0.4".

## The source the consoles use

Nintendo's open-source release for the consoles includes the LuaJIT they ship: `ext-luajit-83dda3b07286174de43ee5adb25e7cc5fbe308e3`
(the same commit name in the NES Classic and SNES Classic packages). It identifies itself as **LuaJIT 2.0.4** and has a
CMake build and Visual Studio projects added, so it is a vendor copy, not an upstream tag.

Built from that source on Linux x64 (`make`, GCC 13), `luajit -b`, `-bs` and `-bgs` turn the decompiled `colors_eur.lua`
into a **1051-byte file identical to the console's**. `-bg` (debug information kept) gives 1164 bytes and differs.
So use `-b` or `-bs`. One script was tested.

## Other compilers tried on the same `colors_eur.lua` (decompiled, then recompiled)

| Compiler | Output | Same as the console's file |
|---|---|---|
| LuaJIT 2.0.2 (Windows `luajit.exe`) | 1051 bytes | yes, byte for byte (with `-b` and `-bs`) |
| LuaJIT `v2.0` at `592f9e3f549c7f176a9a7a0d70189559305f2eda`, `-bs`, Linux x64 | 1454 bytes | no |
| LuaJIT `v2.0` at `2410b57fd466298e6a64a68986a6b696c23656ac`, `-bs`, Linux x64 | 1454 bytes | no (same output as `592f9e3`) |

All carry the same header. The two recent commits write a larger file for this input; the cause was not investigated.
One file was tested, and the recent builds were Linux x64 while the 2.0.2 one is a Windows exe.

## Open

- Whether the larger bytecode of the two upstream commits loads and behaves on a console.
- Whether other scripts also match the vendor build byte for byte; only `colors_eur.lua` was compared.
