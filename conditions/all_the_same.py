from conditions.condition import ConditionsGenerator


class AllTheSame(ConditionsGenerator):
    def generate(self, house) -> None:
        for room in house.rooms:
            no_room_objects = room.count_objects()
            no_room_wall_colors = 1 if room.wall_color else 0

            if room.is_identical_object_colors() and room.is_identical_object_styles():
                condition_str = (
                    f"Objects in the {room} must all have the same color and style."
                )
                self.add_condition(condition_str, 2 + no_room_objects)

            if room.is_identical_object_colors():
                condition_str = f"Objects in the {room} must all have the same color."
                self.add_condition(condition_str, 1 + no_room_objects)

            if room.is_identical_object_styles():
                condition_str = f"Objects in the {room} must all have the same style."
                self.add_condition(condition_str, 1 + no_room_objects)

            if room.is_identical_colors():
                condition_str = f"Everything in the {room} must all have the same color (objects and wall color)."
                self.add_condition(
                    condition_str,
                    1 + no_room_objects + no_room_wall_colors,
                )
