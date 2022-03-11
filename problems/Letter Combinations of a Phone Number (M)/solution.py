def solution(digits: str):
    """
    :type digits: str
    :rtype: List[str]
    """

    digit_letters_mapping = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": ""
    }

    combinations = []

    if not digits:
        return combinations

    for character in digit_letters_mapping.get(digits[0]):
        subcombs = solution(digits[1:])
        if subcombs:
            combinations.extend([character + comb for comb in subcombs])
        else:
            combinations.append(character)

    return combinations


def main():
    digits = "23"
    print(solution(digits))


if __name__ == "__main__":
    main()
