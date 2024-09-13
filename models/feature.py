from abc import ABC, abstractmethod


class Feature(ABC):
    """
    Object or paint color.
    """

    def __repr__(self) -> str:
        return self.__class__.__name__

    @staticmethod
    @abstractmethod
    def get_random(): ...
