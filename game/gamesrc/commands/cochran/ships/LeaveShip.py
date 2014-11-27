"""
Leave a ship.  Pretty much the inverse of boarding a ship.  ;)
"""

from ev import Command as BaseCommand
from ev import default_cmds
from ev import utils

class BoardShipCommand(BaseCommand):
    """
    Board a ship.
    """

    # Command information.
    key = "unboard"
    aliases = ["disembark"]
    locks = "cmd:all()"
    help_category = "Cochran - Ships"

    def at_pre_cmd(self):
        pass

    def parse(self):
        # TODO: Parse the command.

        # Two arguments -- what ship, and the entry password.
        targetShip = self.args[0];
        userPassword = self.args[1];

        # Find out what ship is the user trying to board.
        # Do they have the password right?
        # Is the caller in the same room as the ship?
        # If so, allow user in.
        pass