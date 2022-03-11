def solution(num: int):
    roman_numerals = []

    roman_tuple = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                   (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

    for represent_number, roman_number in roman_tuple:
        if num <= 0:
            break

        if num < represent_number:
            continue

        n_occurrences = num // represent_number

        roman_numerals.extend(roman_number * n_occurrences)

        num -= n_occurrences * represent_number

    return "".join(roman_numerals)


def main():
    num = 58
    print(solution(num))


if __name__ == "__main__":
    main()
