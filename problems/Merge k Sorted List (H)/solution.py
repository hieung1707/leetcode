from common.linked_list import (
    ListNode,
    print_link_list,
    build_link_list
)


def solution(lists):
    head = None
    current_node = None

    while any(lists):
        min_val = None
        list_index = None
        list_len = len(lists)

        for idx, target_node in enumerate(reversed(lists)):
            if not target_node:
                continue

            if min_val is None or min_val > target_node.val:
                min_val = target_node.val
                list_index = idx

        lists[list_len - 1 - list_index] = lists[list_len - 1 - list_index].next

        if not lists[list_len - 1 - list_index]:
            lists.pop(list_len - 1 - list_index)

        node = ListNode(val=min_val)

        if not head:
            head = node

        if current_node:
            current_node.next = node

        current_node = node

    return head


def main():
    input_list = [[0], [1]]

    ll_list = [build_link_list(ll) for ll in input_list]

    print_link_list(solution(ll_list))


if __name__ == "__main__":
    main()
