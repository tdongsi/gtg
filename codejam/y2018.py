
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

    def _solve(self, inputstr):
        return inputstr


def main():
    PROJECT_HOME = "/Users/tdongsi/Hub/gtg"

    # solver = SaveTheUniverse(PROJECT_HOME + "/data/SaveTheUniverse.txt")
    solver = TroubleSort(PROJECT_HOME + "/data/TroubleSort.txt")

    solver.solve()


if __name__ == "__main__":
    main()