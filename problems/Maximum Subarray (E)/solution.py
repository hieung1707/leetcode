def solution(nums: list):
    result = nums[0]
    current_sum = 0

    for num in nums:
        current_sum = max(current_sum + num, num)
        result = max(current_sum, result)

    return result


def main():
    nums = [5, 4, -1, 7, 8]
    print(solution(nums))


if __name__ == "__main__":
    main()
