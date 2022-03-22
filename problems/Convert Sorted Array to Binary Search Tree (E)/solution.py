from common.binary_tree import TreeNode


def create_tree(nums, low, high):
    if low >= high:
        return None

    pivot_index = (low + high) // 2
    center_val = nums[pivot_index]

    if center_val is None:
        return None

    node = TreeNode(val=center_val)

    node.left = create_tree(nums, low, pivot_index)
    node.right = create_tree(nums, pivot_index + 1, high)

    return node


def solution(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    return create_tree(nums, 0, len(nums))


def print_tree_lcr(root: TreeNode):
    if not root:
        return

    if root.left:
        print_tree_lcr(root.left)

    print(root.val)

    if root.right:
        print_tree_lcr(root.right)


def main():
    nums = [-10, -3, 0, 5, 9]
    print_tree_lcr(solution(nums))


if __name__ == "__main__":
    main()
