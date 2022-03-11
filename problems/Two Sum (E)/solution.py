from typing import List


def solution(nums: List[int], target: int) -> List[int, int]:
    pairs = {}

    for idx, num in enumerate(nums):
        pairs[target - num] = idx

    for idx, num in enumerate(nums):
        paired_idx = pairs.get(num, None)
        if paired_idx and paired_idx != idx:
            return [idx, paired_idx]


def main():
    nums: List[int] = [1, 3, 4, 2]
    target: int = 6

    print(solution(nums, target))


if __name__ == "__main__":
    main()
