# ruff: noqa: D103
if True:
    assert __import__("mods_base").__version_info__ >= (1, 1), "Please update the SDK"

from re import T
from mods_base.keybinds import keybind
from mods_base.options import BoolOption, SliderOption
import unrealsdk
from mods_base import build_mod, hook, get_pc
from typing import Any
from unrealsdk.hooks import Type, Block
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct, WrappedArray
from .display import  draw, display_toggle, set_display_on, hud_display_group
from .data import  print_to_log_bool, OnImpact

__version__: str
__version_info__: tuple[int, ...]





@hook("/Script/Engine.PlayerController:ServerNotifyLoadedWorld", Type.POST)
def ServerNotifyLoadedWorld(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:
    if auto_enable.value:
        draw.enable()
        set_display_on(True)

build_mod(
    keybinds=[
        display_toggle,
    ],
    options=[
        print_to_log_bool,
        hud_display_group,
    ]
)
display.draw.disable()
data.OnImpact.enable()