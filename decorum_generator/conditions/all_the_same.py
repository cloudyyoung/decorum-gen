from decorum_generator.conditions.condition import ConditionGroup
from decorum_generator.conditions.conditions_generator import ConditionsGenerator


class AllTheSame(ConditionsGenerator):
    def generate(self) -> None:
        for room in self.house.rooms:
            no_room_objects = room.count_objects()
            no_room_wall_colors = 1 if room.wall_color else 0

            # Object colors and styles
            group = ConditionGroup()

            if room.is_identical_object_colors() and room.is_identical_object_styles():
                condition_str = (
                    f"Objects in the {room} must all have the same color and style."
                )
                group.add(condition_str, 2 + no_room_objects)

            if room.is_identical_object_colors():
                condition_str = f"Objects in the {room} must all have the same color."
                group.add(condition_str, 1 + no_room_objects)

            if room.is_identical_object_styles():
                condition_str = f"Objects in the {room} must all have the same style."
                group.add(condition_str, 1 + no_room_objects)

            if room.is_identical_colors():
                condition_str = f"Everything in the {room} must all have the same color (objects and wall color)."
                group.add(condition_str, 1 + no_room_objects + no_room_wall_colors)

            self.add_condition_group(group)
