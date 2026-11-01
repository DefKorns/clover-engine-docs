<!-- nav -->
[Home](../README.md) · [Reference](clover-engine-reference.md) · [Supervisor](supervisor.md) · [File formats](file-formats.md) · [Scene components](scene-components.md) · [Lua API](api/README.md) · [Boot music](boot-music.md) · [Error C8](c8-error.md) · [Family differences](family-differences.md) · [Lua toolchain](lua-toolchain.md) · [About](about.md)

---

# Error C8

Evidence: stock firmwares, supervisor `clover-mcp` (SNES EUR 2.0.14, NES 1.0.7 unstripped, Shonen 3.0.1), decompiled
with REA/Ghidra, plus disassembly with Capstone. Details of the supervisor are in [supervisor.md](supervisor.md).

## What C8 is (confirmed)

- A full-screen image shown by `clover-mcp`: `Errors.Unknown`. Decoded, the SNES EUR image reads "C8: An error has
  occurred". `Errors.StartupFailed` reads "C1".
- The images are LZ4 blocks that decompress to a raw 1280x720 BGRA framebuffer.
- The Lua UI does not show C8. Its own dialogs are C2, C4, C6, C7 and C9 (`sys_error_*` strings). The string key
  `sys_error_Unexcepted` (C8) is not used by any script of the stock UI package.

## When it appears

In the NES build, where the handlers are named, the code that draws the failure copies the image path before showing it:

- `executeStartup` ("UNABLE TO INITIALIZE SYSTEM") uses `Errors.StartupFailed` (C1);
- `executeMenuRunning`, `executeMenuShutdown`, `executeMenuCommand`, `executeGameReset`, `executeGameShutdown` and
  `executeTestMenuRunning` use `Errors.Unknown` (C8): a menu or game crash, an unknown menu command, a failure during
  reset or shutdown.

In the SNES build the same split holds for the handlers that were resolved: start-up and start-menu read the
StartupFailed field, start-game and resume-game read the Unknown field. The inlined running/shutdown states of the large
`execute` function are only partly resolved (below).

In the SNES `execute` function (`FUN_00017860`) the failure path sets the splash path with 14 string assignments. Thirteen copy the same context string (offset `+0x70` of the object passed in) and exactly one copies its neighbour (`+0x74`): the one for `UNABLE TO START CLOVER TEST MENU`. So the test-menu start failure does not use the same image as the menu and game failures. Which of the two strings is `Errors.Unknown` and which `Errors.StartupFailed` was not traced: the settings loader (`FUN_00020a98`) stores them at `+0xdc` and `+0xe0` of a different object, and the link to the `execute` context was not found. The caller (`FUN_00014b68`) builds that context from the desktop-entry and `X-CLOVER Settings` keys, but no assignment of the two strings at `+0x70` / `+0x74` was found in it, so they may be filled elsewhere or stay at a default.

## The 20 s timeouts

The SNES and Shonen supervisors wait on an eventfd with a 20 000 000 microsecond `select()` for the menu to game and
game to menu transitions (SNES `FUN_0001d710`, called from `0x17860` at two places; Shonen `FUN_0001dce0`).
On expiry they record `GAME TO MENU TRANSITION TIMEOUT` or `MENU TO GAME TRANSITION TIMEOUT`. The NES supervisor has no
such wait.

## What is not established

- That the timeout path ends on the `Errors.Unknown` image: in the SNES build the inlined code copies a context string whose
  identity was not traced (see above). By the NES layout it should.
- Which of the three transition eventfds each `select()` watches. The engine's Lua layer is the writer (see [Supervisor](supervisor.md#who-writes-the-transition-eventfds)).
- The game scan (`menu.titles.lua`) has no time limit of its own; a longer list only matters through the time the menu
  needs to load it.
- No allocation-failure path was found that maps to these screens. That is absence of evidence.
