def solution(n):
    memo = {}

    def dp(n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n not in memo:
            memo[n] = dp(n - 1) + dp(n - 2)

        return memo[n]

    return dp(n)


def main():
    n = 30

    print(solution(n))


if __name__ == "__main__":
    main()
