def solution(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # set max area to 0
    max_area = 0
    # set left index to 0 and right index to last index of array
    left = 0
    right = len(height) - 1

    # while left index is smaller than right index
    while left < right:
        # find area formed by 2 bars
        # the area is the smallest of the 2 bars multiplied by the distance between them
        area = min(height[left], height[right]) * (right - left)

        # if are is greater than max area, update max area
        if area > max_area:
            max_area = area

        # if the bar on the left is smaller than the bar on the right, increment left index,
        # else decrement right index
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution(height))


if __name__ == "__main__":
    main()
