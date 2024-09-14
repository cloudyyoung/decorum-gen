from models.room import Bedroom, Bathroom, LivingRoom, Kitchen, Room
from models.room_group import RoomGroup


class House(RoomGroup):
    """
    House board.
    """

    bedroom: Bedroom = None
    bathroom: Bathroom = None
    living_room: LivingRoom = None
    kitchen: Kitchen = None

    rooms: list[Room] = None

    def __init__(self):
        self.bedroom = Bedroom()
        self.bathroom = Bathroom()
        self.living_room = LivingRoom()
        self.kitchen = Kitchen()
        self.rooms = [self.bedroom, self.bathroom, self.living_room, self.kitchen]

    def get_display(self) -> str:
        string = ""
        for room in self.rooms:
            string += str(room) + "\n"
            string += room.get_display() + "\n"
        return string

    def get_random(self):
        self.bedroom.get_random()
        self.bathroom.get_random()
        self.living_room.get_random()
        self.kitchen.get_random()

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
