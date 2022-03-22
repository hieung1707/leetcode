class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self):
        return f"Value: {self.val}. Neighbors: {[n.val for n in self.neighbors]}"


def build_connected_undirected_graph(node_list: list):
    hm = {}

    def build_node(node_val, neighbor_list: list):
        neighbor_vals = neighbor_list[node_val - 1]

        if node_val not in hm:
            node = Node(val=node_val)
            hm[node_val] = node

            neighbors = []
            for n_val in neighbor_vals:
                if n_val in hm:
                    neighbors.append(hm[n_val])
                else:
                    neighbors.append(build_node(n_val, neighbor_list))

            node.neighbors = neighbors

        return hm[node_val]

    return build_node(1, node_list)


def print_neighbors(node: Node):
    traversed_nodes = []

    q = [node]

    neighbors = []

    while q:
        node = q.pop(0)

        if node in traversed_nodes:
            continue

        traversed_nodes.append(node)
        neighbors.append([n.val for n in node.neighbors])
        q.extend(node.neighbors)

    return neighbors
