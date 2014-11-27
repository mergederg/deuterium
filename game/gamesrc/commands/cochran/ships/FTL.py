"""
Controls for FTL engines.
"""

from ev import Command as BaseCommand
from ev import default_cmds
from ev import utils

class FTLCommand(BaseCommand):
    """
    Run a scan.  This shows everything in space within the craft's sensor range.
    """

    # Command information.
    key = "jump"
    aliases = ["hyperspace"]
    locks = "cmd:all()"
    help_category = "Cochran - Ships"

    def at_pre_cmd(self):
        pass

    def parse(self):
        # TODO: Parse the command.

        # Find out what user the ship is in.
        # Find its range.  Ask space what objects are within sensor range.
        # Display those in a table.
        pass