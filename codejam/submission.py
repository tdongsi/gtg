
import codejam.base as bs


class Solver(bs.BaseSolver):

    def _solve(self, inputstr):
        return inputstr

    pass


def main():
    PROJECT_HOME = "/Users/tdongsi/Hub/gtg"
    solver = Solver(PROJECT_HOME + "/data/SaveTheUniverse.txt")
    with open("out.txt", "w") as f:
        solver.solve()


if __name__ == "__main__":
    main()