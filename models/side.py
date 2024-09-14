from abc import ABC

from models.room import *


class Side(ABC):
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


class LeftSide(Side):
    bathroom: Bathroom = None
    living_room: LivingRoom = None

    def __init__(self, bathroom: Bathroom, living_room: LivingRoom):
        self.bathroom = bathroom
        self.living_room = living_room

    @property
    def rooms(self):
        return [self.bathroom, self.living_room]


class RightSide(Side):
    kitchen: Kitchen = None
    bedroom: Bedroom = None

    def __init__(self, kitchen: Kitchen, bedroom: Bedroom):
        self.kitchen = kitchen
        self.bedroom = bedroom

    @property
    def rooms(self):
        return [self.kitchen, self.bedroom]
