def solution(nums: list):
    prev_num = None
    current_valid_idx = 0

    for idx, num in enumerate(nums):
        if prev_num is None or num != prev_num:
            prev_num = num
            nums[current_valid_idx] = num
            current_valid_idx += 1

    return current_valid_idx


def main():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    print(solution(nums))


if __name__ == "__main__":
    main()
