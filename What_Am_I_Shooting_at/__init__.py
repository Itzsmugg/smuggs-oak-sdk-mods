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
from .display import auto_enable, draw, display_toggle, on_screen_size
from .data import  print_to_log_bool

__version__: str
__version_info__: tuple[int, ...]





@hook("/Script/Engine.PlayerController:ServerNotifyLoadedWorld", Type.POST)
def ServerNotifyLoadedWorld(obj: UObject, args: WrappedStruct, _3: Any, _4: BoundFunction) -> None:
    if auto_enable.value:
        draw.enable()

build_mod(
    keybinds=[
        display_toggle,
    ],
    options=[
        auto_enable,
        on_screen_size,
        print_to_log_bool,
    ]
)
