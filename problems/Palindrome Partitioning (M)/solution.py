def is_palindrome(s):
    start_idx = 0
    end_idx = len(s) - 1

    while start_idx <= end_idx:
        if s[start_idx] != s[end_idx]:
            return False

        start_idx += 1
        end_idx -= 1

    return True


def solution(s):
    """py
    :type s: str
    :rtype: List[List[str]]
    """

    palindromes = []
    discovered_palindromes = {}

    def create_partitions(input_str, current_palindrome):
        if input_str == "":
            palindromes.append(current_palindrome)
            return

        for string_len in range(1, len(input_str) + 1):
            if input_str[0] != input_str[string_len - 1]:
                continue

            target_str = input_str[:string_len]

            if target_str in discovered_palindromes or \
                    (target_str not in discovered_palindromes and is_palindrome(target_str)):

                discovered_palindromes[target_str] = 1
                create_partitions(input_str[string_len:], current_palindrome + [target_str])

    create_partitions(s, [])

    return palindromes


def main():
    s = "aab"
    print(solution(s))


if __name__ == "__main__":
    main()
