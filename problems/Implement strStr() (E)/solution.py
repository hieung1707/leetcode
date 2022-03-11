def solution(haystack: str, needle: str):
    return haystack.index(needle) if needle in haystack else -1


def main():
    test_cases = [
        ("hello", "ll"),
        ("aaaaa", "bba"),
        ("", "")
    ]

    for haystack, needle in test_cases:
        print(solution(haystack, needle))


if __name__ == "__main__":
    main()
