from abc import ABC, abstractmethod
import re


class Feature(ABC):
    """
    Object or paint color.
    """

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return re.sub(r"(\w)([A-Z])", r"\1 \2", cls_name)

    @staticmethod
    @abstractmethod
    def get_random(): ...
