
from abc import abstractmethod, ABCMeta


class RobotState(metaclass=ABCMeta):
    """Robot state interface."""

    @abstractmethod
    def go(self, robot):
        pass

    @abstractmethod
    def left(self, robot):
        pass

    @abstractmethod
    def right(self, robot):
        pass


class FaceNorth(RobotState):

    def go(self, robot):
        robot.y += 1

    def left(self, robot):
        robot.state = FaceWest()

    def right(self, robot):
        robot.state = FaceEast()


class FaceWest(RobotState):

    def go(self, robot):
        robot.x -= 1

    def left(self, robot):
        robot.state = FaceSouth()

    def right(self, robot):
        robot.state = FaceNorth()


class FaceEast(RobotState):

    def go(self, robot):
        robot.x += 1

    def left(self, robot):
        robot.state = FaceNorth()

    def right(self, robot):
        robot.state = FaceSouth()


class FaceSouth(RobotState):

    def go(self, robot):
        robot.y -= 1

    def left(self, robot):
        robot.state = FaceEast()

    def right(self, robot):
        robot.state = FaceWest()


class States:
    """Enum class to avoid creating too many state objects."""
    NORTH = FaceNorth()
    SOUTH = FaceSouth()
    WEST = FaceWest()
    EAST = FaceEast()


class Robot():

    def __init__(self):
        self.state = FaceNorth()
        self.x, self.y = 0, 0

    def do(self, command):
        if command == 'G':
            self.state.go(self)
        elif command == 'L':
            self.state.left(self)
        elif command == 'R':
            self.state.right(self)

    def __str__(self):
        return "Pos: {} {}. Ori: {}".format(self.x, self.y, self.state)


def doesCircleExist(commands):
    for command in commands:
        robot = Robot()
        for c in command:
            robot.do(c)
        print(robot)
