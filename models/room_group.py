from constants.colors import Colors
from constants.objects import ObjectTypes
from constants.styles import Styles
from models.room import Room


class RoomGroup:
    room_group_name: str = None
    rooms: list[Room] = []

    def __init__(self, room_group_name: str, *rooms, **krooms) -> None:
        self.room_group_name = room_group_name
        self.rooms = list(rooms)
        for _, room in krooms.items():
            self.rooms.append(room)

    def __str__(self) -> str:
        return self.room_group_name

    def get_objects(
        self,
        object_type: ObjectTypes = None,
        color: Colors = None,
        style: Styles = None,
    ):
        objects = []
        for room in self.rooms:
            objects.extend(
                room.get_objects(object_type=object_type, color=color, style=style)
            )
        return objects

    def count_objects(
        self,
        object_type: ObjectTypes = None,
        color: Colors = None,
        style: Styles = None,
    ):
        return len(self.get_objects(object_type=object_type, color=color, style=style))

    def is_empty(self):
        return all([room.is_empty() for room in self.rooms])

    def count_empty(self):
        return len([room for room in self.rooms if room.is_empty()])
