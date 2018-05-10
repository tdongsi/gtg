
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

    def __str__(self):
        return self.__class__.__name__


class FaceNorth(RobotState):

    def go(self, robot):
        robot.y += 1

    def left(self, robot):
        robot.state = States.WEST

    def right(self, robot):
        robot.state = States.EAST


class FaceWest(RobotState):

    def go(self, robot):
        robot.x -= 1

    def left(self, robot):
        robot.state = States.SOUTH

    def right(self, robot):
        robot.state = States.NORTH


class FaceEast(RobotState):

    def go(self, robot):
        robot.x += 1

    def left(self, robot):
        robot.state = States.NORTH

    def right(self, robot):
        robot.state = States.SOUTH


class FaceSouth(RobotState):

    def go(self, robot):
        robot.y -= 1

    def left(self, robot):
        robot.state = States.EAST

    def right(self, robot):
        robot.state = States.WEST


class States:
    """Enum class to avoid creating too many state objects."""
    NORTH = FaceNorth()
    SOUTH = FaceSouth()
    WEST = FaceWest()
    EAST = FaceEast()


class Robot():

    def __init__(self):
        self.state = States.NORTH
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
    output = []
    for command in commands:
        robot = Robot()
        for c in command:
            robot.do(c)
        # print(robot)

        if robot.state == States.NORTH and not (robot.x == 0 and robot.y == 0):
            output.append('NO')
        else:
            output.append('YES')

    return output
