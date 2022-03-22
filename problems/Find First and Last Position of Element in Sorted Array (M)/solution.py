def solution(nums: list, target: int):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    first_index = left

    right = len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    last_index = right - 1

    return [first_index, last_index] if first_index <= last_index else [-1, -1]


def main():
    nums = [5, 7, 7, 8, 8, 10]
    target = 6

    print(solution(nums, target))


if __name__ == "__main__":
    main()
