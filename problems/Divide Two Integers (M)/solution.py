def solution(dividend: int, divisor: int):
    MAX_32 = 2 ** 31

    # get sign of output
    signed = (dividend < 0) != (divisor < 0)
    output = 0

    # get absolute value of dividend and divisor
    dividend = abs(dividend)
    divisor = abs(divisor)

    # loop until dividend is less than divisor
    while dividend >= divisor:
        # divide the dividend by half for each loop
        total_times = 1
        total_sum = divisor
        last_valid_number_of_times = 0
        last_valid_sum = total_sum

        # add total_sum by itself (multiply it by 2) until dividend is less than total_sum
        while total_sum <= dividend:
            last_valid_sum = total_sum
            last_valid_number_of_times = total_times

            total_sum += total_sum
            total_times += total_times

        dividend -= last_valid_sum
        output += last_valid_number_of_times

    if signed:
        return -min(MAX_32, output)

    return min(output, MAX_32 - 1)


def main():
    dividend = -1
    divisor = -1

    print(solution(dividend, divisor))


if __name__ == "__main__":
    main()
