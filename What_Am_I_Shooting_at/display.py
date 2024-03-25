from .data import get_text
from mods_base.keybinds import keybind
from mods_base.options import BoolOption, GroupedOption, SliderOption
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

draw_x = SliderOption(identifier="draw_x", display_name="HUD Display X", value=10, min_value=0, max_value=1600, is_integer=False)
draw_y = SliderOption(identifier="HUD Display Y", display_name="HUD Display Y", value=10, min_value=0, max_value=1000, is_integer=False)
on_screen_size = SliderOption("HUD Display Font Size", 0, 0, 100, is_integer=True) 


auto_enable = BoolOption(
    "Auto Enable On",
    False,
    description="Auto Enable Without Keybind",
)
hud_display_group = GroupedOption(
    "HUD Display Options",
    [auto_enable, draw_x, draw_y, on_screen_size],
)

display_on = None

def set_display_on(value: bool) -> None:
    global display_on
    display_on = value

@keybind("display on/off")
def display_toggle() -> None:
    global display_on

    if display_on is not True:
        draw.enable()
        display_on = True
    else:
        draw.disable()
        display_on = False



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

        
        obj.DrawText(get_text(), YELLOW, draw_x.value, draw_y.value, FONT, 0.5 + on_screen_size.value / 100, False)





