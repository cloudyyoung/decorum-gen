from decorum_generator.conditions.condition import ConditionsGenerator
from decorum_generator.conditions.utils import format_object_text
from decorum_generator.models.room import Room
from decorum_generator.models.room_group import RoomGroup


class RoomWallColorMatchesObjectColors(ConditionsGenerator):
    def generate(self, house) -> None:
        # Rooms
        for room in house.rooms:
            self.generate_room(room)

        # RoomGroups
        for room_group in house.room_groups:
            self.generate_room(room_group)

    def generate_room(self, room: Room | RoomGroup) -> None:
        # If is a RoomGroup and the wall colors for rooms are already not identical, skip
        if isinstance(room, RoomGroup) and not room.is_identical_wall_colors():
            return

        # All wall colors are identical now in the room group, so pick the first room wall color
        if isinstance(room, RoomGroup):
            wall_color = room.rooms[0].wall_color
            suffix = "s"
        else:
            wall_color = room.wall_color
            suffix = ""

        # Get objects matching the wall color
        matching_objects = room.get_objects(color=wall_color)
        no_matching_objects = len(matching_objects)
        no_room_objects = room.count_objects()

        if no_matching_objects == no_room_objects:
            condition_str = f"The wall color{suffix} of the {room} must match the color of all the objects in the room{suffix}."
            self.add_condition(condition_str, 4)
        elif no_matching_objects >= 1:
            condition_str = f"The wall color{suffix} of the {room} must match the color of one of the objects in the room{suffix}."
            self.add_condition(condition_str, 3)

        if no_matching_objects >= 1:
            for obj in matching_objects:
                subject_str = format_object_text(2, object_type=obj.object_type)
                condition_str_a = f"The wall color{suffix} of the {room} must match the color of the {subject_str} in the room{suffix}."

                subject_str = format_object_text(2, style=obj.style)
                condition_str_b = f"The wall color{suffix} of the {room} must match the color of one of the {subject_str} in the room{suffix}."

                self.add_conditions((condition_str_a, 3), (condition_str_b, 4))
