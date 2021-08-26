import re
from robot import Robot

print("Issue commands for the robot, begin by placing it, type END to finish:")

robot = Robot()

while True:
    command = input().upper()

    # Check for the PLACE command.
    match = re.search(r"PLACE\W+(\d)\W+(\d)\W+([NSEW])", command)

    if match:
        robot.place(int(match.group(1)), int(match.group(2)), match.group(3))
    elif command == "END":
        break
    elif command == "MOVE":
        robot.move()
    elif command == "LEFT":
        robot.left()
    elif command == "RIGHT":
        robot.right()
    elif command == "REPORT":
        print(robot.report())
