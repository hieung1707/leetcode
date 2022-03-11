def solution(s: str):
    roman_dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    roman_length = len(s)

    idx = 0
    value = 0
    while idx < roman_length:
        next_roman = None
        current_roman = s[idx]
        if idx < roman_length - 1:
            next_roman = s[idx + 1]

        if next_roman and roman_dict[next_roman] > roman_dict[current_roman]:
            value += roman_dict[next_roman] - roman_dict[current_roman]
            idx += 1

        else:
            value += roman_dict[current_roman]

        idx += 1

    return value


def main():
    s = "MCMXCIV"
    print(solution(s))


if __name__ == "__main__":
    main()
