"""
Take off in a ship, either from
"""

from ev import Command as BaseCommand
from ev import default_cmds
from ev import utils

class LandShipCommand(BaseCommand):
    """
    Board a ship.
    """

    # Command information.
    key = "takeoff"
    aliases = ["unland"]
    locks = "cmd:all()"
    help_category = "Cochran - Ships"

    def at_pre_cmd(self):
        pass

    def parse(self):
        # TODO: Parse the command.
        # Is the ship landed now?
        # If so, take off.  Put the ship in space next to wherever it took off from.
        pass