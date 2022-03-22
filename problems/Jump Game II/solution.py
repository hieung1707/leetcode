def solution(nums: list):
    count = 0
    max_reach = 0
    reach = 0
    for idx, num in enumerate(nums):
        max_reach = max(max_reach, idx + num)

        if idx == reach:
            count += 1
            reach = max_reach

    return count


def main():
    nums = [2, 3, 1, 1, 4]
    print(solution(nums))


if __name__ == "__main__":
    main()
