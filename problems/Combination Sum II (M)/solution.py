def get_combinations(candidates: list, target: int, current_combination: list, outputs: list, n_occurrences_dict: dict):
    for idx, candidate in enumerate(candidates):
        if candidate > target:
            continue

        for n_occurrences in range(1, n_occurrences_dict.get(candidate) + 1):
            additional_value = n_occurrences * candidate

            if additional_value > target:
                break

            if additional_value == target:
                outputs.append(current_combination + [candidate] * n_occurrences)
            else:
                get_combinations(candidates[idx + 1:], target - additional_value,
                                 current_combination + [candidate] * n_occurrences, outputs, n_occurrences_dict)


def solution(candidates: list, target: int):
    outputs = []

    n_occurrences_dict = {}

    modified_candidates = []

    for candidate in candidates:
        if candidate not in n_occurrences_dict:
            n_occurrences_dict[candidate] = 0
            modified_candidates.append(candidate)

        n_occurrences_dict[candidate] += 1

    get_combinations(modified_candidates, target, [], outputs, n_occurrences_dict)

    print(outputs)


def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    solution(candidates, target)


if __name__ == "__main__":
    main()
