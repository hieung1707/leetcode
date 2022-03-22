def solution(nums: list):
    idx = 0
    len_nums = len(nums)

    while idx < len_nums:
        if nums[idx] == idx + 1:
            idx += 1
            continue

        elif nums[idx] <= idx:
            return nums[idx]

        tmp_idx = idx + 1
        while tmp_idx < len_nums:
            if nums[tmp_idx] == idx + 1:
                nums[tmp_idx], nums[idx] = nums[idx], nums[tmp_idx]
                break
            tmp_idx += 1

        idx += 1

    return -1


def main():
    nums = [3, 1, 3, 4, 2]
    print(solution(nums))


if __name__ == "__main__":
    main()
