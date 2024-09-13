from abc import ABC, abstractmethod


class Feature(ABC):
    """
    Object or paint color.
    """

    @staticmethod
    @abstractmethod
    def get_random(): ...
