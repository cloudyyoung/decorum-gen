from random import sample
from decorum_generator.conditions.condition import ConditionGroup
from decorum_generator.conditions.conditions_generator import ConditionsGenerator


class EmptyOrNotEmpty(ConditionsGenerator):
    def generate(self) -> None:
        # Individual rooms
        room_group = self.create_condition_group()
        for room in self.house.rooms:
            if room.count_objects() > 0:
                room_group.add(f"The {room} must not be empty.", 0)
            else:
                room_group.add(f"The {room} must be empty.", 0)

        # Room groups
        room_group_group = self.create_condition_group()
        for room_group in self.house.room_groups:
            if room_group.count_objects() > 0:
                room_group_group.add(f"The {room_group} must not be empty.", 1)
            else:
                room_group_group.add(f"The {room_group} must be empty.", 1)

        # Only empty rooms
        no_empty_rooms = self.house.count_empty_rooms()
        if no_empty_rooms == 1:
            empty_room = self.house.get_empty_rooms()[0]
            self.add_condition(f"The {empty_room} must be the only empty room.", 2)

    def pick(self):
        conditions = self.get_flattened_contions()
        return sample(conditions, 5)
