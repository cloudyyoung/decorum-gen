from models.room import *


class RoomGroup:
    rooms: list[Room] = []

    def __init__(self, *rooms, **krooms) -> None:
        self.rooms = list(rooms)
        for _, room in krooms.items():
            self.rooms.append(room)

    def get_objects(
        self,
        object_type: Type[Lamp] | Type[Curio] | Type[WallHanging] = None,
        color: Type[Red] | Type[Green] | Type[Blue] | Type[Green] = None,
        style: Type[Modern] | Type[Antique] | Type[Retro] | Type[Unusual] = None,
    ):
        objects = []
        for room in self.rooms:
            objects.extend(
                room.get_objects(object_type=object_type, color=color, style=style)
            )
        return objects

    def count_objects(
        self,
        object_type: Type[Lamp] | Type[Curio] | Type[WallHanging] = None,
        color: Type[Red] | Type[Green] | Type[Blue] | Type[Green] = None,
        style: Type[Modern] | Type[Antique] | Type[Retro] | Type[Unusual] = None,
    ):
        return len(self.get_objects(object_type=object_type, color=color, style=style))
