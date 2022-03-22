def solution(x):
    low = 0
    high = x

    while low < high:
        val = (high + low + 1) // 2
        print(low, high, val)

        squared_val = val * val

        if squared_val > x:
            high = val - 1
        else:
            low = val

    return low


def main():
    x = 16
    print(solution(x))


if __name__ == "__main__":
    main()
