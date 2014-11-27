"""
Constructor robots create ships.

They have a narrowly defined set of ships that they can create, which is intended to be edited in-game
by administrators.
"""

from ev import Object, create_object
from ev import Command, CmdSet

from game.gamesrc.objects.cochran.ships.generic_ships import BattleShip
from game.gamesrc.objects.cochran.ships.ship import Ship


class BotBeepCMD(Command):
    """
    Test command that makes the constructor bot make a noise.  Should only be accessible in the room
    where the ConstructorBot is currently residing.
    """
    key = "botbeep"

    def parse(self):
        pass

    def func(self):
        self.caller.location.msg_contents("ROBOT SAYS BEEP.")


class BuildShipCMD(Command):
    """
    build <ship_name> <ship_class>
    Build a ship of the specified class, expressed as a string.  The ship will then be dropped at the
    current location, a room-wide message id displayed, and the ships' outer exits are linked.
    """
    key = "construct"
    locks = "cmd:all()"
    help_category = "General"

    def parse(self):
        # build <ship_name> <ship_class>
        arguments = self.args.strip('')
        self.target_ship_name = arguments[0]
        self.target_ship_class = arguments[1]

    def func(self):

        # Sanity checking -- make sure that the ship class is one that this bot can make.
        self.caller.location.msg_contents("CONSTRUCTORBOT: SHIPCLASS--" + self.target_ship_class + "--SHIPNAME--" + self.target_ship_name + "--END")

        if self.obj.can_create_ship(self.target_ship_class):
            self.caller.location.msg_contents("The constructorbot whirs to life and starts assembling modular parts from"
                                          "the shelves into a functioninig ship.")
            myShip = create_object(typeclass=self.target_ship_class, key=self.target_ship_name)

            # Make the object appear at the current location.
            myShip.location = self.caller.location

            self.caller.location.msg_content("Emitting the 'job completed' tone, the constructorbot retreats back into its"
                                         "default position and powers down into standby mode.")

        else:
            self.caller.location.msg_contents("With a static hiss, the constructors vocal encoder comes to life.  'INVALID SHIP TYPE SPECIFIED.")

class ConstructorBotCMDSet(CmdSet):
    """
    Command set for loading onto ConstructorBots.  Call all commands defined above here.
    """
    def at_cmdset_creation(self):
        self.add(BotBeepCMD)
        self.add(BuildShipCMD)


class ConstructorBot(Object):
    """
    Base constructor robot class.  This is the regular entry point for making constructor bots, unless you want
    to subclass further.
    """
    def at_object_creation(self):
        # Define ships that can be constructed.
        self.db.unlocked_ships = ["BasicShip", "Freighter"]
        self.cmdset.add(ConstructorBotCMDSet)

    def create_ship(self, caller, name, ship_class):
        """
        Create a new ship and register it with the space system as an active vessel.
        @type caller: Object
        @type name: str
        @type ship_class: str
        """
        if self.can_create_ship(self, ship_class):
            the_ship = create_object(Ship, key=name)
            the_ship.location = self.location
            # ^ Does that actually put the ship in the right place?

        elif not self.can_create_ship(self, ship_class):
            return False        # Unable to produce requested ship class.

    def can_create_ship(self, ship_class):
        """
        If this shipyard can construct ships of the specified class, return true.
        Otherwise, return false.
        @type ship_class: str
        """
        if self.db.unlocked_ships.count(ship_class) > 0:
            return True
        elif self.db.unlocked_ships.count(ship_class) <= 0:
            return False