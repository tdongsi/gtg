
from codejam.y2018 import SaveTheUniverse as Solver

def main():
    PROJECT_HOME = "/Users/tdongsi/Hub/gtg"
    solver = Solver(PROJECT_HOME + "/data/SaveTheUniverse.txt")
    with open("out.txt", "w") as f:
        solver.solve()


if __name__ == "__main__":
    main()