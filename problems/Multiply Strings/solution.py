def solution(num1: str, num2: str):
    result = ""
    digit_positions = []

    for digit_idx2, digit2 in enumerate(reversed(num2)):
        save = 0
        for digit_idx1, digit1 in enumerate(reversed(num1)):
            multiply_output = int(digit1) * int(digit2)

            if save > 0:
                multiply_output += save

            if digit_idx1 < len(num1) - 1:
                save = multiply_output // 10
                multiply_output = multiply_output % 10

            if len(digit_positions) <= (digit_idx2 + digit_idx1):
                digit_positions.append([])

            digit_positions[digit_idx1 + digit_idx2].append(multiply_output)

    save = 0
    for idx, digits in enumerate(digit_positions):
        position_val = sum(digits)

        if save > 0:
            position_val += save

        if idx < len(digit_positions) - 1:
            save = position_val // 10
            position_val = position_val % 10

        result = str(position_val) + result

    result = result.lstrip("0")

    return result or "0"


def main():
    num1 = "9133"
    num2 = "0"

    print(solution(num1, num2))


if __name__ == "__main__":
    main()
