from decorum_generator.conditions.condition import (
    SingleConditionGroup,
    FullConditionGroup,
)


def test_full_contains_single():
    scg = SingleConditionGroup()
    scg.add("scg1", 2)
    scg.add("scg2", 2)
    scg.add("scg3", 2)
    scg.add("scg4", 2)
    scg.add("scg5", 2)

    fcg = FullConditionGroup()
    fcg.add("fcg1", 2)
    fcg.add("fcg2", 2)
    fcg.add_group(scg)

    picked_conditions = fcg.pick()
    assert len(picked_conditions) == 3
    assert picked_conditions[0].condition == "fcg1"
    assert picked_conditions[1].condition == "fcg2"
    assert picked_conditions[2].condition.startswith("scg")


def test_full_contains_single_contains_full():
    scg = SingleConditionGroup()
    fcg1 = FullConditionGroup()
    fcg2 = FullConditionGroup()
    fcg3 = FullConditionGroup()

    scg.add_group(fcg1)
    scg.add_group(fcg2)
    scg.add_group(fcg3)

    fcg1.add("fcg11", 2)
    fcg1.add("fcg12", 2)
    fcg2.add("fcg21", 2)
    fcg2.add("fcg22", 2)
    fcg3.add("fcg31", 2)
    fcg3.add("fcg32", 2)

    fcg = FullConditionGroup()
    fcg.add_group(scg)

    picked_conditions = fcg.pick()

    assert len(picked_conditions) == 2
    assert picked_conditions[0].condition.startswith("fcg")


def test_single_pick_repeat():
    scg = SingleConditionGroup()
    scg.add("scg1", 2)
    scg.add("scg2", 2)

    picked_conditions = scg.pick()
    assert len(picked_conditions) == 1
    scg.mark_as_picked(picked_conditions[0])
    assert scg.is_exhausted() == False

    picked_conditions = scg.pick()
    assert len(picked_conditions) == 1
    scg.mark_as_picked(picked_conditions[0])
    assert scg.is_exhausted() == True

    picked_conditions = scg.pick()
    assert len(picked_conditions) == 0
    assert scg.is_exhausted() == True


def test_full_pick_repeat():
    fcg1 = FullConditionGroup()
    fcg1.add("fcg1", 2)
    fcg1.add("fcg2", 2)

    picked_conditions = fcg1.pick()
    assert len(picked_conditions) == 2
    assert fcg1.is_exhausted() == False

    picked_conditions = fcg1.pick()
    assert len(picked_conditions) == 2
    assert fcg1.is_exhausted() == False

    fcg1.mark_as_picked(picked_conditions[0])
    assert fcg1.is_exhausted() == False

    picked_conditions = fcg1.pick()
    assert len(picked_conditions) == 1
    assert fcg1.is_exhausted() == False

    fcg1.mark_as_picked(picked_conditions[0])
    assert fcg1.is_exhausted() == True

    picked_conditions = fcg1.pick()
    assert len(picked_conditions) == 0
    assert fcg1.is_exhausted() == True

    fcg2 = FullConditionGroup(1)
    fcg2.add("fcg3", 2)
    fcg2.add("fcg4", 2)

    picked_conditions = fcg2.pick()
    assert len(picked_conditions) == 1

    fcg2.mark_as_picked(picked_conditions[0])
    assert fcg2.is_exhausted() == False

    picked_conditions = fcg2.pick()
    assert len(picked_conditions) == 1

    fcg2.mark_as_picked(picked_conditions[0])
    assert fcg2.is_exhausted() == True

    picked_conditions = fcg2.pick()
    assert len(picked_conditions) == 0
    assert fcg2.is_exhausted() == True
