def solution(s: str):

    # stack is initiated with -1 to input string is ()
    stack = [-1]

    l = 0
    # loop through string
    for i, p in enumerate(s):
        if p == "(":
            stack.append(i)
        else:
            stack.pop()

        # if no element in stack, append the current index
        if len(stack) == 0:
            stack.append(i)
        else:
            # calculate the longest chain of parentheses, which is current index minus the last element in stack,
            # or current longest record, whichever is longer.
            # There are 2 cases that can happen:
            # case #1: p = "(", => stack just pushed i, then i - stack[-1] ( = i) = 0
            # case #2: p = ")" => stack just pop the last element on stack
            #   => stack[-1] = the last position BEFORE the valid parentheses, this will
            l = max(l, i - stack[-1])

    return l


def main():
    testcases = [
        ")()",
        "(()",
        ")()())",
        "",
        "()",
        "(()(((())))()"
    ]

    for testcase in testcases:
        print(solution(testcase))


if __name__ == "__main__":
    main()
