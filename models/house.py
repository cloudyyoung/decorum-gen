from models.room import Bedroom, Bathroom, LivingRoom, Kitchen
from models.room_group import RoomGroup


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
        return RoomGroup(self.bathroom, self.living_room)

    @property
    def right_side(self):
        return RoomGroup(self.bedroom, self.kitchen)

    @property
    def upstairs(self):
        return RoomGroup(self.bathroom, self.bedroom)

    @property
    def downstairs(self):
        return RoomGroup(self.living_room, self.kitchen)

    @property
    def top_left_and_bottom_right(self):
        return RoomGroup(self.bathroom, self.kitchen)

    @property
    def top_right_and_bottom_left(self):
        return RoomGroup(self.bedrrom, self.living_room)
