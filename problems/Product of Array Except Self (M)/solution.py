def solution(nums):
    product = 1

    num_zeros = 0

    for num in nums:
        if num == 0:
            num_zeros += 1
            continue

        product *= num

    if num_zeros > 1:
        return [0] * len(nums)

    if num_zeros == 1:
        return [product if num == 0 else 0 for num in nums]

    return [product // num for num in nums]


def main():
    nums = [-1, 1, 0, -3, 3]
    print(solution(nums))
