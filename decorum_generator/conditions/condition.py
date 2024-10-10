from abc import ABC, abstractmethod
from random import choice, sample
from typing import Any, Self


class Condition:
    def __init__(self, condition: str, difficulty_points: int):
        """
        Initialize the condition with a condition string and a difficulty points value.

        :param condition: The condition string.
        :type condition: str
        :param difficulty_points: The difficulty points value.
        :type difficulty_points: int
        """
        self.condition = condition
        self.difficulty_points = difficulty_points

    def __str__(self):
        return self.condition

    def __repr__(self):
        return f"({self.condition}, {self.difficulty_points} pts)"

    def __hash__(self):
        return hash(self.condition)

    def __eq__(self, other: object):
        if not other or not isinstance(other, Condition):
            return False
        return self.condition == other.condition


class ConditionGroup(list[Condition | Self], ABC):
    """
    This class is a list of conditions and/or condition group.
    """

    __picked: set[Condition]

    def __init__(self, *args):
        """
        Initialize the condition group with a logic operator.
        """
        super().__init__(args)
        self.__picked = set()

    @property
    def groups(self):
        return [group for group in self if isinstance(group, ConditionGroup)]

    @property
    def conditions(self):
        return [condition for condition in self if isinstance(condition, Condition)]

    def append(self, object: Condition | Self | Any) -> None:
        """
        Append a condition or condition group to the list.

        :param object: The condition or condition group to append.
        :type object: `Condition` or `ConditionGroup`
        """
        if object is None:
            return
        return super().append(object)

    def add(self, condition_str: str, difficulty_points: int) -> Condition:
        """
        Add a single condition to the conditions list.

        :param condition_str: The condition string.
        :type condition_str: str
        :param difficulty_points: The difficulty points value.
        :type difficulty_points: int

        :return: The added condition.
        :rtype: `Condition`
        """
        condition = Condition(condition_str, difficulty_points)
        self.append(condition)
        return condition

    def add_group(self, condition_group: Self) -> Self:
        """
        Add a condition group to the conditions list.

        :param condition_group: The condition group to add.
        :type condition_group: `ConditionGroup`

        :return: The added condition group.
        :rtype: `ConditionGroup`
        """
        self.append(condition_group)
        return condition_group

    @abstractmethod
    def pick(self) -> list[Condition]: ...

    def is_exhausted(self) -> bool:
        """
        Check if all conditions in the group have been picked.

        :return: True if all conditions have been picked, False otherwise.
        :rtype: bool
        """
        conditions_exhausted = all(
            condition in self.__picked
            for condition in self
            if isinstance(condition, Condition)
        )
        condition_groups_exhausted = all(
            condition_group.is_exhausted()
            for condition_group in self
            if isinstance(condition_group, ConditionGroup)
        )
        return conditions_exhausted and condition_groups_exhausted

    def get_pickable_members(self) -> list[Condition]:
        """
        Get all pickable members from the condition group. These members can be conditions or other condition groups.
        If a member is a condition group, it recursively gets pickable members from the group.

        :return: A list of conditions.
        """
        pickable_members = []
        for member in self:
            if isinstance(member, ConditionGroup) and not member.is_exhausted():
                pickable_members.append(member)
            elif isinstance(member, Condition) and member not in self.__picked:
                pickable_members.append(member)
        return pickable_members

    def mark_as_picked(self, condition: Condition) -> None:
        """
        Mark a condition as picked.

        :param condition: The condition to mark as picked.
        :type condition: `Condition`
        """

        if condition in self:
            self.__picked.add(condition)
        else:
            for member in self.groups:
                member.mark_as_picked(condition)


class SingleConditionGroup(ConditionGroup):
    def pick(self) -> list[Condition]:
        """
        Pick a single member from the condition group. This member can be a condition or another condition group.
        If it is a condition group, it recursively picks conditions from the group.

        :return: A list of conditions containing a **single** condition. If there are no pickable members, return an empty list.
        :rtype: list[Condition]
        """
        pickable_members = self.get_pickable_members()
        if len(pickable_members) == 0:
            return []

        picked_member = choice(pickable_members)
        if isinstance(picked_member, ConditionGroup):
            return picked_member.pick()

        return [picked_member]


class FullConditionGroup(ConditionGroup):
    max_num_of_conditions: int

    def __init__(self, max_num_of_conditions=None, *args):
        """
        Initialize the condition group with a logic operator and a maximum number of conditions to pick.

        :param max_num_of_conditions: The maximum number of conditions to pick. If None, pick all conditions.
        :type max_num_of_conditions: int
        """
        super().__init__(*args)
        self.max_num_of_conditions = max_num_of_conditions

    def pick(self) -> list[Condition]:
        """
        Pick all members from the condition group. These members can be conditions or other condition groups.
        If a member is a condition group, it recursively picks conditions from the group.

        :return: A list of conditions.
        """
        conditions = []

        pickable_members = self.get_pickable_members()
        if len(pickable_members) == 0:
            return []

        if self.max_num_of_conditions is not None:
            pickable_members = sample(
                pickable_members,
                min(self.max_num_of_conditions, len(pickable_members)),
            )

        for member in pickable_members:
            if isinstance(member, ConditionGroup):
                conditions.extend(member.pick())
            else:
                conditions.append(member)

        return conditions
