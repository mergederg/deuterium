from ev import Command, CmdSet


class ShipCommandSet(CmdSet):
    """
    This command set gets attached to all ships via the ship computer.  They are accessible to anyone in the cockpit.
    """
    def at_cmdset_creation(self):
        self.add(TakeOffCmd)
        self.add(LandCmd)
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


class LandCmd(Command):
    """
    Lands a ship.
    """
    key = "+ship/land"

    def parse(self):
        # Parse command here for execution.
        pass

    def func(self):
        # Execute command here.
        pass

