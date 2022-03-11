from typing import List


def solution(nums1: List[int], nums2: List[int]):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    i = 0
    j = 0
    current_idx = 0
    median_idx = int(len(nums1) + len(nums2)) / 2
    current_value, last_value = None, None

    while i < len(nums1) and j < len(nums2) and current_idx <= median_idx:
        if nums1[i] < nums2[j]:
            tmp = nums1[i]
            i += 1
        else:
            tmp = nums2[j]
            j += 1

        last_value = current_value
        current_value = tmp

        current_idx += 1

    if current_idx <= median_idx:
        while i < len(nums1) and current_idx <= median_idx:
            last_value = current_value
            current_value = nums1[i]
            current_idx += 1
            i += 1

        while j < len(nums2) and current_idx <= median_idx:
            last_value = current_value
            current_value = nums2[j]
            current_idx += 1
            j += 1

    if (len(nums1) + len(nums2)) % 2 == 0:
        return float(last_value + current_value) / 2

    return current_value


def main():
    nums1 = [1, 2]
    nums2 = [3, 4]

    print(solution(nums1, nums2))


if __name__ == "__main__":
    main()
