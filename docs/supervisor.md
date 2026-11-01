<!-- nav -->
[Home](../README.md) · [Reference](clover-engine-reference.md) · [Supervisor](supervisor.md) · [File formats](file-formats.md) · [Scene components](scene-components.md) · [Lua API](api/README.md) · [Boot music](boot-music.md) · [Error C8](c8-error.md) · [Family differences](family-differences.md) · [Lua toolchain](lua-toolchain.md) · [About](about.md)

---

# The supervisor (clover-mcp)

`/usr/bin/clover-mcp` starts first. It owns the screen and the process lifecycle: it scans the games, starts the menu
(`ReedPlayer-Clover` running the UI), starts the games, shows the splash and error screens, and handles shutdown.

Sources: SNES EUR 2.0.14 (stripped, 650 functions), NES 1.0.7 (**unstripped**, 641 functions, 79 named
`nerd::clover::*`) and Shonen 3.0.1 (stripped). The NES build gives the names; the SNES and Shonen builds were matched
to it by their messages.

## State machine

The NES build names every state handler of `nerd::clover::execute`:

| Handler | Purpose |
|---|---|
| `executeStartup` | Read settings, open the display, scan games. Failure: "UNABLE TO INITIALIZE SYSTEM". |
| `executeCheckEnableTest`, `executeCheckSelectStart`, `executeWaitForKeyCombo` | Key combos at boot (test menu, factory reset). |
| `executeStartMenu` / `executeMenuRunning` / `executeMenuCommand` / `executeMenuShutdown` / `executeMenuFailure` | Menu process lifecycle and the commands it sends back. |
| `executeStartGame` / `executeResumeGame` / `executeStartSuperPlay` | Launch a game, resume a suspend point, start Super Play. |
| `executeGameRunning` / `executeGameReset` / `executeGameShutdown` / `executeGameFailure` | Game process lifecycle. |
| `executeStartTestMenu` / `executeTestMenuRunning` | Test menu. |
| `executeFactoryReset` | Factory reset. |
| `executeStartupFailure` / `executeGeneralFailure` | Show the error splash and wait. |
| `executeShutdown` | Power-off path. |

In the SNES EUR build the same states are in `FUN_0001e290` (startup and game scan), `FUN_0001d948` (start menu),
`FUN_0001ae98` (start game), `FUN_0001b570` (resume game), `FUN_0001c210` (menu command) and the large `FUN_00017860`
(the `execute` loop with the running and shutdown states inlined).

## Settings (clover-mcp.desktop)

The supervisor reads `/usr/share/applications/clover-mcp.desktop`. Keys, and which supervisors know them
(SNES, NES, Shonen):

| Key | S N J | Meaning |
|---|---|---|
| `Settings.GamesFolder` | x x x | Where the games are (`/usr/share/games`). |
| `Settings.MenuLuaFile` | x x x | Output of the scan (`/var/cache/clover/menu.titles.lua`). |
| `Settings.GamesListFile`, `GamesTitleFont`, `CopyrightFont`, `SaveGamePersistentPath`, `DebugMenuDesktop` | - x - | NES only. |
| `Settings.StateFile`, `CommandFile` | x x x | State and command files shared with the menu. |
| `Settings.SaveGameVolatilePath`, `SaveGameVolatileBackupPath` | x x x | Volatile saves. |
| `Settings.DefaultLangFile`, `UserLangFile` | x x x | Language. |
| `Settings.DefaultAutoShutdownDelay`, `UserAutoShutdownDelayFile` | x x x | Auto shutdown. |
| `Settings.DefaultDimmingDelay`, `UserDimmingDelayFile` | x - x | Dimming (SNES and Shonen). |
| `Settings.MenuDesktop`, `TestMenuDesktop`, `FactoryResetDesktop`, `MenuResetDesktop` | x x x | `.desktop` files that start the menu and tools. |
| `Settings.FramebufferPath`, `DispDevPath`, `MenuResolution`, `GameResolution`, `SplashResolution` | x x x | Display. |
| `Settings.SplashStartup` | x - x | Startup splash (`startup.lz4`). |
| `Settings.SplashShutdown` | x x x | Shutdown splash. |
| `Settings.DaemonMode`, `DebugMode`, `GUI` | x x x (GUI: x - x) | Run mode. |
| `Errors.Unknown`, `Errors.StartupFailed` | x x x | Error splash images, one per locale (`Unknown[de_EUR]`...). |

Per game, from `<game>/<game>.desktop`: `Desktop Entry.Name`, `Desktop Entry.Icon`, `Game.Players`,
`Game.Simultaneous`, `Game.ReleaseDate`, `Game.SaveCount`, `Game.Copyright`, `Game.SortRawTitle`,
`Game.SortRawPublisher`, `Game.TestID`; SNES and Shonen add `Game.Status` and `Game.MyPlayDemoTime`; Shonen adds
`Game.FastTransition`.

## The game scan

`FUN_0001e290` (SNES) runs in the startup state:

