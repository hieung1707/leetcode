def solution(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """

    heights = {}
    neighbors = {}
    min_height = float("inf")

    for idx in range(n):
        neighbors[idx] = []

    for vertex1, vertex2 in edges:
        neighbors[vertex1].append(vertex2)
        neighbors[vertex2].append(vertex1)

    for idx in range(n):
        stack = [(idx, 0)]
        traversed_vertices = []
        tree_height = 0

        while stack:
            vertex, current_height = stack.pop()
            traversed_vertices.append(vertex)

            vertex_neighbors = [n for n in neighbors[vertex] if n not in traversed_vertices]
            if not vertex_neighbors:
                tree_height = max(tree_height, current_height)
                continue

            for neighbor in vertex_neighbors:
                if neighbor in traversed_vertices:
                    continue

                stack.append((neighbor, current_height + 1))

        heights[idx] = tree_height
        if tree_height < min_height:
            min_height = tree_height

    return [node_id for node_id, height in heights.items() if height == min_height]


def main():
    n = 6
    edges = [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]
    print(solution(n, edges))


if __name__ == "__main__":
    main()
