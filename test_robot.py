import pytest
from robot import Robot


@pytest.fixture
def robot():
    """DRY: create robot before each test case."""
    return Robot()


def test_constructor(robot):
    """Check that robot begins without any state because it hasn't been placed."""
    assert not robot.state


# Test on_table method.
def test_on_table_one(robot):
    """Check that method returns True when position is on the table."""
    assert robot.on_table(2, 2)


def test_on_table_two(robot):
    """Check that method returns False when position is off the table due to X."""
    assert not robot.on_table(6, 2)


def test_on_table_three(robot):
    """Check that method returns False when position is off the table due to Y."""
    assert not robot.on_table(2, 6)


# Test place method.
def test_place_one(robot):
    """Check that we can place the robot on the table."""
    robot.place(0, 0, "S")
    assert robot.state == {"X": 0, "Y": 0, "F": "S"}


def test_place_two(robot):
    """Check that we cannot place the robot off the table."""
    robot.place(7, 7, "E")
    assert not robot.state


def test_place_three(robot):
    """Check that we can place the robot on the table twice."""
    robot.place(4, 4, "S")
    assert robot.state == {"X": 4, "Y": 4, "F": "S"}
    robot.place(2, 3, "W")
    assert robot.state == {"X": 2, "Y": 3, "F": "W"}


def test_place_four(robot):
    """Check that we can place the robot on the table after trying to place it off the table"""
    robot.place(6, 8, "E")
    assert not robot.state
    robot.place(5, 5, "S")
    assert robot.state == {"X": 5, "Y": 5, "F": "S"}


def test_place_five(robot):
    """Check that we cannot place the robot off the table after placing it on the table."""
    robot.place(0, 4, "N")
    robot.place(2, 6, "S")
    assert robot.state == {"X": 0, "Y": 4, "F": "N"}


# Test left method.
def test_left_one(robot):
    """Check that robot can be turned left once."""
    robot.place(3, 3, "N")
    robot.left()
    assert robot.state["F"] == "W"


def test_left_two(robot):
    """Check that robot can be turned left twice."""
    robot.place(3, 3, "S")
    robot.left()
    robot.left()
    assert robot.state["F"] == "N"


def test_left_three(robot):
    """Check that robot cannot be turned left if it hasn't been placed."""
    robot.left()
    assert not robot.state


# Test right method.
def test_right_one(robot):
    """Check that robot can be turned right once."""
    robot.place(1, 5, "W")
    robot.right()
    assert robot.state["F"] == "N"


def test_right_two(robot):
    """Check that robot can be turned right three times."""
    robot.place(4, 2, "E")
    robot.right()
    robot.right()
    robot.right()
    assert robot.state["F"] == "N"


def test_right_three(robot):
    """Check that robot cannot be turned right if it hasn't been placed on the table."""
    robot.place(9, 9, "N")
    robot.right()
    assert not robot.state


def test_turning(robot):
    """Check that robot can be turned left once and then turned right twice."""
    robot.place(3, 3, "S")
    robot.left()
    robot.right()
    robot.right()
    assert robot.state["F"] == "W"


# Test move method.
def test_move_one(robot):
    """Check that robot can move one unit north."""
    robot.place(1, 1, "N")
    robot.move()
    assert robot.state == {"X": 1, "Y": 2, "F": "N"}


def test_move_two(robot):
    """Check that robot can move one unit south."""
    robot.place(3, 3, "S")
    robot.move()
    assert robot.state == {"X": 3, "Y": 2, "F": "S"}


def test_move_three(robot):
    """Check that robot can move one unit east."""
    robot.place(3, 3, "E")
    robot.move()
    assert robot.state == {"X": 4, "Y": 3, "F": "E"}


def test_move_four(robot):
    """Check that robot can move one unit west."""
    robot.place(1, 3, "W")
    robot.move()
    assert robot.state == {"X": 0, "Y": 3, "F": "W"}


def test_move_five(robot):
    """Check that robot cannot move off the table."""
    robot.place(1, 5, "N")
    robot.move()
    assert robot.state == {"X": 1, "Y": 5, "F": "N"}


# Test report method.
def test_report_one(robot):
    """Check that robot can return to original position after trying to move off the table."""
    robot.place(4, 1, "E")
    robot.move()
    robot.move()
    robot.left()
    robot.left()
    robot.move()
    assert robot.report() == "4, 1, WEST"


def test_report_two(robot):
    """Check that robot can move in a zigzag pattern."""
    robot.place(0, 0, "N")
    robot.move()  # 0, 1, N
    robot.right()  # 0, 1, E
    robot.move()  # 1, 1, E
    robot.left()  # 1, 1, N
    robot.move()  # 1, 2, N
    robot.right()  # 1, 2, E
    robot.move()  # 2, 2, E
    assert robot.report() == "2, 2, EAST"
