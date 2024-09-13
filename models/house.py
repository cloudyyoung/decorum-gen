from models.room import Bedroom, Bathroom, LivingRoom, Kitchen


class House:
    """
    House board.
    """

    bedroom: Bedroom = None
    bathroom: Bathroom = None
    living_room: LivingRoom = None
    kitchen: Kitchen = None

    def __init__(self):
        self.bedroom = Bedroom()
        self.bathroom = Bathroom()
        self.living_room = LivingRoom()
        self.kitchen = Kitchen()
