def solution(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    longest_common_prefix = []

    for i in range(len(strs[0])):
        if any(len(s) <= i for s in strs):
            break

        c = strs[0][i]
        if any(s[i] != c for s in strs):
            break

        longest_common_prefix.append(c)

    return "".join(longest_common_prefix)


def main():
    strs = ["flower", "flow", "flight"]
    print(solution(strs))


if __name__ == "__main__":
    main()
