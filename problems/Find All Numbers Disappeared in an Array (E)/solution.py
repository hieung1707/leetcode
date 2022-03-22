def solution(nums: list):
    current_num = 1

    nums.sort()
    missing_numbers = []
    prev_num = None
    sum_nums = 0

    for num in nums:
        if num == prev_num:
            continue

        while num != current_num:
            missing_numbers.append(current_num)
            current_num += 1

        prev_num = num
        sum_nums += num
        current_num += 1

    while current_num <= len(nums):
        missing_numbers.append(current_num)
        current_num += 1

    missing_val = sum(range(1, len(nums) + 1)) - sum_nums - sum(missing_numbers)

    if missing_val and missing_val not in missing_numbers:
        missing_numbers.append(missing_val)

    return missing_numbers


def main():
    nums = [4, 3, 2, 7, 8, 2, 3, 1]

    print(solution(nums))


if __name__ == "__main__":
    main()
