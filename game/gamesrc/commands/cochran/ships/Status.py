"""
Status command.
"""

from ev import Command as BaseCommand
from ev import default_cmds
from ev import utils

class StatusCommand(BaseCommand):
    """
    Run a scan.  This shows everything in space within the craft's sensor range.
    """

    # Command information.
    key = "status"
    aliases = ["shipstat"]
    locks = "cmd:all()"
    help_category = "Cochran - Ships"

    def at_pre_cmd(self):
        pass

    def parse(self):
        # TODO: Parse the command.
        pass