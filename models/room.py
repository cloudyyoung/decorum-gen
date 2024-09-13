from abc import ABC
from random import randint
from models.object import Curio, Lamp, WallHanging
from models.paint import Paint


class Room(ABC):
    """
    House Room.
    """

    paint: Paint = None
    lamp: Lamp = None
    curio: Curio = None
    wall_hanging: WallHanging = None

    def get_display(self) -> str:
        string = ""
        string += "    Paint: " + str(self.paint) + "\n"
        string += "    Lamp: " + str(self.lamp) + "\n"
        string += "    Curio: " + str(self.curio) + "\n"
        string += "    Wall Hanging: " + str(self.wall_hanging) + "\n"
        return string

    @staticmethod
    def get_random():
        room = Room()

        lamp_r = randint(0, 3)
        curio_r = randint(0, 3)
        wall_hanging_r = randint(0, 3)

        room.paint = Paint.get_random()

        if lamp_r <= 2:
            room.lamp = Lamp.get_random()

        if curio_r <= 2:
            room.curio = Curio.get_random()

        if wall_hanging_r <= 2:
            room.wall_hanging = WallHanging.get_random()

        return room


class Bathroom(Room): ...


class Bedroom(Room): ...


class LivingRoom(Room): ...


class Kitchen(Room): ...
