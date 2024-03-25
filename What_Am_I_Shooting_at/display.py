from .data import get_text
from mods_base.keybinds import keybind
from mods_base.options import BoolOption, SliderOption
import unrealsdk
from mods_base import  hook, get_pc
from typing import Any
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct, WrappedArray



YELLOW = unrealsdk.make_struct("LinearColor", R=1, G=1, B=0, A=1)
FONT = unrealsdk.construct_object(unrealsdk.find_class("Font"), unrealsdk.find_class("Font").Outer, "NEWFONT", 0, unrealsdk.find_object("Font", "/Game/UI/_Shared/Fonts/OAK_BODY.OAK_BODY")) 
FONT.LegacyFontSize += 30
CLASS = "NONE"
NAME = "NONE"
TEXT = "NONE"


on_screen_size = SliderOption("HUD Display Font Size", 0, 0, 100, is_integer=True) 

auto_enable = BoolOption(
    "Auto Enable On",
    False,
    description="Auto Enable Without Keybind",
)

display_on = False

@keybind("display on/off")
def display_toggle() -> None:
    global display_on
    display_on = not display_on

    if display_on:
        draw.enable()
    else:
        draw.disable()


@hook(
    "/Script/Engine.HUD:ReceiveDrawHUD",
    Type.POST,
    auto_enable=False,
)
def draw(
    obj: UObject,
    _2: WrappedStruct,
    _3: Any,
    _4: BoundFunction,
) -> None:

        
        obj.DrawText(get_text(), YELLOW, 10, 10, FONT, 0.5 + on_screen_size.value / 100, False)





