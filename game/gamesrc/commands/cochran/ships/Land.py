"""
Land a ship.
"""

from ev import Command as BaseCommand
from ev import default_cmds
from ev import utils

class LandShipCommand(BaseCommand):
    """
    Board a ship.
    """

    # Command information.
    key = "land"
    aliases = ["landship"]
    locks = "cmd:all()"
    help_category = "Cochran - Ships"

    def at_pre_cmd(self):
        pass

    def parse(self):
        # TODO: Parse the command.
        # Is the ship already taken off?
        # Is the target valid?
        # Is the target in range?
        # If so, land the target
        pass