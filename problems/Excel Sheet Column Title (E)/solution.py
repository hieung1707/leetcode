def solution(column_number: int):
    title = ""

    while column_number > 0:
        column_number -= 1
        title = chr(column_number % 26 + ord("A")) + title
        column_number = column_number // 26

    return title


def main():
    num = 1
    print(solution(num))


if __name__ == "__main__":
    main()
