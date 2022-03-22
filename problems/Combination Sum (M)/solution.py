def get_combinations(candidates: list, target: int, current_combination: list, outputs: list):
    for idx, candidate in enumerate(candidates):
        if candidate > target:
            continue

        for n_occurrences in range(1, (target // candidate) + 1):
            additional_value = n_occurrences * candidate

            if additional_value == target:
                outputs.append(current_combination + [candidate] * n_occurrences)
            else:
                get_combinations(candidates[idx + 1:], target - additional_value,
                                 current_combination + [candidate] * n_occurrences, outputs)


def solution(candidates: list, target: int):
    outputs = []

    get_combinations(candidates, target, [], outputs)

    print(outputs)


def main():
    candidates = [2,3,6,7]
    target = 7

    solution(candidates, target)


if __name__ == "__main__":
    main()
