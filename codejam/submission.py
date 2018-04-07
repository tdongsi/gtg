
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
    """
    Google Code Jam 2018.
    https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard
    """

    def _solve(self, inputstr):
        limit, program = inputstr.split()
        try:
            count = self._compute(int(limit), program)
            return str(count)
        except ValueError:
            return "IMPOSSIBLE"

    def _compute_damage(self, program):
        cur_hit = 1
        total = 0
        for c in program:
            if c == 'C':
                cur_hit *= 2
            elif c == 'S':
                total += cur_hit
        return total

    def _compute_charge(self, program):
        cur_hit = 1
        charge = [0] * len(program)
        for idx, c in enumerate(program):
            if c == 'C':
                cur_hit *= 2
            charge[idx] = cur_hit
        return charge

    def _compute(self, limit: int, program: str):

        count = 0
        damage = self._compute_damage(program)
        charge = self._compute_charge(program)
        # print(charge)
        while damage > limit:
            idx = program.rfind('CS')
            if idx == -1:
                raise ValueError('Impossible')
            else:
                count += 1
                program = program[:idx] + 'SC' + program[idx+2:]

                # damage recomputed more efficiently this way
                # O(1) instead of O(n) if using function _compute_damage(program)
                charge[idx] //= 2
                damage -= charge[idx]

        return count


def main():
    """ Example run:
    python3 codejam/submission.py < /Users/tdongsi/Hub/gtg/data/SaveTheUniverse.txt
    """
    solver = Solver()
    solver.solve()


if __name__ == "__main__":
    main()