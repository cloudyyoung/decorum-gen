from abc import ABC

from constants.styles import Styles


class Style(ABC): ...


class Modern(Style, ABC):
    style = Styles.MODERN


class Antique(Style, ABC):
    style = Styles.ANTIQUE


class Retro(Style, ABC):
    style = Styles.RETRO


class Unusual(Style, ABC):
    style = Styles.UNUSUAL
