
import sys


class Solver():

    def __init__(self, filename):
        """ Initialize with the given input file.

        :param filename: input file path
        :return:
        """
        self._filename = filename
        pass

    def solve(self, output=sys.stdout):
        """ Handle input and output before calling an internal method to solve the problem.

        :param output: specify output to file or screen.
        :return:
        """
        try:
            with open(self._filename, 'r') as f:
                lines = f.readlines()

                for case_num, line in enumerate(lines[1:], start=1):
                    result = self._solve(line.strip())
                    output.write("Case #%d: %s\n" % (case_num, result))

        except IOError:
            print("Error opening file")
        pass

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