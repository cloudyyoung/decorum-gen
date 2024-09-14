from abc import ABC

from models.room import *


class Floor(ABC):
    @property
    def rooms(self):
        return []

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


class Upstairs(Floor):
    bedroom: Bedroom = None
    bathroom: Bathroom = None

    def __init__(self, bedroom: Bedroom, bathroom: Bathroom):
        self.bedroom = bedroom
        self.bathroom = bathroom

    @property
    def rooms(self):
        return [self.bedroom, self.bathroom]


class Downstairs(Floor):
    living_room: LivingRoom = None
    kitchen: Kitchen = None

    def __init__(self, living_room: LivingRoom, kitchen: Kitchen):
        self.living_room = living_room
        self.kitchen = kitchen

    @property
    def rooms(self):
        return [self.living_room, self.kitchen]
