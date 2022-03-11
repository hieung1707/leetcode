from __future__ import annotations

from typing import List


class ListNode(object):
    def __init__(self, x: int):
        self.val = x
        self.next: ListNode = None

    def set_next(self, node: ListNode):
        self.next = node


def find_cycle_starting_point(node: ListNode, node_idx: int) -> int:
    node_val = node.val
    current_node = node.next
    node_values = []

    while current_node:
        if current_node.val in node_values:
            return node_values.index(current_node.val)

        current_node = current_node.next

    if node.next:
        find_cycle_starting_point(node.next, node_idx + 1)

    return -1


def solution(head: ListNode) -> int:
    # return find_cycle_starting_point(head, 0)
    current_node = head
    node_values = []
    sus_count = 0

    while current_node:
        if current_node.val in node_values:
            sus_count += 1
            if sus_count == 2:
                idx = node_values.index(current_node.val) - 1
                for _ in range(idx):
                    head = head.next

                return head
        else:
            node_values.append(current_node.val)
        current_node = current_node.next

    return None


def setup(heads: List[int], pos: int):
    first_node: ListNode = None
    current_node: ListNode = None
    cycle_node: ListNode = None

    for idx, head in enumerate(heads):
        node = ListNode(head)
        if idx == pos:
            cycle_node = node
        elif idx == len(heads) - 1:
            node.set_next(cycle_node)

        if not first_node:
            first_node = node
        else:
            current_node.set_next(node)

        current_node = node

    return first_node


def main():
    head = setup(heads=[-1, -7, 7, -4, 19, 6, -9, -5, -2, -5], pos=6)
    print(solution(head).val)


if __name__ == "__main__":
    main()
