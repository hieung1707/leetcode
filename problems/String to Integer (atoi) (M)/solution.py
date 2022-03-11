def solution(s: str):
    """
            :type s: str
            :rtype: int
            """
    max_value_32 = 2 ** 31
    list_digits = list(map(str, range(0, 10)))
    s = s.lstrip()
    sign = 1

    value = 0

    for idx, c in enumerate(s):
        if idx == 0 and c in ("+", "-"):
            if c == "+":
                sign = 1
            else:
                sign = -1

        elif c in list_digits:
            value = value * 10 + int(c)
        else:
            break

    value = value * sign

    if value > max_value_32 - 1:
        return max_value_32 - 1
    elif value < -1 * max_value_32:
        return -1 * max_value_32

    return value


def main():
    print(solution("42"))


if __name__ == "__main__":
    main()
