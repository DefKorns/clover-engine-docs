<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › FileUtils

# FileUtils

17 methods (static functions of a global table).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `cleanupPath` | `FileUtils.cleanupPath(arg1: any)` | SNJ | `a5acc / babbc / e5e34` | Not described (name only). |
| `copyDirectory` | `FileUtils.copyDirectory(arg1: any, arg2: any): boolean` | SJ | `a518c / - / e54f4` | Not described (name only). |
| `copyDirectoryAsync` | `FileUtils.copyDirectoryAsync(arg1: any, arg2: any, arg3: any, arg4: any): boolean` | SJ | `a4e14 / - / e5198` | Not described (name only). |
| `copyFile` | `FileUtils.copyFile(...): boolean` | SNJ | `a69d0 / cc470 / e6e48` | Not described (name only). |
| `copyFileAsync` | `FileUtils.copyFileAsync(arg1: boolean, arg2: boolean, arg3: any, arg4: any, arg5: any, arg6: any): boolean` | SJ | `a4f60 / - / e52d8` | Not described (name only). |
| `createDirectory` | `FileUtils.createDirectory(arg1: any): boolean` | SJ | `a52d0 / - / e5638` | Not described (name only). |
| `deleteDirectory` | `FileUtils.deleteDirectory(arg1: any): boolean` | SNJ | `a524c / bbe34 / e55b4` | Not described (name only). |
| `deleteFile` | `FileUtils.deleteFile(arg1: any): boolean` | SNJ | `a53e4 / bbef4 / e574c` | Not described (name only). |
| `directoryExists` | `FileUtils.directoryExists(arg1: any): boolean` | SJ | `a535c / - / e56c4` | Not described (name only). |
| `fileExists` | `FileUtils.fileExists(arg1: any): boolean` | SNJ | `a5b64 / bbc74 / e5ecc` | Not described (name only). |
| `listDirectories` | `FileUtils.listDirectories(arg1: any)` | SNJ | `a589c / 107378 / e5c04` | Not described (name only). |
| `listDirectoryFiles` | `FileUtils.listDirectoryFiles(arg1: any)` | SNJ | `a5a00 / 107104 / e5d68` | Not described (name only). |
| `listDirectoryFilesByExt` | `FileUtils.listDirectoryFilesByExt(arg1: any, arg2: any)` | SNJ | `a5930 / 108f6c / e5c98` | Not described (name only). |
| `readFile` | `FileUtils.readFile(arg1: any)` | SNJ | `a569c / b9cc4 / e5a04` | Not described (name only). |
| `renameDirectory` | `FileUtils.renameDirectory(arg1: any, arg2: any): boolean` | SJ | `a50dc / - / e5448` | Not described (name only). |
| `renameFile` | `FileUtils.renameFile(arg1: any, arg2: any): boolean` | SNJ | `a5468 / cc700 / e57d0` | Not described (name only). |
| `writeFile` | `FileUtils.writeFile(arg1: any, arg2: any): boolean` | SJ | `a5534 / - / e589c` | Not described (name only). |

## How to read the tables

- **Signature**: `Class:method(...)` is an instance method (colon call); `Class.method(...)` is a static function of a
  global table. Types come from the helper the binding uses to read an argument or push a result: `number`, `integer`,
  `boolean`, `string`, or a resource class. `any` means that helper was not classified. For NES-only methods the
  signature lists only the argument count.
- **Families**: S = SNES (EUR, USA, SHVC), N = NES and HVC, J = Shonen. A dash means the family does not bind the method.
- **Binding**: address of the binding function in the SNES EUR 2.0.14, NES 1.0.7 and Shonen 3.0.1 builds.
- **Summary**: derived from the method name (getters and setters only); "Not described (name only)" means nothing beyond the name is known. A **Note** was verified in the code or in the stock scripts.
- Parameter names are not in the binary: single-argument setters use the name after `set`, the others are `argN`.


---

← [FileNameUtils](FileNameUtils.md) · [Index](README.md) · [FontResource](FontResource.md) →
