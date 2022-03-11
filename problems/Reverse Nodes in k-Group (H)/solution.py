from common.linked_list import (
    ListNode,
    build_link_list,
    print_link_list
)


def solution(head: ListNode, k: int):
    if k == 0:
        return head

    new_head: ListNode = None
    last_adjacent_node: ListNode = None
    current_node: ListNode = head

    while current_node:
        swap_nodes = [current_node]

        tmp = current_node
        for _ in range(k - 1):
            if not tmp:
                break
            swap_nodes.append(tmp.next)
            tmp = tmp.next

        if len(swap_nodes) < k or not all(swap_nodes):
            break

        swap_nodes[0].next = swap_nodes[-1].next

        for i in range(k - 1, 0, -1):
            swap_nodes[i].next = swap_nodes[i - 1]

        if not new_head:
            new_head = swap_nodes[-1]

        if last_adjacent_node:
            last_adjacent_node.next = swap_nodes[-1]

        last_adjacent_node = current_node

        current_node = current_node.next

    return new_head or head


def main():
    test_cases = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2, 3, 4, 5], 2),
    ]

    for ll, k in test_cases:
        print(f"Test case: {k}; {ll}")
        head = build_link_list(ll)
        print_link_list(solution(head, k))


if __name__ == "__main__":
    main()
