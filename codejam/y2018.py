
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

    def _compute(self, limit: int, program: str):

        count = 0
        damage = self._compute_damage(program)
        while damage > limit:
            idx = program.rfind('CS')
            if idx == -1:
                raise ValueError('Impossible')
            else:
                count += 1
                program = program[:idx] + 'SC' + program[idx+2:]
                # print(program)
                damage = self._compute_damage(program)

        return count


def main():
    PROJECT_HOME = "/Users/tdongsi/Hub/gtg"
    solver = SaveTheUniverse(PROJECT_HOME + "/data/SaveTheUniverse.txt")
    with open("out.txt", "w") as f:
        solver.solve()


if __name__ == "__main__":
    main()