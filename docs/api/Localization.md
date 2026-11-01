<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › Localization

# Localization

6 methods (static functions of a global table).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `getLocale` | `Localization.getLocale(...): (string, string, integer)` | SNJ | `a3220 / be268 / e2f8c` | Returns the locale. |
| `getText` | `Localization.getText(arg1: string): string` | SNJ | `a31b4 / bb03c / e2f20` | Returns the text. |
| `getUserLocale` | `Localization.getUserLocale(...): (string, string, integer)` | SNJ | `a337c / bdbdc / e30e8` | Returns the user locale. |
| `reloadStrings` | `Localization.reloadStrings(...): number` | SNJ | `a3280 / b4830 / e2fec` | Not described (name only). |
| `setLocale` | `Localization.setLocale(arg1: integer, arg2: any, arg3: any)` | SNJ | `a3434 / cee38 / e31a0` | Sets the locale. |
| `useUserLocale` | `Localization.useUserLocale(...)` | SNJ | `a32d8 / e8080 / e3044` | Not described (name only). |

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

← [LabelComponent](LabelComponent.md) · [Index](README.md) · [MeshComponent](MeshComponent.md) →
