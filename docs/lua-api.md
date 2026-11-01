# Lua API reference

Every class and method the engine exposes to Lua, with its signature, which engine families bind it, and the
address of its binding in each build. Interactive version: `index.html`, page *API explorer*.

## How to read this

- `Class:method(...)` is an instance method (called with a colon); `Class.method(...)` is a static function of a
  global table (`Application`, `FileUtils`, `Input`, `Localization`, `CRC64`).
- Parameter and return types come from the engine code: the helper each binding calls to read an argument or push a
  result (`number`, `integer`, `boolean`, `string`, or a resource class). `any` means the argument is read by a helper
  that was not classified. Parameter names are not in the binary: single-argument setters use the name after `set`,
  the rest are `argN`.
- Families: **S** = SNES (EUR, USA, SHVC; identical API), **N** = NES and HVC (identical API), **J** = Shonen. The NES
  signatures list only the number of arguments: its binding code was not classified.
- The summaries are derived from the method names. Lines under *Note* were verified in the code.

## Contents

- [AnimatedImageResource](#animatedimageresource) (1 method)
- [AnimatedSpriteComponent](#animatedspritecomponent) (16 methods)
- [AnimatorComponent](#animatorcomponent) (22 methods)
- [Application](#application) (18 methods)
- [CRC64](#crc64) (1 method)
- [CameraCaptureResource](#cameracaptureresource) (2 methods)
- [CameraComponent](#cameracomponent) (21 methods)
- [CameraDevice](#cameradevice) (7 methods)
- [ClickableComponent](#clickablecomponent) (23 methods)
- [Component](#component) (8 methods)
- [FileNameUtils](#filenameutils) (6 methods)
- [FileUtils](#fileutils) (17 methods)
- [FontResource](#fontresource) (3 methods)
- [ImageResource](#imageresource) (4 methods)
- [Input](#input) (8 methods)
- [LabelComponent](#labelcomponent) (36 methods)
- [Localization](#localization) (6 methods)
- [MeshComponent](#meshcomponent) (5 methods)
- [Object](#object) (2 methods)
- [Player](#player) (3 methods)
- [RawResource](#rawresource) (1 method)
- [RenderTargetResource](#rendertargetresource) (2 methods)
- [Resource](#resource) (2 methods)
- [Scene](#scene) (1 method)
- [SceneAnimation](#sceneanimation) (1 method)
- [ScriptComponent](#scriptcomponent) (1 method)
- [SoundComponent](#soundcomponent) (36 methods)
- [SoundListenerComponent](#soundlistenercomponent) (1 method)
- [SoundResource](#soundresource) (3 methods)
- [SpriteAnimationResource](#spriteanimationresource) (1 method)
- [SpriteComponent](#spritecomponent) (11 methods)
- [SpriteResource](#spriteresource) (3 methods)
- [TextVariable](#textvariable) (3 methods)
- [TextureComponent](#texturecomponent) (19 methods)
- [TextureResource](#textureresource) (2 methods)
- [TilemapComponent](#tilemapcomponent) (7 methods)
- [VideoComponent](#videocomponent) (18 methods)
- [VisualComponent](#visualcomponent) (31 methods)
- [Volumes](#volumes) (8 methods)
- [WorldNode](#worldnode) (76 methods)

## AnimatedImageResource

1 method. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getFrameCount` | `AnimatedImageResource:getFrameCount(): number` | J | Returns the frame count. |

## AnimatedSpriteComponent

16 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `animEnded` | `AnimatedSpriteComponent:animEnded(): boolean` | SNJ | Calls anim ended. |
| `changeAnimation` | `AnimatedSpriteComponent:changeAnimation(arg1: SpriteAnimationResource)` | SNJ | Calls change animation. |
| `create` | `AnimatedSpriteComponent:create(...)` | SNJ | Calls create. |
| `getAnchor` | `AnimatedSpriteComponent:getAnchor(): (number, number)` | SNJ | Returns the anchor. |
| `getSpriteAnimation` | `AnimatedSpriteComponent:getSpriteAnimation()` | SNJ | Returns the sprite animation. |
| `increaseTime` | `AnimatedSpriteComponent:increaseTime(arg1: number)` | SNJ | Calls increase time. |
| `isAutoUpdated` | `AnimatedSpriteComponent:isAutoUpdated(): boolean` | SNJ | Returns whether auto updated. |
| `isFlippedHorizontal` | `AnimatedSpriteComponent:isFlippedHorizontal(): boolean` | SNJ | Returns whether flipped horizontal. |
| `isFlippedVertical` | `AnimatedSpriteComponent:isFlippedVertical(): boolean` | SNJ | Returns whether flipped vertical. |
| `isLooped` | `AnimatedSpriteComponent:isLooped(): boolean` | SNJ | Returns whether looped. |
| `restart` | `AnimatedSpriteComponent:restart()` | SNJ | Calls restart. |
| `setAutoUpdate` | `AnimatedSpriteComponent:setAutoUpdate(autoUpdate: boolean)` | SNJ | Sets the auto update. |
| `setFlipHorizontal` | `AnimatedSpriteComponent:setFlipHorizontal(flipHorizontal: boolean)` | SNJ | Sets the flip horizontal. |
| `setFlipVertical` | `AnimatedSpriteComponent:setFlipVertical(flipVertical: boolean)` | SNJ | Sets the flip vertical. |
| `setLoop` | `AnimatedSpriteComponent:setLoop(loop: boolean)` | SNJ | Sets the loop. |
| `setSpriteAnimation` | `AnimatedSpriteComponent:setSpriteAnimation(spriteAnimation: SpriteAnimationResource)` | SNJ | Sets the sprite animation. |

## AnimatorComponent

22 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `advanceCurrentTime` | `AnimatorComponent:advanceCurrentTime(arg1: number)` | SNJ | Calls advance current time. |
| `callEventHandlers` | `AnimatorComponent:callEventHandlers(arg1: number, arg2: number)` | SNJ | Calls call event handlers. |
| `create` | `AnimatorComponent:create(...)` | SNJ | Calls create. |
| `getCurrentTime` | `AnimatorComponent:getCurrentTime(): number` | SNJ | Returns the current time. |
| `getDuration` | `AnimatorComponent:getDuration(): number` | SNJ | Returns the duration. |
| `getEventListener` | `AnimatorComponent:getEventListener()` | SNJ | Returns the event listener. |
| `getSceneAnimation` | `AnimatorComponent:getSceneAnimation()` | SNJ | Returns the scene animation. |
| `getSpeed` | `AnimatorComponent:getSpeed(): number` | SNJ | Returns the speed. |
| `isLooped` | `AnimatorComponent:isLooped(): boolean` | SNJ | Returns whether looped. |
| `isPaused` | `AnimatorComponent:isPaused(): boolean` | SNJ | Returns whether paused. |
| `isPlaying` | `AnimatorComponent:isPlaying(): boolean` | SNJ | Returns whether playing. |
| `isStopped` | `AnimatorComponent:isStopped(): boolean` | SNJ | Returns whether stopped. |
| `play` | `AnimatorComponent:play()` | SNJ | Calls play. |
| `replay` | `AnimatorComponent:replay()` | SNJ | Calls replay. |
| `reset` | `AnimatorComponent:reset()` | SNJ | Calls reset. |
| `resolveBindings` | `AnimatorComponent:resolveBindings()` | SNJ | Calls resolve bindings. |
| `setCurrentTime` | `AnimatorComponent:setCurrentTime(currentTime: number)` | SNJ | Sets the current time. |
| `setEventListener` | `AnimatorComponent:setEventListener(eventListener: any)` | SNJ | Sets the event listener. |
| `setLoop` | `AnimatorComponent:setLoop(loop: boolean)` | SNJ | Sets the loop. |
| `setSceneAnimation` | `AnimatorComponent:setSceneAnimation(sceneAnimation: SceneAnimation)` | SNJ | Sets the scene animation. |
| `setSpeed` | `AnimatorComponent:setSpeed(speed: number)` | SNJ | Sets the speed. |
| `stop` | `AnimatorComponent:stop()` | SNJ | Calls stop. |

## Application

18 methods. Static functions of a global table.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `abort` | `Application.abort(...)` | J | Calls abort. |
| `captureScreen` | `Application.captureScreen(arg1: integer, arg2: string): number` | SNJ | Calls capture screen. |
| `eventFdRead` | `Application.eventFdRead(arg1: integer): (integer, number)` | SJ | Calls event fd read. |
| `eventFdWrite` | `Application.eventFdWrite(arg1: integer, arg2: integer): integer` | SJ | Calls event fd write. |
| `exit` | `Application.exit(...)` | SNJ | Calls exit. |
| `getDataPath` | `Application.getDataPath(arg1: any)` | SNJ | Returns the data path. |
| `getErrorHandler` | `Application.getErrorHandler(...)` | J | Returns the error handler. |
| `getExitHandler` | `Application.getExitHandler(...)` | SNJ | Returns the exit handler. |
| `getMaxFPS` | `Application.getMaxFPS(...): number` | SNJ | Returns the max fps. |
| `getResourcesPath` | `Application.getResourcesPath(arg1: any)` | J | Returns the resources path. |
| `pause` | `Application.pause(...)` | SNJ | Calls pause. |
| `resetErrorHandler` | `Application.resetErrorHandler(...)` | J | Calls reset error handler. |
| `resetExitHandler` | `Application.resetExitHandler(...)` | SNJ | Calls reset exit handler. |
| `setErrorHandler` | `Application.setErrorHandler(...)` | J | Sets the error handler. |
| `setExitHandler` | `Application.setExitHandler(arg1: any, arg2: any)` | SNJ | Sets the exit handler. |
| `setMaxFPS` | `Application.setMaxFPS(maxFPS: number)` | SNJ | Sets the max fps. |
| `skipDraw` | `Application.skipDraw(...)` | SJ | Calls skip draw. |
| `unpause` | `Application.unpause(...)` | SNJ | Calls unpause. |

## CRC64

1 method. Static functions of a global table.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `hash` | `CRC64.hash(arg1: any): number` | SNJ | Calls hash. |

## CameraCaptureResource

2 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getCameraSource` | `CameraCaptureResource:getCameraSource(0 args)` | N | Returns the camera source. |
| `getPixel` | `CameraCaptureResource:getPixel(2 args)` | N | Returns the pixel. |

## CameraComponent

21 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `create` | `CameraComponent:create(...)` | SNJ | Calls create. |
| `getCategoryMask` | `CameraComponent:getCategoryMask(): number` | SNJ | Returns the category mask. |
| `getClearColor` | `CameraComponent:getClearColor(): (number, number, number, number)` | SNJ | Returns the clear color. |
| `getClearScreen` | `CameraComponent:getClearScreen(): boolean` | SNJ | Returns the clear screen. |
| `getFrontCameraRenderingAtViewPoint` | `CameraComponent:getFrontCameraRenderingAtViewPoint(arg1: integer, arg2: integer)` | J | Returns the front camera rendering at view point. |
| `getOrder` | `CameraComponent:getOrder(): integer` | SNJ | Returns the order. |
| `getRenderTarget` | `CameraComponent:getRenderTarget()` | SNJ | Returns the render target. |
| `getTargetScreen` | `CameraComponent:getTargetScreen(): integer` | SN | Returns the target screen. |
| `getTargetSize` | `CameraComponent:getTargetSize(): (number, number)` | J | Returns the target size. |
| `getTargetView` | `CameraComponent:getTargetView(): number` | J | Returns the target view. |
| `getViewportRect` | `CameraComponent:getViewportRect(): (number, number, number, number)` | SNJ | Returns the viewport rect. |
| `screenToWorldPosition` | `CameraComponent:screenToWorldPosition(arg1: number, arg2: number): (number, number)` | SNJ | Calls screen to world position. |
| `setCategoryMask` | `CameraComponent:setCategoryMask(categoryMask: integer)` | SNJ | Sets the category mask. |
| `setClearColor` | `CameraComponent:setClearColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | Sets the clear color. |
| `setClearScreen` | `CameraComponent:setClearScreen(clearScreen: boolean)` | SNJ | Sets the clear screen. |
| `setOrder` | `CameraComponent:setOrder(order: integer)` | SNJ | Sets the order. |
| `setRenderTarget` | `CameraComponent:setRenderTarget(renderTarget: RenderTargetResource)` | SNJ | Sets the render target. |
| `setTargetScreen` | `CameraComponent:setTargetScreen(targetScreen: integer)` | SN | Sets the target screen. |
| `setTargetView` | `CameraComponent:setTargetView(targetView: integer)` | J | Sets the target view. |
| `setViewportRect` | `CameraComponent:setViewportRect(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | Sets the viewport rect. |
| `worldToScreenPosition` | `CameraComponent:worldToScreenPosition(arg1: number, arg2: number): (number, number)` | SNJ | Calls world to screen position. |

## CameraDevice

7 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getTextureCoordinates` | `CameraDevice:getTextureCoordinates(0 args)` | N | Returns the texture coordinates. |
| `isStarted` | `CameraDevice:isStarted(0 args)` | N | Returns whether started. |
| `setEffect` | `CameraDevice:setEffect(1 args)` | N | Sets the effect. |
| `setFramerate` | `CameraDevice:setFramerate(1 args)` | N | Sets the framerate. |
| `setResolution` | `CameraDevice:setResolution(2 args)` | N | Sets the resolution. |
| `start` | `CameraDevice:start(0 args)` | N | Calls start. |
| `stop` | `CameraDevice:stop(0 args)` | N | Calls stop. |

## ClickableComponent

23 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `create` | `ClickableComponent:create(...)` | SNJ | Calls create. |
| `getAutoRaycastMask` | `ClickableComponent:getAutoRaycastMask(...): number` | SNJ | Returns the auto raycast mask. |
| `getBoxShapeSize` | `ClickableComponent:getBoxShapeSize(): (number, number)` | SNJ | Returns the box shape size. |
| `getCenter` | `ClickableComponent:getCenter(): (number, number)` | SNJ | Returns the center. |
| `getCircleShapeRadius` | `ClickableComponent:getCircleShapeRadius(): number` | SNJ | Returns the circle shape radius. |
| `getClickListener` | `ClickableComponent:getClickListener()` | SNJ | Returns the click listener. |
| `getLayer` | `ClickableComponent:getLayer(): integer` | SNJ | Returns the layer. |
| `getShapeType` | `ClickableComponent:getShapeType(): integer` | SNJ | Returns the shape type. |
| `getWorldZIndex` | `ClickableComponent:getWorldZIndex(): integer` | SNJ | Returns the world zindex. |
| `getZIndex` | `ClickableComponent:getZIndex(): integer` | SNJ | Returns the zindex. |
| `hitTest` | `ClickableComponent:hitTest(arg1: number, arg2: number): boolean` | SNJ | Calls hit test. |
| `raycastAll` | `ClickableComponent:raycastAll(arg1: number): array` | SNJ | Calls raycast all. |
| `raycastAllInCategories` | `ClickableComponent:raycastAllInCategories(arg1: number, arg2: number): array` | SNJ | Calls raycast all in categories. |
| `raycastNearest` | `ClickableComponent:raycastNearest(arg1: number)` | SNJ | Calls raycast nearest. |
| `raycastNearestInCategories` | `ClickableComponent:raycastNearestInCategories(arg1: number, arg2: number)` | SNJ | Calls raycast nearest in categories. |
| `setAutoRaycastMask` | `ClickableComponent:setAutoRaycastMask()` | SNJ | Sets the auto raycast mask. |
| `setBoxShape` | `ClickableComponent:setBoxShape(arg1: number, arg2: number)` | SNJ | Sets the box shape. |
| `setCenter` | `ClickableComponent:setCenter(arg1: number, arg2: number)` | SNJ | Sets the center. |
| `setCircleShape` | `ClickableComponent:setCircleShape(circleShape: number)` | SNJ | Sets the circle shape. |
| `setClickListener` | `ClickableComponent:setClickListener(clickListener: any)` | SNJ | Sets the click listener. |
| `setLayer` | `ClickableComponent:setLayer(layer: integer)` | SNJ | Sets the layer. |
| `setWorldZIndex` | `ClickableComponent:setWorldZIndex(worldZIndex: integer)` | SNJ | Sets the world zindex. |
| `setZIndex` | `ClickableComponent:setZIndex(zIndex: integer)` | SNJ | Sets the zindex. |

## Component

8 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `disable` | `Component:disable()` | SNJ | Calls disable. **Note:** Disables the component. The boot music (Main.bootBGM) is disabled this way by main.lua and by the Shonen firmware. |
| `enable` | `Component:enable()` | SNJ | Calls enable. **Note:** Enables the component. |
| `getNode` | `Component:getNode()` | SNJ | Returns the node. |
| `getTypeName` | `Component:getTypeName(): string` | SNJ | Returns the type name. |
| `isActive` | `Component:isActive(): boolean` | SNJ | Returns whether active. |
| `isEnabled` | `Component:isEnabled(): boolean` | SNJ | Returns whether enabled. |
| `isSelfEnabled` | `Component:isSelfEnabled(): boolean` | SNJ | Returns whether self enabled. |
| `setEnabled` | `Component:setEnabled(enabled: boolean)` | SNJ | Sets the enabled. |

## FileNameUtils

6 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `concat` | `FileNameUtils:concat(arg1: any)` | J | Calls concat. |
| `getBasename` | `FileNameUtils:getBasename()` | J | Returns the basename. |
| `getPath` | `FileNameUtils:getPath()` | J | Returns the path. |
| `getPrefix` | `FileNameUtils:getPrefix()` | J | Returns the prefix. |
| `getPrefixLength` | `FileNameUtils:getPrefixLength(): number` | J | Returns the prefix length. |
| `normalize` | `FileNameUtils:normalize()` | J | Calls normalize. |

## FileUtils

17 methods. Static functions of a global table.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `cleanupPath` | `FileUtils.cleanupPath(arg1: any)` | SNJ | Calls cleanup path. |
| `copyDirectory` | `FileUtils.copyDirectory(arg1: any, arg2: any): boolean` | SJ | Calls copy directory. |
| `copyDirectoryAsync` | `FileUtils.copyDirectoryAsync(arg1: any, arg2: any, arg3: any, arg4: any): boolean` | SJ | Calls copy directory async. |
| `copyFile` | `FileUtils.copyFile(...): boolean` | SNJ | Calls copy file. |
| `copyFileAsync` | `FileUtils.copyFileAsync(arg1: boolean, arg2: boolean, arg3: any, arg4: any, arg5: any, arg6: any): boolean` | SJ | Calls copy file async. |
| `createDirectory` | `FileUtils.createDirectory(arg1: any): boolean` | SJ | Calls create directory. |
| `deleteDirectory` | `FileUtils.deleteDirectory(arg1: any): boolean` | SNJ | Calls delete directory. |
| `deleteFile` | `FileUtils.deleteFile(arg1: any): boolean` | SNJ | Calls delete file. |
| `directoryExists` | `FileUtils.directoryExists(arg1: any): boolean` | SJ | Calls directory exists. |
| `fileExists` | `FileUtils.fileExists(arg1: any): boolean` | SNJ | Calls file exists. |
| `listDirectories` | `FileUtils.listDirectories(arg1: any)` | SNJ | Calls list directories. |
| `listDirectoryFiles` | `FileUtils.listDirectoryFiles(arg1: any)` | SNJ | Calls list directory files. |
| `listDirectoryFilesByExt` | `FileUtils.listDirectoryFilesByExt(arg1: any, arg2: any)` | SNJ | Calls list directory files by ext. |
| `readFile` | `FileUtils.readFile(arg1: any)` | SNJ | Calls read file. |
| `renameDirectory` | `FileUtils.renameDirectory(arg1: any, arg2: any): boolean` | SJ | Calls rename directory. |
| `renameFile` | `FileUtils.renameFile(arg1: any, arg2: any): boolean` | SNJ | Calls rename file. |
| `writeFile` | `FileUtils.writeFile(arg1: any, arg2: any): boolean` | SJ | Calls write file. |

## FontResource

3 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getBaselineOffset` | `FontResource:getBaselineOffset(): integer` | SNJ | Returns the baseline offset. |
| `getLineHeight` | `FontResource:getLineHeight(): integer` | SNJ | Returns the line height. |
| `getSpaceSize` | `FontResource:getSpaceSize(): integer` | SNJ | Returns the space size. |

## ImageResource

4 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getPixel` | `ImageResource:getPixel(arg1: number, arg2: number): (number, number, number, number)` | SNJ | Returns the pixel. |
| `getSize` | `ImageResource:getSize(): (integer, integer)` | SNJ | Returns the size. |
| `readPixel` | `ImageResource:readPixel(arg1: integer, arg2: integer): (number, number, number, number)` | J | Calls read pixel. |
| `reloadFromFile` | `ImageResource:reloadFromFile(...): number` | SNJ | Calls reload from file. |

## Input

8 methods. Static functions of a global table.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `freeze` | `Input.freeze(...)` | SNJ | Calls freeze. |
| `getPreviousState` | `Input.getPreviousState(arg1: integer, arg2: any): number` | SNJ | Returns the previous state. |
| `getState` | `Input.getState(arg1: integer, arg2: any): number` | SNJ | Returns the state. |
| `getStateDelta` | `Input.getStateDelta(arg1: integer, arg2: any): number` | SNJ | Returns the state delta. |
| `isConnected` | `Input.isConnected(arg1: any): boolean` | SNJ | Returns whether connected. |
| `setPreviousState` | `Input.setPreviousState(arg1: integer, arg2: number, arg3: any)` | SNJ | Sets the previous state. |
| `setState` | `Input.setState(arg1: integer, arg2: number, arg3: any)` | SNJ | Sets the state. |
| `touchToViewPoint` | `Input.touchToViewPoint(arg1: integer, arg2: integer, arg3: any): (integer, integer, integer)` | J | Calls touch to view point. |

## LabelComponent

36 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `create` | `LabelComponent:create(...)` | SNJ | Calls create. |
| `getBottomColor` | `LabelComponent:getBottomColor(): (number, number, number, number)` | SNJ | Returns the bottom color. |
| `getCharacterSpacingOffset` | `LabelComponent:getCharacterSpacingOffset(): integer` | SNJ | Returns the character spacing offset. |
| `getFlags` | `LabelComponent:getFlags(): number` | SNJ | Returns the flags. |
| `getFontResource` | `LabelComponent:getFontResource()` | SNJ | Returns the font resource. |
| `getLineHeightOffset` | `LabelComponent:getLineHeightOffset(): integer` | SNJ | Returns the line height offset. |
| `getPivot` | `LabelComponent:getPivot(): (number, number)` | SNJ | Returns the pivot. |
| `getShadowColor` | `LabelComponent:getShadowColor(): (number, number, number, number)` | SNJ | Returns the shadow color. |
| `getShadowOffset` | `LabelComponent:getShadowOffset(): (number, number)` | SNJ | Returns the shadow offset. |
| `getText` | `LabelComponent:getText(): string` | SNJ | Returns the text. |
| `getTextOffset` | `LabelComponent:getTextOffset(): (number, number)` | SNJ | Returns the text offset. |
| `getTextScale` | `LabelComponent:getTextScale(): (number, number)` | SNJ | Returns the text scale. |
| `getTopColor` | `LabelComponent:getTopColor(): (number, number, number, number)` | SNJ | Returns the top color. |
| `getWrapWidth` | `LabelComponent:getWrapWidth(): integer` | SNJ | Returns the wrap width. |
| `hasShadow` | `LabelComponent:hasShadow(): boolean` | SNJ | Returns whether shadow. |
| `hasWordWrap` | `LabelComponent:hasWordWrap(): boolean` | SNJ | Returns whether word wrap. |
| `isMonospaced` | `LabelComponent:isMonospaced(): boolean` | SNJ | Returns whether monospaced. |
| `refreshText` | `LabelComponent:refreshText()` | SNJ | Calls refresh text. |
| `refreshTextAll` | `LabelComponent:refreshTextAll(...)` | SNJ | Calls refresh text all. |
| `setBottomColor` | `LabelComponent:setBottomColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | Sets the bottom color. |
| `setCharacterSpacingOffset` | `LabelComponent:setCharacterSpacingOffset(characterSpacingOffset: integer)` | SNJ | Sets the character spacing offset. |
| `setFlags` | `LabelComponent:setFlags(flags: integer)` | SNJ | Sets the flags. |
| `setFontResource` | `LabelComponent:setFontResource(fontResource: FontResource)` | SNJ | Sets the font resource. |
| `setHasShadow` | `LabelComponent:setHasShadow(hasShadow: boolean)` | SNJ | Sets the has shadow. |
| `setLineHeightOffset` | `LabelComponent:setLineHeightOffset(lineHeightOffset: integer)` | SNJ | Sets the line height offset. |
| `setLocalIntVariable` | `LabelComponent:setLocalIntVariable(arg1: integer, arg2: any)` | SNJ | Sets the local int variable. |
| `setLocalVariable` | `LabelComponent:setLocalVariable(arg1: any, arg2: any)` | SNJ | Sets the local variable. |
| `setMonospaced` | `LabelComponent:setMonospaced(monospaced: boolean)` | SNJ | Sets the monospaced. |
| `setShadowColor` | `LabelComponent:setShadowColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | Sets the shadow color. |
| `setShadowOffset` | `LabelComponent:setShadowOffset(arg1: number, arg2: number)` | SNJ | Sets the shadow offset. |
| `setText` | `LabelComponent:setText(text: string)` | SNJ | Sets the text. |
| `setTextFromStringId` | `LabelComponent:setTextFromStringId(textFromStringId: string)` | SNJ | Sets the text from string id. |
| `setTextOffset` | `LabelComponent:setTextOffset(arg1: number, arg2: number)` | SNJ | Sets the text offset. |
| `setTextScale` | `LabelComponent:setTextScale(arg1: number, arg2: number)` | SNJ | Sets the text scale. |
| `setTopColor` | `LabelComponent:setTopColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | Sets the top color. |
| `setWrapWidth` | `LabelComponent:setWrapWidth(wrapWidth: integer)` | SNJ | Sets the wrap width. |

## Localization

6 methods. Static functions of a global table.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getLocale` | `Localization.getLocale(...): (string, string, integer)` | SNJ | Returns the locale. |
| `getText` | `Localization.getText(arg1: string): string` | SNJ | Returns the text. |
| `getUserLocale` | `Localization.getUserLocale(...): (string, string, integer)` | SNJ | Returns the user locale. |
| `reloadStrings` | `Localization.reloadStrings(...): number` | SNJ | Calls reload strings. |
| `setLocale` | `Localization.setLocale(arg1: integer, arg2: any, arg3: any)` | SNJ | Sets the locale. |
| `useUserLocale` | `Localization.useUserLocale(...)` | SNJ | Calls use user locale. |

## MeshComponent

5 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `create` | `MeshComponent:create(...)` | SNJ | Calls create. |
| `getTexture` | `MeshComponent:getTexture()` | SNJ | Returns the texture. |
| `getTrianglesCount` | `MeshComponent:getTrianglesCount(): integer` | SNJ | Returns the triangles count. |
| `setTexture` | `MeshComponent:setTexture(texture: Resource)` | SNJ | Sets the texture. |
| `setTriangles` | `MeshComponent:setTriangles(...)` | SNJ | Sets the triangles. |

## Object

2 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getType` | `Object:getType()` | SNJ | Returns the type. |
| `isInstanceOf` | `Object:isInstanceOf(arg1: any): boolean` | SNJ | Returns whether instance of. |

## Player

3 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getLastLoadResult` | `Player:getLastLoadResult(...): number` | J | Returns the last load result. |
| `getListeningPort` | `Player:getListeningPort(...): integer` | J | Returns the listening port. |
| `hasLoadError` | `Player:hasLoadError(...): boolean` | J | Returns whether load error. |

## RawResource

1 method. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getContent` | `RawResource:getContent()` | SNJ | Returns the content. |

## RenderTargetResource

2 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getPixel` | `RenderTargetResource:getPixel(arg1: number, arg2: number): (number, number, number, number)` | SN | Returns the pixel. |
| `getSize` | `RenderTargetResource:getSize(): (integer, integer)` | SNJ | Returns the size. |

## Resource

2 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `loadResourceConfiguration` | `Resource:loadResourceConfiguration(): number` | SNJ | Calls load resource configuration. |
| `synchronize` | `Resource:synchronize(...)` | SNJ | Calls synchronize. |

## Scene

1 method. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `instantiate` | `Scene:instantiate()` | SNJ | Calls instantiate. |

## SceneAnimation

1 method. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getDuration` | `SceneAnimation:getDuration(): number` | SNJ | Returns the duration. |

## ScriptComponent

1 method. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `create` | `ScriptComponent:create(...)` | SNJ | Calls create. |

## SoundComponent

36 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `closeNativeDevice` | `SoundComponent:closeNativeDevice(...)` | SJ | Calls close native device. |
| `create` | `SoundComponent:create(...)` | SNJ | Calls create. |
| `getMasterVolume` | `SoundComponent:getMasterVolume(...): number` | SNJ | Returns the master volume. |
| `getMaxDistance` | `SoundComponent:getMaxDistance(): number` | SNJ | Returns the max distance. |
| `getMinDistance` | `SoundComponent:getMinDistance(): number` | SNJ | Returns the min distance. |
| `getPan` | `SoundComponent:getPan(): number` | SNJ | Returns the pan. |
| `getPitch` | `SoundComponent:getPitch(): number` | SNJ | Returns the pitch. |
| `getPriority` | `SoundComponent:getPriority(): integer` | SNJ | Returns the priority. |
| `getSamplePosition` | `SoundComponent:getSamplePosition(): number` | SNJ | Returns the sample position. **Note:** Returns 0.0 when the component has no native sound object; it does not raise an error. |
| `getSoundResource` | `SoundComponent:getSoundResource()` | SNJ | Returns the sound resource. |
| `getTimePosition` | `SoundComponent:getTimePosition(): number` | SNJ | Returns the time position. |
| `getVolume` | `SoundComponent:getVolume(): number` | SNJ | Returns the volume. |
| `isAutoPlay` | `SoundComponent:isAutoPlay(): boolean` | SNJ | Returns whether auto play. |
| `isLooped` | `SoundComponent:isLooped(): boolean` | SNJ | Returns whether looped. |
| `isMuted` | `SoundComponent:isMuted(...): boolean` | SNJ | Returns whether muted. |
| `isPaused` | `SoundComponent:isPaused(): boolean` | SNJ | Returns whether paused. |
| `isPlaying` | `SoundComponent:isPlaying(): boolean` | SNJ | Returns whether playing. **Note:** Returns false when the component has no native sound object (for example a disabled one); it does not raise an error. |
| `isPositional` | `SoundComponent:isPositional(): boolean` | SNJ | Returns whether positional. |
| `isStoppedWhenDisabled` | `SoundComponent:isStoppedWhenDisabled(): boolean` | SNJ | Returns whether stopped when disabled. |
| `pause` | `SoundComponent:pause()` | SNJ | Calls pause. |
| `play` | `SoundComponent:play(): number` | SNJ | Calls play. |
| `playOneShot` | `SoundComponent:playOneShot(arg1: number, arg2: number, arg3: number)` | SNJ | Calls play one shot. |
| `setAutoPlay` | `SoundComponent:setAutoPlay(autoPlay: boolean)` | SNJ | Sets the auto play. |
| `setLoop` | `SoundComponent:setLoop(loop: boolean)` | SNJ | Sets the loop. |
| `setMasterVolume` | `SoundComponent:setMasterVolume()` | SNJ | Sets the master volume. |
| `setMaxDistance` | `SoundComponent:setMaxDistance(maxDistance: number)` | SNJ | Sets the max distance. |
| `setMinDistance` | `SoundComponent:setMinDistance(minDistance: number)` | SNJ | Sets the min distance. |
| `setMute` | `SoundComponent:setMute()` | SNJ | Sets the mute. |
| `setPan` | `SoundComponent:setPan(pan: number)` | SNJ | Sets the pan. |
| `setPitch` | `SoundComponent:setPitch(pitch: number)` | SNJ | Sets the pitch. |
| `setPositional` | `SoundComponent:setPositional(positional: boolean)` | SNJ | Sets the positional. |
| `setPriority` | `SoundComponent:setPriority(priority: integer)` | SNJ | Sets the priority. |
| `setSoundResource` | `SoundComponent:setSoundResource(soundResource: SoundResource)` | SNJ | Sets the sound resource. **Note:** The argument must be a loaded SoundResource; otherwise the engine raises 'resource (SoundResource) is not loaded'. |
| `setStopWhenDisabled` | `SoundComponent:setStopWhenDisabled(stopWhenDisabled: boolean)` | SNJ | Sets the stop when disabled. |
| `setVolume` | `SoundComponent:setVolume(volume: number)` | SNJ | Sets the volume. |
| `stop` | `SoundComponent:stop()` | SNJ | Calls stop. |

## SoundListenerComponent

1 method. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `create` | `SoundListenerComponent:create(...)` | SNJ | Calls create. |

## SoundResource

3 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getLength` | `SoundResource:getLength(): number` | SNJ | Returns the length. |
| `getSampleCount` | `SoundResource:getSampleCount(): number` | SNJ | Returns the sample count. |
| `getSampleRate` | `SoundResource:getSampleRate(): number` | SNJ | Returns the sample rate. |

## SpriteAnimationResource

1 method. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getFrameCount` | `SpriteAnimationResource:getFrameCount(): number` | SNJ | Returns the frame count. |

## SpriteComponent

11 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `create` | `SpriteComponent:create(...)` | SNJ | Calls create. |
| `getPivot` | `SpriteComponent:getPivot(): (number, number)` | SNJ | Returns the pivot. |
| `getSize` | `SpriteComponent:getSize(): (number, number)` | SNJ | Returns the size. |
| `getSprite` | `SpriteComponent:getSprite()` | SNJ | Returns the sprite. |
| `isFlippedHorizontal` | `SpriteComponent:isFlippedHorizontal(): boolean` | SNJ | Returns whether flipped horizontal. |
| `isFlippedVertical` | `SpriteComponent:isFlippedVertical(): boolean` | SNJ | Returns whether flipped vertical. |
| `resetSize` | `SpriteComponent:resetSize()` | SNJ | Calls reset size. |
| `setFlipHorizontal` | `SpriteComponent:setFlipHorizontal(flipHorizontal: boolean)` | SNJ | Sets the flip horizontal. |
| `setFlipVertical` | `SpriteComponent:setFlipVertical(flipVertical: boolean)` | SNJ | Sets the flip vertical. |
| `setSize` | `SpriteComponent:setSize(arg1: number, arg2: number)` | SNJ | Sets the size. |
| `setSprite` | `SpriteComponent:setSprite(sprite: SpriteResource)` | SNJ | Sets the sprite. |

## SpriteResource

3 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getPivot` | `SpriteResource:getPivot(): (number, number)` | SNJ | Returns the pivot. |
| `getSize` | `SpriteResource:getSize(): (integer, integer)` | SNJ | Returns the size. |
| `getTextureResource` | `SpriteResource:getTextureResource()` | SNJ | Returns the texture resource. |

## TextVariable

3 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getVariable` | `TextVariable:getVariable(): (string, number, integer)` | SNJ | Returns the variable. |
| `setIntVariable` | `TextVariable:setIntVariable(intVariable: integer)` | SNJ | Sets the int variable. |
| `setVariable` | `TextVariable:setVariable(variable: any)` | SNJ | Sets the variable. |

## TextureComponent

19 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `create` | `TextureComponent:create(...)` | SNJ | Calls create. |
| `getPivot` | `TextureComponent:getPivot(): (number, number)` | SNJ | Returns the pivot. |
| `getSize` | `TextureComponent:getSize(): (number, number)` | SNJ | Returns the size. |
| `getTexture` | `TextureComponent:getTexture()` | SNJ | Returns the texture. |
| `getTextureOffset` | `TextureComponent:getTextureOffset(): (number, number)` | SNJ | Returns the texture offset. |
| `getTextureRepeat` | `TextureComponent:getTextureRepeat(): (number, number)` | SNJ | Returns the texture repeat. |
| `resetSize` | `TextureComponent:resetSize()` | SNJ | Calls reset size. |
| `setCurrentFrame` | `TextureComponent:setCurrentFrame(currentFrame: integer)` | J | Sets the current frame. |
| `setHeight` | `TextureComponent:setHeight(height: number)` | SJ | Sets the height. |
| `setPivot` | `TextureComponent:setPivot(arg1: number, arg2: number)` | SNJ | Sets the pivot. |
| `setSize` | `TextureComponent:setSize(arg1: number, arg2: number)` | SNJ | Sets the size. |
| `setTexture` | `TextureComponent:setTexture(texture: Resource)` | SNJ | Sets the texture. |
| `setTextureOffset` | `TextureComponent:setTextureOffset(arg1: number, arg2: number)` | SNJ | Sets the texture offset. |
| `setTextureOffsetX` | `TextureComponent:setTextureOffsetX(textureOffsetX: number)` | SJ | Sets the texture offset x. |
| `setTextureOffsetY` | `TextureComponent:setTextureOffsetY(textureOffsetY: number)` | SJ | Sets the texture offset y. |
| `setTextureRepeat` | `TextureComponent:setTextureRepeat(arg1: number, arg2: number)` | SNJ | Sets the texture repeat. |
| `setTextureRepeatX` | `TextureComponent:setTextureRepeatX(textureRepeatX: number)` | SJ | Sets the texture repeat x. |
| `setTextureRepeatY` | `TextureComponent:setTextureRepeatY(textureRepeatY: number)` | SJ | Sets the texture repeat y. |
| `setWidth` | `TextureComponent:setWidth(width: number)` | SJ | Sets the width. |

## TextureResource

2 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getPixel` | `TextureResource:getPixel(arg1: number, arg2: number): (number, number, number, number)` | SN | Returns the pixel. |
| `getSize` | `TextureResource:getSize(): (integer, integer)` | SNJ | Returns the size. |

## TilemapComponent

7 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `create` | `TilemapComponent:create(...)` | SNJ | Calls create. |
| `getTileGridSize` | `TilemapComponent:getTileGridSize(): (integer, integer)` | SNJ | Returns the tile grid size. |
| `getTileSizeScreen` | `TilemapComponent:getTileSizeScreen(): (number, number)` | SNJ | Returns the tile size screen. |
| `getTileSizeTexture` | `TilemapComponent:getTileSizeTexture(): (number, number)` | SNJ | Returns the tile size texture. |
| `setTileGridSize` | `TilemapComponent:setTileGridSize(arg1: integer, arg2: integer)` | SNJ | Sets the tile grid size. |
| `setTileSizeScreen` | `TilemapComponent:setTileSizeScreen(arg1: number, arg2: number)` | SNJ | Sets the tile size screen. |
| `setTileSizeTexture` | `TilemapComponent:setTileSizeTexture(arg1: number, arg2: number)` | SNJ | Sets the tile size texture. |

## VideoComponent

18 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `close` | `VideoComponent:close(0 args)` | N | Calls close. |
| `create` | `VideoComponent:create(? args)` | N | Calls create. |
| `getCurrentTime` | `VideoComponent:getCurrentTime(0 args)` | N | Returns the current time. |
| `getCurrentTimeAsSeconds` | `VideoComponent:getCurrentTimeAsSeconds(0 args)` | N | Returns the current time as seconds. |
| `getLength` | `VideoComponent:getLength(0 args)` | N | Returns the length. |
| `getLengthAsSeconds` | `VideoComponent:getLengthAsSeconds(0 args)` | N | Returns the length as seconds. |
| `getState` | `VideoComponent:getState(0 args)` | N | Returns the state. |
| `isAutoPlay` | `VideoComponent:isAutoPlay(0 args)` | N | Returns whether auto play. |
| `open` | `VideoComponent:open(1 args)` | N | Calls open. |
| `pause` | `VideoComponent:pause(0 args)` | N | Calls pause. |
| `play` | `VideoComponent:play(0 args)` | N | Calls play. |
| `resume` | `VideoComponent:resume(0 args)` | N | Calls resume. |
| `seek` | `VideoComponent:seek(1 args)` | N | Calls seek. |
| `seekAsSeconds` | `VideoComponent:seekAsSeconds(1 args)` | N | Calls seek as seconds. |
| `setAutoPlay` | `VideoComponent:setAutoPlay(1 args)` | N | Sets the auto play. |
| `setAutoresize` | `VideoComponent:setAutoresize(1 args)` | N | Sets the autoresize. |
| `setSize` | `VideoComponent:setSize(2 args)` | N | Sets the size. |
| `stop` | `VideoComponent:stop(0 args)` | N | Calls stop. |

## VisualComponent

31 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getAlpha` | `VisualComponent:getAlpha(): number` | SNJ | Returns the alpha. |
| `getBlendPreset` | `VisualComponent:getBlendPreset(): integer` | SNJ | Returns the blend preset. |
| `getColor` | `VisualComponent:getColor(): (number, number, number, number)` | SNJ | Returns the color. |
| `getColorB` | `VisualComponent:getColorB(): number` | SNJ | Returns the color b. |
| `getColorG` | `VisualComponent:getColorG(): number` | SNJ | Returns the color g. |
| `getColorR` | `VisualComponent:getColorR(): number` | SNJ | Returns the color r. |
| `getLayer` | `VisualComponent:getLayer(): integer` | SNJ | Returns the layer. |
| `getSelfAlpha` | `VisualComponent:getSelfAlpha(): number` | SJ | Returns the self alpha. |
| `getSelfColor` | `VisualComponent:getSelfColor(): (number, number, number, number)` | SJ | Returns the self color. |
| `getSelfColorB` | `VisualComponent:getSelfColorB(): number` | SJ | Returns the self color b. |
| `getSelfColorG` | `VisualComponent:getSelfColorG(): number` | SJ | Returns the self color g. |
| `getSelfColorR` | `VisualComponent:getSelfColorR(): number` | SJ | Returns the self color r. |
| `getSize` | `VisualComponent:getSize(): (number, number)` | SNJ | Returns the size. |
| `getWorldZIndex` | `VisualComponent:getWorldZIndex(): integer` | SNJ | Returns the world zindex. |
| `getZIndex` | `VisualComponent:getZIndex(): integer` | SNJ | Returns the zindex. |
| `isCulled` | `VisualComponent:isCulled(): boolean` | SNJ | Returns whether culled. |
| `isSelfVisible` | `VisualComponent:isSelfVisible(): boolean` | SJ | Returns whether self visible. |
| `isVisible` | `VisualComponent:isVisible(): boolean` | SJ | Returns whether visible. |
| `setAlpha` | `VisualComponent:setAlpha(alpha: number)` | SNJ | Sets the alpha. |
| `setBlendPreset` | `VisualComponent:setBlendPreset(blendPreset: integer)` | SNJ | Sets the blend preset. |
| `setColor` | `VisualComponent:setColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SNJ | Sets the color. |
| `setColorB` | `VisualComponent:setColorB(colorB: number)` | SNJ | Sets the color b. |
| `setColorG` | `VisualComponent:setColorG(colorG: number)` | SNJ | Sets the color g. |
| `setColorR` | `VisualComponent:setColorR(colorR: number)` | SNJ | Sets the color r. |
| `setFilters` | `VisualComponent:setFilters(arg1: integer, arg2: integer)` | SNJ | Sets the filters. |
| `setLayer` | `VisualComponent:setLayer(layer: integer)` | SNJ | Sets the layer. |
| `setSamplerSettings` | `VisualComponent:setSamplerSettings(arg1: integer, arg2: integer, arg3: integer, arg4: integer)` | SNJ | Sets the sampler settings. |
| `setVisible` | `VisualComponent:setVisible(visible: boolean)` | SJ | Sets the visible. |
| `setWorldZIndex` | `VisualComponent:setWorldZIndex(worldZIndex: integer)` | SNJ | Sets the world zindex. |
| `setWrapModes` | `VisualComponent:setWrapModes(arg1: integer, arg2: integer)` | SNJ | Sets the wrap modes. |
| `setZIndex` | `VisualComponent:setZIndex(zIndex: integer)` | SNJ | Sets the zindex. |

## Volumes

8 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `getBootApplicationPath` | `Volumes:getBootApplicationPath(...)` | J | Returns the boot application path. |
| `getPath` | `Volumes:getPath()` | J | Returns the path. |
| `getSyncApplicationPath` | `Volumes:getSyncApplicationPath(...)` | J | Returns the sync application path. |
| `getSystemPath` | `Volumes:getSystemPath(...)` | J | Returns the system path. |
| `getTempPath` | `Volumes:getTempPath(...)` | J | Returns the temp path. |
| `getUserPath` | `Volumes:getUserPath(...)` | J | Returns the user path. |
| `isVolumeMounted` | `Volumes:isVolumeMounted(): boolean` | J | Returns whether volume mounted. |
| `mountDataVolume` | `Volumes:mountDataVolume(arg1: string): number` | J | Calls mount data volume. |

## WorldNode

76 methods. Instance methods.

| Method | Signature | Families | Summary |
|---|---|---|---|
| `addChildNode` | `WorldNode:addChildNode(arg1: any): number` | SNJ | Calls add child node. |
| `addHierarchyToNode` | `WorldNode:addHierarchyToNode(arg1: any): number` | SNJ | Calls add hierarchy to node. |
| `addHierarchyToRoot` | `WorldNode:addHierarchyToRoot(): number` | SNJ | Calls add hierarchy to root. |
| `attachComponent` | `WorldNode:attachComponent(arg1: any): number` | SNJ | Calls attach component. |
| `attachToWorld` | `WorldNode:attachToWorld(): number` | SNJ | Calls attach to world. |
| `create` | `WorldNode:create(...)` | SNJ | Calls create. |
| `destroy` | `WorldNode:destroy()` | SNJ | Calls destroy. |
| `detachComponent` | `WorldNode:detachComponent(arg1: any): number` | SNJ | Calls detach component. |
| `detachFromWorld` | `WorldNode:detachFromWorld(): number` | SNJ | Calls detach from world. |
| `disable` | `WorldNode:disable()` | SNJ | Calls disable. |
| `enable` | `WorldNode:enable()` | SNJ | Calls enable. |
| `getAllComponents` | `WorldNode:getAllComponents(): array` | SNJ | Returns the all components. |
| `getAlpha` | `WorldNode:getAlpha(): number` | SJ | Returns the alpha. |
| `getCategory` | `WorldNode:getCategory(): integer` | SNJ | Returns the category. |
| `getChildByName` | `WorldNode:getChildByName(arg1: any)` | SNJ | Returns the child by name. |
| `getColor` | `WorldNode:getColor(): (number, number, number, number)` | SJ | Returns the color. |
| `getComponent` | `WorldNode:getComponent(arg1: any)` | SNJ | Returns the component. |
| `getComponents` | `WorldNode:getComponents(arg1: any): array` | SNJ | Returns the components. |
| `getFirstChildNode` | `WorldNode:getFirstChildNode()` | SNJ | Returns the first child node. |
| `getLastChildNode` | `WorldNode:getLastChildNode()` | SNJ | Returns the last child node. |
| `getLocalPosition` | `WorldNode:getLocalPosition(): (number, number)` | SNJ | Returns the local position. |
| `getLocalPositionX` | `WorldNode:getLocalPositionX(): number` | SNJ | Returns the local position x. |
| `getLocalPositionY` | `WorldNode:getLocalPositionY(): number` | SNJ | Returns the local position y. |
| `getLocalRotation` | `WorldNode:getLocalRotation(): number` | SNJ | Returns the local rotation. |
| `getLocalScale` | `WorldNode:getLocalScale(): (number, number)` | SNJ | Returns the local scale. |
| `getLocalScaleX` | `WorldNode:getLocalScaleX(): number` | SNJ | Returns the local scale x. |
| `getLocalScaleY` | `WorldNode:getLocalScaleY(): number` | SNJ | Returns the local scale y. |
| `getLocalTransform` | `WorldNode:getLocalTransform(): (number, number, number, number, number, number)` | SNJ | Returns the local transform. |
| `getName` | `WorldNode:getName()` | SNJ | Returns the name. |
| `getParentNode` | `WorldNode:getParentNode()` | SNJ | Returns the parent node. |
| `getPreviousSiblingNode` | `WorldNode:getPreviousSiblingNode()` | SNJ | Returns the previous sibling node. |
| `getSelfAlpha` | `WorldNode:getSelfAlpha(): number` | SJ | Returns the self alpha. |
| `getSelfColor` | `WorldNode:getSelfColor(): (number, number, number, number)` | SJ | Returns the self color. |
| `getSiblingNode` | `WorldNode:getSiblingNode()` | SNJ | Returns the sibling node. |
| `getWorldPosition` | `WorldNode:getWorldPosition(): (number, number)` | SNJ | Returns the world position. |
| `getWorldRotation` | `WorldNode:getWorldRotation(): number` | SNJ | Returns the world rotation. |
| `getWorldScale` | `WorldNode:getWorldScale(): (number, number)` | SNJ | Returns the world scale. |
| `getWorldTransform` | `WorldNode:getWorldTransform(): (number, number, number, number, number, number)` | SNJ | Returns the world transform. |
| `getWorldZIndex` | `WorldNode:getWorldZIndex(): integer` | SNJ | Returns the world zindex. |
| `getXAxis` | `WorldNode:getXAxis(): (number, number)` | SNJ | Returns the xaxis. |
| `getYAxis` | `WorldNode:getYAxis(): (number, number)` | SNJ | Returns the yaxis. |
| `getZIndex` | `WorldNode:getZIndex(): integer` | SNJ | Returns the zindex. |
| `isDestroyed` | `WorldNode:isDestroyed(): boolean` | SNJ | Returns whether destroyed. |
| `isEnabled` | `WorldNode:isEnabled(): boolean` | SNJ | Returns whether enabled. |
| `isSelfEnabled` | `WorldNode:isSelfEnabled(): boolean` | SNJ | Returns whether self enabled. |
| `isSelfVisible` | `WorldNode:isSelfVisible(): boolean` | SJ | Returns whether self visible. |
| `isVisible` | `WorldNode:isVisible(): boolean` | SJ | Returns whether visible. |
| `localToWorldDirection` | `WorldNode:localToWorldDirection(arg1: number, arg2: number): (number, number)` | SNJ | Calls local to world direction. |
| `localToWorldPosition` | `WorldNode:localToWorldPosition(arg1: number, arg2: number): (number, number)` | SNJ | Calls local to world position. |
| `removeChildNode` | `WorldNode:removeChildNode(arg1: any): number` | SNJ | Calls remove child node. |
| `removeHierarchy` | `WorldNode:removeHierarchy(): number` | SNJ | Calls remove hierarchy. |
| `rotate` | `WorldNode:rotate(arg1: number)` | SNJ | Calls rotate. |
| `scale` | `WorldNode:scale(arg1: number, arg2: number)` | SNJ | Calls scale. |
| `setAlpha` | `WorldNode:setAlpha(alpha: number)` | SJ | Sets the alpha. |
| `setCategory` | `WorldNode:setCategory(category: integer)` | SNJ | Sets the category. |
| `setColor` | `WorldNode:setColor(arg1: number, arg2: number, arg3: number, arg4: number)` | SJ | Sets the color. |
| `setEnabled` | `WorldNode:setEnabled(enabled: boolean)` | SNJ | Sets the enabled. |
| `setLocalPosition` | `WorldNode:setLocalPosition(arg1: number, arg2: number)` | SNJ | Sets the local position. |
| `setLocalPositionX` | `WorldNode:setLocalPositionX(localPositionX: number)` | SNJ | Sets the local position x. |
| `setLocalPositionY` | `WorldNode:setLocalPositionY(localPositionY: number)` | SNJ | Sets the local position y. |
| `setLocalRotation` | `WorldNode:setLocalRotation(localRotation: number)` | SNJ | Sets the local rotation. |
| `setLocalScale` | `WorldNode:setLocalScale(arg1: number, arg2: number)` | SNJ | Sets the local scale. |
| `setLocalScaleX` | `WorldNode:setLocalScaleX(localScaleX: number)` | SNJ | Sets the local scale x. |
| `setLocalScaleY` | `WorldNode:setLocalScaleY(localScaleY: number)` | SNJ | Sets the local scale y. |
| `setLocalTransform` | `WorldNode:setLocalTransform(arg1: number, arg2: number, arg3: number, arg4: number, arg5: number, arg6: number)` | SNJ | Sets the local transform. |
| `setName` | `WorldNode:setName(name: any)` | SNJ | Sets the name. |
| `setNewParent` | `WorldNode:setNewParent(...)` | SNJ | Sets the new parent. |
| `setVisible` | `WorldNode:setVisible(visible: boolean)` | SJ | Sets the visible. |
| `setWorldPosition` | `WorldNode:setWorldPosition(arg1: number, arg2: number)` | SNJ | Sets the world position. |
| `setWorldRotation` | `WorldNode:setWorldRotation(worldRotation: number)` | SNJ | Sets the world rotation. |
| `setWorldTransform` | `WorldNode:setWorldTransform(arg1: number, arg2: number, arg3: number, arg4: number, arg5: number, arg6: number)` | SNJ | Sets the world transform. |
| `setWorldZIndex` | `WorldNode:setWorldZIndex(worldZIndex: integer)` | SNJ | Sets the world zindex. |
| `setZIndex` | `WorldNode:setZIndex(zIndex: integer)` | SNJ | Sets the zindex. |
| `translate` | `WorldNode:translate(arg1: number, arg2: number)` | SNJ | Calls translate. |
| `worldToLocalDirection` | `WorldNode:worldToLocalDirection(arg1: number, arg2: number): (number, number)` | SNJ | Calls world to local direction. |
| `worldToLocalPosition` | `WorldNode:worldToLocalPosition(arg1: number, arg2: number): (number, number)` | SNJ | Calls world to local position. |
