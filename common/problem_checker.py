import os
import glob
from pathlib import Path


def main():
    solved_problems = []
    unsolved_problems = []

    problem_dirs = glob.glob(str(Path(__file__).parents[1].joinpath("problems/*")))
    for problem_dir in problem_dirs:
        problem_name = os.path.basename(problem_dir)

        if "SUCCESS" in os.listdir(problem_dir):
            solved_problems.append(problem_name)
        else:
            unsolved_problems.append(problem_name)

    print("Solved problems ({}):\n{}".format(len(solved_problems), "\n".join(solved_problems)))
    print("-" * 30)
    print("Unsolved problems ({}):\n{}".format(len(unsolved_problems), "\n".join(unsolved_problems)))


if __name__ == "__main__":
    main()
