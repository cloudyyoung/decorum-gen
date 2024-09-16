from collections import defaultdict
from constants.colors import Colors
from constants.objects import ObjectTypes
from constants.styles import Styles
from models.object import Object
from models.room import Room


class RoomGroup:
    room_group_name: str = None
    rooms: list[Room] = []

    def __init__(self, room_group_name: str, *rooms, **krooms) -> None:
        self.room_group_name = room_group_name
        self.rooms = list(rooms)
        for _, room in krooms.items():
            self.rooms.append(room)

    def __str__(self) -> str:
        return self.room_group_name

    def get_objects(
        self,
        object_type: ObjectTypes = None,
        color: Colors = None,
        style: Styles = None,
    ):
        objects = []
        for room in self.rooms:
            objects.extend(
                room.get_objects(object_type=object_type, color=color, style=style)
            )
        return objects

    def count_objects(
        self,
        object_type: ObjectTypes = None,
        color: Colors = None,
        style: Styles = None,
    ):
        return len(self.get_objects(object_type=object_type, color=color, style=style))

    def count_common_objects(
        self,
        object_type: ObjectTypes = None,
        color: Colors = None,
        style: Styles = None,
    ):
        no_objects = 999
        for room in self.rooms:
            objs = room.count_objects(object_type=object_type, color=color, style=style)
            no_objects = min(no_objects, objs)
        return no_objects

    def is_empty(self):
        return all([room.is_empty() for room in self.rooms])

    def count_empty_rooms(self):
        return len([room for room in self.rooms if room.is_empty()])

    def count_slots(self):
        return sum([room.count_slots() for room in self.rooms])
    
    def count_empty_slots(self):
        return sum([room.count_empty_slots() for room in self.rooms])

    def count_object_slots(self):
        return sum([room.count_object_slots() for room in self.rooms])

    def get_object_counts(self, include_nonexistent=False):
        objects = defaultdict(int)

        if include_nonexistent:
            object_classes = Object.get_object_classes()
            for obj_class in object_classes:
                obj = obj_class()
                count = self.count_objects(
                    object_type=obj.object_type, color=obj.color, style=obj.style
                )
                objects[obj] = count
        else:
            for room in self.rooms:
                for obj in room.get_objects():
                    objects[obj] += 1

        return objects

    def is_identical_wall_colors(self):
        wall_colors = [room.wall_color for room in self.rooms]
        return len(set(wall_colors)) == 1
