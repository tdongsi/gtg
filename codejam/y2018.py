
import itertools
import math
import decimal
import sys

import codejam.base as bs


class SaveTheUniverse(bs.BaseSolver):
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
                # print(charge)
                damage -= charge[idx]

        return count


class TroubleSort(bs.BaseSolver):
    """ Google Code Jam 2018.
    https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb
    """

    def _solve(self, inputstr):
        numbers = [int(e) for e in inputstr.split()]
        sorted_nums = self._trouble_sort(numbers)

        idx = 'OK'
        for i in range(len(numbers)-1):
            if sorted_nums[i] > sorted_nums[i+1]:
                return str(i)

        return idx

    def _trouble_sort(self, mlist):
        """ Trouble sorting is equivalent to sorting odd elements and even elements in place.

        :param mlist:
        :return:
        """
        temp = [0] * len(mlist)
        temp[::2]= sorted(mlist[::2])
        temp[1::2] = sorted(mlist[1::2])

        return temp

    def _trouble_sort_naive(self, mlist):
        """Naive Implementation of TroubleSort"""
        done = False

        if not mlist or len(mlist) <= 2:
            return mlist

        while not done:
            done = True
            for i in range(len(mlist)-2):
                if mlist[i] > mlist[i+2]:
                    mlist[i], mlist[i+2] = mlist[i+2], mlist[i]
                    done = False

        return mlist


class CubeUfo(bs.BaseSolver):
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


class GoGopher():
    """ Google Code Jam 2018.
    https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/0000000000007a30
    """

    def solve(self):
        T = int(input())
        for _ in range(T):
            A = int(input())
            self._compute(A)
        pass

    def _compute(self, A):
        print("10 10")
        sys.stdout.flush()
        a, b = map(int, input().split())
        pass


def main():
    PROJECT_HOME = "/Users/tdongsi/Hub/gtg"

    # solver = SaveTheUniverse(PROJECT_HOME + "/data/SaveTheUniverse.txt")
    solver = TroubleSort(PROJECT_HOME + "/data/TroubleSort.txt")
    # solver = CubeUfo(PROJECT_HOME + "/data/CubeUfo.txt")

    solver.solve()


if __name__ == "__main__":
    main()