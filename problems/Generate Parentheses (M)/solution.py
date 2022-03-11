def solve(ans: list, o: int, c: int, res: str):
    # if all open and close brackets are used up, append the answer to list
    if o == c == 0:
        ans.append(res)

    # the key here is 'if', and not 'elif', as the function will try to loop through all open brackets,
    # AND then add close brackets to the current iteration
    # E.g:
    # +-----------+------+-------+
    # | iteration | open | close |
    # +-----------+------+-------+
    # | 1         | 2    | 2     |
    # +-----------+------+-------+
    # | 2         | 1    | 2     |
    # +-----------+------+-------+
    # | 3         | 0    | 2     |
    # +-----------+------+-------+
    # | 4         | 0    | 1     |
    # +-----------+------+-------+
    # | 5         | 0    | 0     |
    # +-----------+------+-------+
    # | 6         | 1    | 1     |
    # +-----------+------+-------+
    # ............................

    if o > 0:
        solve(ans, o - 1, c, res + "(")

    if c > o:
        solve(ans, o, c - 1, res + ")")


def solution(n: int):
    answers = []

    solve(answers, n, n, "")

    return answers


def main():
    print(solution(4))


if __name__ == "__main__":
    main()
