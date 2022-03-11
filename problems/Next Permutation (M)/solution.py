def find_next_permutation(nums: list, permutation: list, outputs: list, prev_permutation: list):
    if not nums:
        if permutation not in outputs:
            outputs.append(permutation)
            if len(outputs) >= 2 and outputs[-2] == prev_permutation:
                return permutation

    for idx, num in enumerate(nums):
        res = find_next_permutation(nums[:idx] + nums[idx + 1:], permutation + [num], outputs, prev_permutation)

        if res:
            return res


def solution(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    outputs = []
    next_permutation = find_next_permutation(sorted(nums), [], outputs, nums)
    if not next_permutation:
        next_permutation = outputs[0]

    for idx in range(len(nums)):
        nums[idx] = next_permutation[idx]

    print(nums)


def main():
    nums = [3, 1, 4, 4, 2, 3, 4, 0, 0]
    solution(nums)


if __name__ == "__main__":
    main()
