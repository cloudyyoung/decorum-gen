from models.floor import Downstairs, Upstairs
from models.room import Bedroom, Bathroom, LivingRoom, Kitchen
from models.side import LeftSide, RightSide


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

    def get_display(self) -> str:
        string = ""
        string += "House:\n"
        string += "  Bedroom:\n"
        string += self.bedroom.get_display()
        string += "  Bathroom:\n"
        string += self.bathroom.get_display()
        string += "  Living Room:\n"
        string += self.living_room.get_display()
        string += "  Kitchen:\n"
        string += self.kitchen.get_display()
        return string

    @staticmethod
    def get_random():
        house = House()
        house.bedroom = Bedroom.get_random()
        house.bathroom = Bathroom.get_random()
        house.living_room = LivingRoom.get_random()
        house.kitchen = Kitchen.get_random()
        return house

    @property
    def left_side(self):
        return LeftSide(self.bathroom, self.living_room)

    @property
    def right_side(self):
        return RightSide(self.kitchen, self.bedroom)

    @property
    def upstairs(self):
        return Upstairs(self.bedroom, self.bathroom)

    @property
    def downstairs(self):
        return Downstairs(self.living_room, self.kitchen)
