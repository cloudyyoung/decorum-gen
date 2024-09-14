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
    room_groups: list[RoomGroup] = None

    upstairs: RoomGroup = None
    downstairs: RoomGroup = None
    left_side: RoomGroup = None
    right_side: RoomGroup = None
    top_left_and_bottom_right: RoomGroup = None
    top_right_and_bottom_left: Room

    def __init__(self):
        self.bedroom = Bedroom()
        self.bathroom = Bathroom()
        self.living_room = LivingRoom()
        self.kitchen = Kitchen()

        self.rooms = [self.bedroom, self.bathroom, self.living_room, self.kitchen]
        self.upstairs = RoomGroup(self.bathroom, self.bedroom)
        self.downstairs = RoomGroup(self.living_room, self.kitchen)
        self.left_side = RoomGroup(self.bathroom, self.living_room)
        self.right_side = RoomGroup(self.bedroom, self.kitchen)
        self.top_left_and_bottom_right = RoomGroup(self.bathroom, self.kitchen)
        self.top_right_and_bottom_left = RoomGroup(self.bedroom, self.living_room)

        self.room_groups = [
            self.upstairs,
            self.downstairs,
            self.left_side,
            self.right_side,
            self.top_left_and_bottom_right,
            self.top_right_and_bottom_left,
        ]

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
