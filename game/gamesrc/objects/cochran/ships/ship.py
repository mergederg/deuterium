"""

Root class for ships.  Everything inheriting from this (and you should inherit from this rather than @create them
directly) will have the properties and behaviors outlined below.

Basic Rooms:
When each ship is constructed, its at_object_creation makes certain Rooms (ev.Room) -- a Cargo Bay (which is where
cargo gets loaded to, people board, etc -- conceptually the first room in from 'outside'), and a cockpit (where all
the magic of ship controls happens.

Ships contain a special exit, airlock, that is connected to the outside world.  One end gets dynamically reconnected
whenever the ship lands somewhere.

"""

import uuid
from ev import Object, create_object, Room, Exit


class Ship(Object):
    """
    Base ship class.  These should generally not be constructed on their own, but inherited from within subclasses in
    your own implementation of Cochran (see above).
    """
    def at_object_creation(self):
        self.db.desc = "An unadorned vessel.  You shouldn't see this unless something has gone horribly wrong."
        self.db.transponder_id = uuid.uuid1()
        self.db.entry_password = '1235'

        # Create the bridge and cargo bay.
        self.bridge = create_object(Room, key="Bridge")
        self.cargo_bay = create_object(Room, key="Cargo Bay")

        # Link with exits.
        self.bridge_entrance = create_object(Exit, key="Out")
        self.bridge_exit = create_object(Exit, key="Bridge")

        # Bridge -> Cargo Bay
        self.db.bridge_exit_ref = self.bridge_exit.dbref
        self.bridge_exit.location = self.bridge
        self.bridge_exit.destination = self.cargo_bay

        # Cargo Bay -> Bridge
        self.db.bridge_entrance_ref = self.bridge_entrance.dbref
        self.bridge_entrance.location = self.cargo_bay
        self.bridge_entrance.destination = self.bridge

        # And do the same with an airlock, on the inside of the cargo bay and the outside of the ship.
        self.airlock_out = create_object(Exit, key="Airlock Out")
        self.airlock_in = create_object(Exit, key="Airlock In")

        self.db.airlock_in_ref = self.airlock_in.dbref
        self.db.airlock_out_ref = self.airlock_out.dbref
        self.db.cargo_ref = self.cargo_bay.dbref
        self.db.bridge_ref = self.bridge.dbref

        #Link airlock exits to wherever the ship is being built.
        self.airlock_out.location = self.cargo_bay
        self.airlock_out.destination = self.location
        self.airlock_in.location = self.location
        self.airlock_in.destination = self.cargo_bay

    # TODO: State changing methods, for use by scripts and such.