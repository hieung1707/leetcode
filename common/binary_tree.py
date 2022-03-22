class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_nodes_inorder(root: list):
    if not root:
        return None

    val = root.pop(0)
    if not val:
        return None

    node = TreeNode(val)
    if val:
        node.left = build_tree_nodes_inorder(root)
        node.right = build_tree_nodes_inorder(root)

    return node


def traverse_tree(root, output):
    if root.left:
        traverse_tree(root.left, output)

    output.append(root.val)

    if root.right:
        traverse_tree(root.right, output)


def main():
    r = [1, None, 2, 3]
    root = build_tree_nodes_inorder(r)

    output = []
    queue = [root]
    traversed_list = []

    while queue:
        node = queue[0]

        if node.left and node.left not in traversed_list:
            queue.insert(0, node.left)
            continue

        queue.pop(0)
        traversed_list.append(node)
        output.append(node.val)

        if node.right and node.right not in traversed_list:
            queue.insert(0, node.right)

    print(output)
    return output


if __name__ == "__main__":
    main()
