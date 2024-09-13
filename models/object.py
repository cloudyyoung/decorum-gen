from abc import ABC
import random
from typing import Self, Type

from models.color import Red, Yellow, Blue, Green
from models.style import Modern, Antique, Retro, Unusual
from models.feature import Feature


class Object(Feature, ABC):
    @staticmethod
    def get_random(
        object_type: Type["Lamp"] | Type["Curio"] | Type["WallHanging"] = None,
        color: Type[Red] | Type[Green] | Type[Blue] | Type[Green] = None,
        style: Type[Modern] | Type[Antique] | Type[Retro] | Type[Unusual] = None,
    ) -> Self:
        # Get all subclasses of Object recursively
        subclasses = []
        for subclass in Object.__subclasses__():
            subclasses.extend(subclass.__subclasses__())

        if object_type:
            subclasses = [cls for cls in subclasses if issubclass(cls, object_type)]

        if color:
            subclasses = [cls for cls in subclasses if issubclass(cls, color)]

        if style:
            subclasses = [cls for cls in subclasses if issubclass(cls, style)]

        if len(subclasses) == 0:
            raise Exception("No matching object found")

        subclass = random.choice(subclasses)
        return subclass()


class Lamp(Object, ABC): ...


class Curio(Object, ABC): ...


class WallHanging(Object, ABC): ...


### Modern


class RedModernWallHanging(WallHanging, Red, Modern): ...


class GreenModernCurio(Curio, Green, Modern): ...


class BlueModernLamp(Lamp, Blue, Modern): ...


### Antique


class GreenAntiqueWallHanging(WallHanging, Green, Antique): ...


class BlueAntiqueCurio(Curio, Blue, Antique): ...


class YellowAntiqueLamp(Lamp, Yellow, Antique): ...


### Retro


class BlueRetroWallHanging(WallHanging, Blue, Retro): ...


class YellowRetroCurio(Curio, Yellow, Retro): ...


class RedRetroLamp(Lamp, Red, Retro): ...


### Unusual


class YellowUnsualWallHanging(WallHanging, Yellow, Unusual): ...


class RedUnusualCurio(Curio, Red, Unusual): ...


class GreenUnusualLamp(Lamp, Green, Unusual): ...
