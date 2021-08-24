import pytest
from robot import Robot


@pytest.fixture
def robot():
    """DRY: create robot before each test case."""
    return Robot()


def test_constructor(robot):
    """Check that robot begins without any state because it hasn't been placed."""
    assert robot.state == None


def test_on_table_one(robot):
    """Check that method returns True when position is on the table."""
    assert robot.on_table(2, 2)


def test_on_table_two(robot):
    """Check that method returns False when position is off the table due to X."""
    assert not robot.on_table(6, 2)


def test_on_table_three(robot):
    """Check that method returns False when position is off the table due to Y."""
    assert not robot.on_table(2, 6)


def test_place_one(robot):
    """Check that we can place the robot on the table."""
    robot.place(0, 0, "N")
    assert robot.state == {"X": 0, "Y": 0, "F": "N"}


def test_place_two(robot):
    """Check that we cannot place the robot off the table."""
    robot.place(5, 7, "N")
    assert not robot.state


def test_place_three(robot):
    """Check that we can place the robot on the table twice."""
    robot.place(4, 4, "S")
    assert robot.state == {"X": 4, "Y": 4, "F": "S"}
    robot.place(2, 3, "W")
    assert robot.state == {"X": 2, "Y": 3, "F": "W"}


def test_place_four(robot):
    """Check that we can place the robot on the table after trying to place it off the table"""
    robot.place(7, 7, "E")
    assert not robot.state
    robot.place(5, 5, "S")
    assert robot.state == {"X": 5, "Y": 5, "F": "S"}
