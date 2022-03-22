from common.graph import (
    Node,
    build_connected_undirected_graph,
    print_neighbors
)


def solution(node: Node):
    if not node:
        return None

    node_hm = {}

    def dfs(n):
        if n not in node_hm:
            new_node = Node(n.val)
            node_hm[n] = new_node
            neighbors = []
            for neighbor in n.neighbors:
                if neighbor in node_hm:
                    neighbors.append(node_hm[neighbor])
                else:
                    neighbors.append(dfs(neighbor))

            new_node.neighbors = neighbors

        return node_hm[n]

    return dfs(node)


def main():
    neighbor_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
    node = build_connected_undirected_graph(neighbor_list)

    clone_node = solution(node)

    print(print_neighbors(clone_node))


if __name__ == "__main__":
    main()
