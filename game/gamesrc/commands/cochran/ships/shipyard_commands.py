from ev import Command, CmdSet


class ShipCommandSet(CmdSet):
    def at_cmdset_creation(self):
        self.add(BuildShipCmd)
        pass


class BuildShipCmd(Command):
    """
    Build a ship.  The ship must be of a type that can be constructed by the relevant shipyard.
    """
    key = "+shipyard/build"
    help_category = "Shipyard Commands"

    def parse(self):
        # Parse command here for execution.
        pass

    def func(self):
        # Execute command here.
        pass