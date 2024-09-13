from abc import ABC
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


class Bathroom(Room): ...


class Bedroom(Room): ...


class LivingRoom(Room): ...


class Kitchen(Room): ...