1. `opendir(GamesFolder)`; for each sub-directory not starting with `.`.
2. Parse `<dir>/<dir>.desktop` as INI.
3. Check for `pixelart/<name>.png`, `autoplay/<name>.inputs` and `superplay/<name>.inputs`.
4. Replace `-` by `_` in the id, and emit one entry of `titles_list = { ... }` into `MenuLuaFile`.

It has no timeout of its own. The menu process then loads that Lua file.

## Splash images

Every error screen is a full-screen LZ4 image (a raw 1280x720 BGRA framebuffer, 3 686 400 bytes) listed per locale in
`[X-CLOVER Errors]`:

| Key | Screen (SNES EUR) |
|---|---|
| `Errors.StartupFailed` | **C1** |
| `Errors.Unknown` | **C8** |

Which failure shows which image (confirmed in the NES build: the code copies `Settings.Unknown` or
`Settings.StartupFailed` into the splash path before `executeStartupFailure` / `executeGeneralFailure` draw it):

- **`Errors.StartupFailed` (C1)**: only `executeStartup`, i.e. "UNABLE TO INITIALIZE SYSTEM".
- **`Errors.Unknown` (C8)**: `executeMenuRunning`, `executeMenuShutdown`, `executeMenuCommand`, `executeGameReset`,
  `executeGameShutdown`, `executeTestMenuRunning`.

In the SNES build the start-up handlers (`FUN_0001e290`, `FUN_0001d948` start menu) read the StartupFailed field
(`+0xe0`) and start game / resume game (`FUN_0001ae98`, `FUN_0001b570`) read the Unknown field (`+0xdc`). The splash
source of the inlined states in `FUN_00017860` is only partly resolved: 13 of its 14 splash-path assignments copy one
context string (`+0x70`), the test-menu start failure copies the next one (`+0x74`). Which is `Errors.Unknown` was not
traced; by the NES layout the common one should be.

## Failure messages

All recorded to stderr as `FATAL ERROR: <text>`: `CLOVER GAME CRASHED` (also `DURING RESET`, `DURING SHUTDOWN`),
`CLOVER MENU CRASHED` (also `DURING SHUTDOWN`), `CLOVER TEST MENU CRASHED`, `GAME TO MENU TRANSITION TIMEOUT`,
`MENU TO GAME TRANSITION TIMEOUT`, `INVALID SETTINGS`, `UNABLE TO INITIALIZE SYSTEM`, `UNABLE TO RESUME CLOVER GAME`,
`UNABLE TO START CLOVER GAME`, `UNABLE TO START CLOVER MENU`, `UNABLE TO START CLOVER SUPER PLAY`,
`UNABLE TO START CLOVER TEST MENU`, `UNKNOWN CLOVER MENU COMMAND`, `WILD UNKNOWN ERROR APPEARED`.

The NES supervisor lacks `CLOVER GAME CRASHED`, `GAME TO MENU TRANSITION TIMEOUT` and
`MENU TO GAME TRANSITION TIMEOUT`.

## Transition timeouts

In the SNES and Shonen supervisors the menu to game and game to menu transitions wait on an eventfd with
`select()` for **20 000 000 microseconds (20 s)** (`FUN_0001d710(fd, 20000000)` in SNES `0x17860`; `FUN_0001dce0` in
Shonen `0x17d40`). A timeout records the matching `TRANSITION TIMEOUT` message. The NES supervisor has no such wait; its
2 000 000 000 ns values are 2 s shutdown timeouts.

### Who writes the transition eventfds

The supervisor creates three eventfds and passes their numbers to the engine in the shared state file as
`WAIT_TRANSITION_FD`, `START_TRANSITION_FD` and `FINISH_TRANSITION_FD` (written by `0x1df18` in Shonen, only when
transitions are enabled). The engine's Lua layer then drives them through `Application.eventFdRead` and
`Application.eventFdWrite` (script `mcp_commands.lua`, read from the SNES EUR 2.0.14 scripts):

| Lua function | Eventfd operation | Called from |
|---|---|---|
| `mcp.waitTransition` | blocking `eventFdRead(WAIT_TRANSITION_FD)` | `sys_boot`, once the textures are loaded (or a boot timeout passes) and the boot fade is not pending |
| `mcp.startTransition` | `eventFdWrite(START_TRANSITION_FD, 1)` | at the end of `mcp.write_command`, right after the command file is written atomically |
| `mcp.finishTransition` | `eventFdWrite(FINISH_TRANSITION_FD, 1)`, then `eventFdWrite(WAIT_TRANSITION_FD, 1)` unless the app is exiting | `sys_boot.stop` |

So the writer is the engine, not the supervisor: a menu that has written a command (for example `start-game`, followed by
`Application.exit`) signals START, and the next UI's boot script signals FINISH when it stops. If the process on the other
side never writes, the supervisor's 20 s wait expires. Not verified: which of the three descriptors each `select()` in the
supervisor watches, and what happens on the engine side when the supervisor passes no descriptors.
