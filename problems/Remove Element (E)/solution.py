def solution(nums: list, val: int):
    start_remove_index = None
    removed_elements = 0

    idx = 0
    max_array_len = len(nums)

    while idx < max_array_len:
        if nums[idx] == val:
            if start_remove_index is None:
                start_remove_index = idx

            removed_elements += 1

        else:
            if start_remove_index is not None:
                tmp = start_remove_index

                for i in range(idx, max_array_len):
                    nums[start_remove_index] = nums[i]
                    start_remove_index += 1

                max_array_len -= removed_elements
                removed_elements = 0
                idx = tmp

            start_remove_index = None

        idx += 1

    # print(removed_elements)

    return max_array_len - removed_elements


def main():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2

    print(solution(nums, val))


if __name__ == "__main__":
    main()
