if True:
    assert __import__("mods_base").__version_info__ >= (1, 0), "Please update the SDK"

from argparse import Namespace  
from mods_base import get_pc, build_mod, command, Game

__version__: str
__version_info__: tuple[int, ...]

@command("add_to_inv", 
         description="Adds the 'add_to_inv' command to add a serial code from a save editor.`")
def add_to_inv(args: Namespace) -> None:
    pc = get_pc()
    serial_code = args.serial_code

    if '(' in serial_code and ')' in serial_code:
        start = serial_code.find('(') + 1
        end = serial_code.find(')')
        serial_code = serial_code[start:end]

    print(f"Adding serial code {serial_code} to inventory")

    if Game.get_current() is Game.BL3:
        pc.ServerAddGearToInventory(serial_code, 0) 
    elif Game.get_current() is Game.WL:
        pc.ServerAddGearToInventory(serial_code, 0, 0)

    print("Successfully added to inventory")



add_to_inv.add_argument("serial_code", help="Params are `add_to_inv SERIALCODE FROM SAVE EDITOR")


build_mod()
