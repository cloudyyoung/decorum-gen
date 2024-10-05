from decorum_generator.conditions.conditions_generator import ConditionsGenerator


class EmptyOrNotEmpty(ConditionsGenerator):
    def generate(self, house) -> None:
        # Individual rooms
        for room in house.rooms:
            if room.count_objects() > 0:
                self.add_condition(f"The {room} must not be empty.", 0)
            else:
                self.add_condition(f"The {room} must be empty.", 0)

        # Room groups
        for room_group in house.room_groups:
            if room_group.count_objects() > 0:
                self.add_condition(f"The {room_group} must not be empty.", 1)
            else:
                self.add_condition(f"The {room_group} must be empty.", 1)

        # Only empty rooms
        no_empty_rooms = house.count_empty_rooms()
        if no_empty_rooms == 1:
            empty_room = house.get_empty_rooms()[0]
            self.add_condition(f"The {empty_room} must be the only empty room.", 2)
