from abc import ABC
from random import randint
from typing import Self
from constants.objects import ObjectTypes
from constants.styles import Styles
from constants.colors import Colors
from models.object import Curio, Lamp, WallHanging
from models.wall_color import WallColor


class Room(ABC):
    """
    House Room.
    """

    room_name: str = None
    wall_color: WallColor = None
    lamp: Lamp = None
    curio: Curio = None
    wall_hanging: WallHanging = None

    def __init__(self, room_name):
        self.room_name = room_name

    def get_objects(
        self,
        object_type: ObjectTypes = None,
        color: Colors = None,
        style: Styles = None,
    ):
        objects = [self.lamp, self.curio, self.wall_hanging]
        objects = [object for object in objects if object]

        if object_type:
            objects = [
                object for object in objects if object.object_type == object_type
            ]
        if color:
            objects = [object for object in objects if object.color == color]
        if style:
            objects = [object for object in objects if object.style == style]

        return objects

    def count_objects(
        self,
        object_type: ObjectTypes = None,
        color: Colors = None,
        style: Styles = None,
    ):
        return len(self.get_objects(object_type=object_type, color=color, style=style))

    def count_wall_color(self):
        return 1 if self.wall_color else 0

    def count_empty_slots(self):
        return 4 - self.count_objects() - self.count_wall_color()

    def count_occupied_slots(self):
        return self.count_objects() + self.count_wall_color()

    def is_empty(self):
        return self.count_empty_slots() == 4

    def is_full(self):
        return self.count_occupied_slots() == 4

    def get_display(self) -> str:
        string = ""
        string += "    WallColor:    " + str(self.wall_color) + "\n"
        string += "    Lamp:         " + str(self.lamp) + "\n"
        string += "    Curio:        " + str(self.curio) + "\n"
        string += "    Wall Hanging: " + str(self.wall_hanging) + "\n"
        return string

    def is_identical_features(self, other: Self) -> bool:
        if not other:
            return False
        return (
            self.wall_color == other.wall_color
            and self.lamp == other.lamp
            and self.curio == other.curio
            and self.wall_hanging == other.wall_hanging
        )

    def __str__(self) -> str:
        return self.room_name

    def get_random(self):
        lamp_r = randint(0, 3)
        curio_r = randint(0, 3)
        wall_hanging_r = randint(0, 3)

        self.wall_color = WallColor.get_random()
        if lamp_r <= 2:
            self.lamp = Lamp.get_random(object_type=ObjectTypes.LAMP)
        if curio_r <= 2:
            self.curio = Curio.get_random(object_type=ObjectTypes.CURIO)
        if wall_hanging_r <= 2:
            self.wall_hanging = WallHanging.get_random(
                object_type=ObjectTypes.WALL_HANGING
            )


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
