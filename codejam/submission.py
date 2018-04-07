
from abc import ABCMeta, abstractmethod
import sys


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
    https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb
    """

    def _solve(self, inputstr):
        return inputstr


def main():
    """ Example run:
    python3 codejam/submission.py < /Users/tdongsi/Hub/gtg/data/SaveTheUniverse.txt
    """
    solver = Solver()
    solver.solve()


if __name__ == "__main__":
    main()