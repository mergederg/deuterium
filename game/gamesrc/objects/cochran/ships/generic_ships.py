"""
All the basic Cochran ship classes are contained within this file.  Create additional ships either here, or each in their own file.
"""
from ship import Ship


class BattleShip(Ship):
    "Specific battleship; no base class."
    def at_object_creation(self):
        super(Ship, self).at_object_creation()
        self.db.desc = "I'm a battleship!"


class Freighter(Ship):
    """
    A slow ship with minimal weapons and a large cargo capacity suitable for carrying freight.
    """
    def at_object_creation(self):
        super(Ship, self).at_object_creation()
        self.db.desc = "I'm a freighter!"


class DerpFreighter(Freighter):
    """
    Specific variant of the freighter NX class.
    """
    def at_object_creation(self):
        super(Freighter, self).at_object_creation()
        self.db.desc = "I'm a Derp-model freighter!"