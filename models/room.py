from abc import ABC
from random import randint
from typing import Type
from models.color import *
from models.object import Curio, Lamp, WallHanging
from models.paint import Paint
from models.style import *


class Room(ABC):
    """
    House Room.
    """

    room_name: str = None
    paint: Paint = None
    lamp: Lamp = None
    curio: Curio = None
    wall_hanging: WallHanging = None

    def __init__(self, room_name):
        self.room_name = room_name

    def get_objects(
        self,
        object_type: Type[Lamp] | Type[Curio] | Type[WallHanging] = None,
        color: Type[Red] | Type[Green] | Type[Blue] | Type[Green] = None,
        style: Type[Modern] | Type[Antique] | Type[Retro] | Type[Unusual] = None,
    ):
        objects = [self.paint, self.lamp, self.curio, self.wall_hanging]
        objects = [object for object in objects if object]

        if object_type:
            objects = [object for object in objects if isinstance(object, object_type)]
        if color:
            objects = [object for object in objects if isinstance(object, color)]
        if style:
            objects = [object for object in objects if isinstance(object, style)]

        return objects

    def count_objects(
        self,
        object_type: Type[Lamp] | Type[Curio] | Type[WallHanging] = None,
        color: Type[Red] | Type[Green] | Type[Blue] | Type[Green] = None,
        style: Type[Modern] | Type[Antique] | Type[Retro] | Type[Unusual] = None,
    ):
        return len(self.get_objects(object_type=object_type, color=color, style=style))

    def get_display(self) -> str:
        string = ""
        string += "    Paint:        " + str(self.paint) + "\n"
        string += "    Lamp:         " + str(self.lamp) + "\n"
        string += "    Curio:        " + str(self.curio) + "\n"
        string += "    Wall Hanging: " + str(self.wall_hanging) + "\n"
        return string

    def __str__(self) -> str:
        return self.room_name

    def get_random(self):
        lamp_r = randint(0, 4)
        curio_r = randint(0, 4)
        wall_hanging_r = randint(0, 4)

        self.paint = Paint.get_random()
        if lamp_r <= 2:
            self.lamp = Lamp.get_random(object_type=Lamp)
        if curio_r <= 2:
            self.curio = Curio.get_random(object_type=Curio)
        if wall_hanging_r <= 2:
            self.wall_hanging = WallHanging.get_random(object_type=WallHanging)


class Bathroom(Room):
    def __init__(self):
        super().__init__("Bathroom")


class Bedroom(Room):
    def __init__(self):
        super().__init__("Bedroom")


class LivingRoom(Room):
    def __init__(self):
        super().__init__("Living Room")


class Kitchen(Room):
    def __init__(self):
        super().__init__("Kitchen")
