from ev import Command, CmdSet


class ShipCommandSet(CmdSet):
    """
    This command set gets attached to all ships via the ship computer.  They are accessible to anyone in the cockpit.
    """
    def at_cmdset_creation(self):
        self.add(TakeOffCmd)
        self.add(LandShipCmd)
        pass


class BoardShipCommand(Command):
    """
    Board a ship.
    """

    # Command information.
    key = "board"
    aliases = ["enter"]
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


class LeaveShip(Command):
    """
    Leave a Ship.
    """

    # TODO: To be available outside of the ship, this command is gonna have to be global.

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
        targetShip = self.args[0]
        userPassword = self.args[1]

        # Find out what ship is the user trying to board.
        # Do they have the password right?
        # Is the caller in the same room as the ship?
        # If so, allow user in.
        pass


class TakeOffCmd(Command):
    """
    Take off in a ship, departing its current landing zone.
    """
    key = "+ship/takeoff"

    def parse(self):
        # Parse command here for execution.
        pass

    def func(self):
        # Execute command here.
        pass


class LandShipCmd(Command):
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


class StatusCommand(Command):
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


class FireCommand(Command):
    """
    The simplest combat command.  Immediately fires all weapons at the targeted craft.
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