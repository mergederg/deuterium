"""
Fire one, some or all of a ship's weapons at a target.
"""

from ev import Command as BaseCommand
from ev import default_cmds
from ev import utils

class FireCommand(BaseCommand):
    """
    Run a scan.  This shows everything in space within the craft's sensor range.
    """

    # Command information.
    key = "fire"
    aliases = ["engage"]
    locks = "cmd:all()"
    help_category = "Cochran - Ships"

    def at_pre_cmd(self):
        pass

    def parse(self):
        # TODO: Parse the command.
        # Find out what user the ship is in.
        # Is the input sane?  Trying to fire any weapons they don't have?
        # Return combat results to space.
        pass