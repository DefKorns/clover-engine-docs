<!-- nav -->
[Home](../README.md) · [Reference](clover-engine-reference.md) · [Supervisor](supervisor.md) · [File formats](file-formats.md) · [Scene components](scene-components.md) · [Lua API](api/README.md) · [Boot music](boot-music.md) · [Error C8](c8-error.md) · [Family differences](family-differences.md) · [Lua toolchain](lua-toolchain.md) · [About](about.md)

---

# LuaJIT toolchain

The console scripts are LuaJIT 2.0 bytecode, version 1, stripped (`1b 4c 4a 01 02`). The engine reports
"LuaJIT 2.0.4".

## Compilers tried on `colors_eur.lua` (decompiled, then recompiled)

| Compiler | Output | Same as the console's file |
|---|---|---|
| `Lib/luajit/luajit.exe` of the Lua Compiler tool (LuaJIT 2.0.2) | 1051 bytes | yes, byte for byte (with `-b` and `-bs`) |
| LuaJIT `v2.0` at `592f9e3f549c7f176a9a7a0d70189559305f2eda`, `-bs`, Linux x64 | 1454 bytes | no |
| LuaJIT `v2.0` at `2410b57fd466298e6a64a68986a6b696c23656ac` (used by `hmod-build/luajit-bc.sh`), `-bs`, Linux x64 | 1454 bytes | no (same output as `592f9e3`) |

All carry the same header. The two recent commits write a larger file for this input; the cause was not investigated.
One file was tested, and the recent builds were Linux x64 while the 2.0.2 one is a Windows exe.

## Open

- Whether the larger bytecode loads and behaves on a console.
- Whether other scripts also differ.
