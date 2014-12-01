"""
Space is where all the ships go once they're built and sent off, and where ships that take off or undock from their mothership or space station end up.  Pretty much its where stuff happens.

'Space' as an application concept exist mostly in the ship indexes.  Everything is assigned x,y,z coordinates that are manipulated by the space controller scripts.
"""

from ev import Room


class Space(Room):

    def at_object_creation(self):
        #Initialize the space system.
        self.db.desc = "An initialized space room."