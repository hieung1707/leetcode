from common.linked_list import (
    ListNode,
    build_link_list,
    print_link_list
)


def solution(head: ListNode):
    new_head: ListNode = None
    last_adjacent_node: ListNode = None
    current_node: ListNode = head

    while current_node:
        adjacent_node = current_node.next

        if not adjacent_node:
            break

        current_node.next = adjacent_node.next
        adjacent_node.next = current_node

        if not new_head:
            new_head = adjacent_node

        if last_adjacent_node:
            last_adjacent_node.next = adjacent_node

        last_adjacent_node = current_node

        current_node = current_node.next

    return new_head or head


def main():
    test_cases = [
        [1, 2, 3, 4],
        [],
        [1]
    ]

    for test_case in test_cases:

        head = build_link_list(test_case)
        print_link_list(solution(head))


if __name__ == "__main__":
    main()
