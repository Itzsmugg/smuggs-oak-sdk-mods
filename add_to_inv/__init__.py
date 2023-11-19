# Reordered imports
from argparse import Namespace
import mods_base

# Ensuring the SDK version is up-to-date
assert mods_base.__version_info__ >= (1, 0), "Please update the SDK"

# Version information
__version__: str
__version_info__: tuple[int, ...]

@command("add_to_inv", description="Adds the \"add_to_inv\" command to add a serial code from a save editor.")
def add_to_inv(args: Namespace) -> None:
    """
    Adds the specified serial code to the player's inventory.

    Args:
        args (Namespace): The parsed command-line arguments.
    """
    pc = get_pc()
    serial_code = args.serial_code

    # Extracting serial code if wrapped in parentheses
    if "(" in serial_code and ")" in serial_code:
        start = serial_code.find("(") + 1
        end = serial_code.find(")")
        serial_code = serial_code[start:end]

    print(f"Adding serial code {serial_code} to inventory")

    # Adding serial code based on the game
    if Game.get_current() is Game.BL3:
        pc.ServerAddGearToInventory(serial_code, 0)
    elif Game.get_current() is Game.WL:
        pc.ServerAddGearToInventory(serial_code, 0, 0)

    print("Successfully added to inventory")

# Adding argument description for serial_code
add_to_inv.add_argument("serial_code", help="Params are `add_to_inv SERIALCODE FROM SAVE EDITOR`")

# Building the mod
build_mod()