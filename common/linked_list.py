# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Value: {self.val}; next value: {self.next.val if self.next else None}"


def build_link_list(l: list):
    head: ListNode = None
    current_node: ListNode = None

    for element in l:
        node = ListNode(val=element)

        if not head:
            head = node

        if current_node:
            current_node.next = node

        current_node = node

    return head


def print_link_list(ll: ListNode):
    output_list = []

    while ll:
        output_list.append(ll.val)
        ll = ll.next

    print(output_list)
