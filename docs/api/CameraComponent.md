<!-- nav -->
[Home](../../README.md) · [Reference](../clover-engine-reference.md) · [Supervisor](../supervisor.md) · [File formats](../file-formats.md) · [Scene components](../scene-components.md) · [Lua API](../api/README.md) · [Boot music](../boot-music.md) · [Error C8](../c8-error.md) · [Family differences](../family-differences.md) · [Lua toolchain](../lua-toolchain.md) · [About](../about.md)

---

[Documentation](../../README.md) › [Lua API](README.md) › CameraComponent

# CameraComponent

21 methods (instance methods).

| Method | Signature | Families | Binding S / N / J | Summary |
|---|---|---|---|---|
| `create` | `CameraComponent:create(...)` | SNJ | `a7944 / 115240 / e8508` | Not described (name only). |
| `getCategoryMask` | `CameraComponent:getCategoryMask(): number` | SNJ | `a98d0 / fceb4 / e9bc4` | Returns the category mask. |
| `getClearColor` | `CameraComponent:getClearColor(): (number, number, number, number)` | SNJ | `a99f4 / f6fe4 / e9ce8` | Returns the clear color. |
| `getClearScreen` | `CameraComponent:getClearScreen(): boolean` | SNJ | `a9af8 / fd4e0 / e9dec` | Returns the clear screen. |
| `getFrontCameraRenderingAtViewPoint` | `CameraComponent:getFrontCameraRenderingAtViewPoint(arg1: integer, arg2: integer)` | J | `- / - / e9904` | Returns the front camera rendering at view point. |
| `getOrder` | `CameraComponent:getOrder(): integer` | SNJ | `a9b5c / fdc00 / e9e50` | Returns the order. |
| `getRenderTarget` | `CameraComponent:getRenderTarget()` | SNJ | `a9780 / 113154 / e9f48` | Returns the render target. |
| `getTargetScreen` | `CameraComponent:getTargetScreen(): integer` | SN | `a9c54 / fda58 / -` | Returns the target screen. |
| `getTargetSize` | `CameraComponent:getTargetSize(): (number, number)` | J | `- / - / e9ae8` | Returns the target size. |
| `getTargetView` | `CameraComponent:getTargetView(): number` | J | `- / - / ea030` | Returns the target view. |
| `getViewportRect` | `CameraComponent:getViewportRect(): (number, number, number, number)` | SNJ | `a9bc0 / f8638 / e9eb4` | Returns the viewport rect. |
| `screenToWorldPosition` | `CameraComponent:screenToWorldPosition(arg1: number, arg2: number): (number, number)` | SNJ | `a9df8 / d43c4 / ea098` | Not described (name only). |
| `setCategoryMask` | `CameraComponent:setCategoryMask(categoryMask: integer)` | SNJ | `a9868 / fd364 / e9b5c` | Sets the category mask. |
| `setClearColor` | `CameraComponent:setClearColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | `a9938 / f66c8 / e9c2c` | Sets the clear color. |
| `setClearScreen` | `CameraComponent:setClearScreen(clearScreen: boolean)` | SNJ | `a9a90 / fc0d8 / e9d84` | Sets the clear screen. |
| `setOrder` | `CameraComponent:setOrder(order: integer)` | SNJ | `a9ebc / fbacc / ea15c` | Sets the order. |
| `setRenderTarget` | `CameraComponent:setRenderTarget(renderTarget: RenderTargetResource)` | SNJ | `a9710 / d4774 / ea290` | Sets the render target. |
| `setTargetScreen` | `CameraComponent:setTargetScreen(targetScreen: integer)` | SN | `a9fe8 / fb5f8 / -` | Sets the target screen. |
| `setTargetView` | `CameraComponent:setTargetView(targetView: integer)` | J | `- / - / ea388` | Sets the target view. |
| `setViewportRect` | `CameraComponent:setViewportRect(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | `a9f2c / 101f58 / ea1cc` | Sets the viewport rect. |
| `worldToScreenPosition` | `CameraComponent:worldToScreenPosition(arg1: number, arg2: number): (number, number)` | SNJ | `a9cb8 / d4578 / e9a24` | Not described (name only). |

## How to read the tables

- **Signature**: `Class:method(...)` is an instance method (colon call); `Class.method(...)` is a static function of a
  global table. Types come from the helper the binding uses to read an argument or push a result: `number`, `integer`,
  `boolean`, `string`, or a resource class. `any` means that helper was not classified. For NES-only methods the
  signature lists only the argument count, except the `VideoComponent` methods, whose bindings were read by hand.
- **Families**: S = SNES (EUR, USA, SHVC), N = NES and HVC, J = Shonen. A dash means the family does not bind the method.
- **Binding**: address of the binding function in the SNES EUR 2.0.14, NES 1.0.7 and Shonen 3.0.1 builds.
- **Summary**: derived from the method name (getters and setters only); "Not described (name only)" means nothing beyond the name is known. A **Note** was verified in the code or in the stock scripts.
- Parameter names are not in the binary: single-argument setters use the name after `set`, the others are `argN`.


---

← [CameraCaptureResource](CameraCaptureResource.md) · [Index](README.md) · [CameraDevice](CameraDevice.md) →
