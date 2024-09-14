from abc import ABC
import random
from typing import Self, Type

from constants.colors import Colors
from constants.objects import ObjectTypes
from constants.styles import Styles
from models.color import Red, Yellow, Blue, Green
from models.style import Modern, Antique, Retro, Unusual
from models.feature import Feature


class Object(Feature, ABC):
    object_type: ObjectTypes
    color: Colors
    style: Styles

    def __str__(self) -> str:
        return f"{self.color} {self.style} {self.object_type}"

    def __eq__(self, other: Self) -> bool:
        return (
            self.object_type == other.object_type
            and self.color == other.color
            and self.style == other.style
        )

    def __hash__(self) -> int:
        return hash((self.object_type, self.color, self.style))

    @staticmethod
    def get_object_classes() -> list[Type[Self]]:
        subclasses = []
        for subclass in Object.__subclasses__():
            subclasses.extend(subclass.__subclasses__())
        return subclasses

    @staticmethod
    def get_random(
        object_type: ObjectTypes = None,
        color: Colors = None,
        style: Styles = None,
    ) -> Self:
        subclasses = Object.get_object_classes()

        if object_type:
            subclasses = [cls for cls in subclasses if cls.object_type == object_type]

        if color:
            subclasses = [cls for cls in subclasses if cls.color == color]

        if style:
            subclasses = [cls for cls in subclasses if cls.style == style]

        if len(subclasses) == 0:
            return None

        subclass = random.choice(subclasses)
        return subclass()


class Lamp(Object, ABC):
    object_type = ObjectTypes.LAMP


class Curio(Object, ABC):
    object_type = ObjectTypes.CURIO


class WallHanging(Object, ABC):
    object_type = ObjectTypes.WALL_HANGING


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
