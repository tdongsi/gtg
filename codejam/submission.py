
from abc import ABCMeta, abstractmethod
import sys
import itertools
import math
import decimal


class BaseSolver(metaclass=ABCMeta):

    def __init__(self, filename=None):
        """ Initialize with the given input file.

        :param filename: input file path
        :return:
        """
        self._filename = filename
        pass

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.
        Follow Google Code Jam format.

        :param output: specify output to file or screen.
        :return:
        """
        inf = open(self._filename) if self._filename else sys.stdin
        try:
            with inf as f:
                lines = f.readlines()

                for case_num, line in enumerate(lines[1:], start=1):
                    result = self._solve(line.strip())
                    output.write("Case #%d: %s\n" % (case_num, result))

        except IOError:
            print("Error opening file")
        pass

    @abstractmethod
    def _solve(self, input_str: str) -> str:
        raise NotImplementedError('Abstract method')


class Solver(BaseSolver):
    """ Google Code Jam 2018.
    https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cc
    """

    def _solve(self, inputstr):
        area = float(inputstr)
        centers = self._compute(area)
        template = "\n{0} {1} {2}\n{3} {4} {5}\n{6} {7} {8}"

        return template.format(*itertools.chain.from_iterable(centers))

    def _compute(self, area: float):
        """ Purely mathematical solution for Test set: 1.000000 <= A <= 1.414213.
        For A <= 1.414213, it is satisfactory to just rotate around z axis.
        One side of the projection will be always 1. The area is dependent on the other side length of projection

        At the angle x = 0, the other side's length is 1.
        For rotation of radian x, the other side's length is cos(x) + sin(x).

        In that case, the output of three centers are as follows:
        0.5*cos(x) 0.5*sin(x) 0
        -0.5*sin(x) 0.5*cos(x) 0
        0 0 0.5

        The problem is reduced to given A = cos(x) + sin(x), find cos(x) and sin(x).
        Given that 1 = cos(x) ^ 2 + sin(x) ^ 2, it can be solved using quadratic equation's formula OR
        sin(2x) = A^2 - 1

        :param area: input area
        :return:
        """
        k2 = decimal.Decimal(area*area)
        one = decimal.Decimal(1.0)
        alpha = math.asin(k2 - one)/2

        cos = math.cos(alpha) * 0.5
        sin = math.sin(alpha) * 0.5

        return [(cos, sin, 0.0), (-sin, cos, 0.0), (0.0, 0.0, 0.5)]

def main():
    """ Example run:
    python3 codejam/submission.py < /Users/tdongsi/Hub/gtg/data/SaveTheUniverse.txt
    """
    solver = Solver()
    solver.solve()


if __name__ == "__main__":
    main()