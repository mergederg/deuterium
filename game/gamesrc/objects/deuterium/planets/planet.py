"""
These are a little more than containers for rooms.  They gave those bunches of rooms a coordinate to be in space.

While they generally shouldn't be moved, we'll expose a function to allow administrators to change their location.
"""
from ev import Object, Room, create_object


class Planet(Object):

    def at_object_creation(self):
        self.spaceport = create_object(Room, key="Spaceport")
        pass

    def create_room(self, room_name):
        "Create a room with the planet's name as one of its tags."
        tempRoom = create_object(Room, key="room_name")
        tempRoom.tags.add(self.key)
        pass

    def set_coordinates(self, newX, newY, newZ):
        "'Move' the planet to different space coordinates by assigning a different set of X/Y/Z coordinates."
        self.locationX = newX
        self.locationY = newY
        self.locationZ = newZ