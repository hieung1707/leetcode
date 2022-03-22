def solution(nums1: list, m: int, nums2: list, n: int):
    current_idx = 0
    nums_1_idx = 0
    nums_2_idx = 0
    additional_idx = 0

    while nums_1_idx < m and nums_2_idx < n:
        if nums1[additional_idx + nums_1_idx] <= nums2[nums_2_idx]:
            nums_1_idx += 1

        else:
            for idx in range(additional_idx + m - 1, additional_idx + nums_1_idx - 1, -1):
                nums1[idx + 1] = nums1[idx]

            nums1[nums_1_idx + nums_2_idx] = nums2[nums_2_idx]
            additional_idx += 1
            nums_2_idx += 1

        current_idx += 1

    while nums_1_idx < m:
        nums1[nums_1_idx + nums_2_idx] = nums1[additional_idx + nums_1_idx]
        nums_1_idx += 1

    while nums_2_idx < n:
        nums1[nums_1_idx + nums_2_idx] = nums2[nums_2_idx]
        nums_2_idx += 1

    return nums1


def main():
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3

    print(solution(nums1, m, nums2, n))


if __name__ == "__main__":
    main()
