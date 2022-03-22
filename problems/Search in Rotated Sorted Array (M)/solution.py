def find_peak(nums: list, low: int, high):
    if high - low == 1:
        return low

    first_element = nums[low]
    median_index = (high + low) // 2
    median_element = nums[median_index]

    # if median element is greater than the first => peak might be on the right side
    if median_element >= first_element:
        return find_peak(nums, median_index, high)
    # else peak is on left side
    else:
        return find_peak(nums, low, median_index)


def binary_search(nums: list, low: int, high: int, target: int):
    if low >= high:
        return -1

    pivot_idx = (high + low) // 2
    pivot_val = nums[pivot_idx]

    if pivot_val == target:
        return pivot_idx
    elif target > pivot_val:
        return binary_search(nums, pivot_idx + 1, high, target)
    else:
        return binary_search(nums, low, pivot_idx, target)


def solution(nums: list, target: int):
    if not nums:
        return -1

    pivot_index = (find_peak(nums, 0, len(nums)) + 1) % len(nums)

    if target >= nums[0]:
        return binary_search(nums, 0, (pivot_index - 1) % len(nums) + 1, target)
    else:
        return binary_search(nums, pivot_index, len(nums), target)


def main():
    nums = [4,5,6,7,0,1,2]
    target = 0

    print(solution(nums, target))


if __name__ == "__main__":
    main()
