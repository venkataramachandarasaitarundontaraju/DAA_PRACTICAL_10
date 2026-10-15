from typing import List, Tuple

class DisjointSet:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def kruskals_algorithm(vertices_count: int, edges: List[Tuple[int, int, int]]) -> Tuple[float, List[Tuple[int, int, int]]]:
    sorted_edges = sorted(edges, key=lambda item: item[2])
    dsu = DisjointSet(vertices_count)
    mst_edges = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == vertices_count - 1:
                break

    if len(mst_edges) == vertices_count - 1 or vertices_count == 1:
        return float(total_weight), mst_edges
    else:
        return float('inf'), []

if __name__ == "__main__":
    V = 5
    edge_list: List[Tuple[int, int, int]] = []

    def add_edge(u: int, v: int, w: int) -> None:
        edge_list.append((u, v, w))

    add_edge(0, 1, 2)
    add_edge(0, 3, 6)
    add_edge(1, 2, 3)
    add_edge(1, 3, 8)
    add_edge(1, 4, 5)
    add_edge(2, 4, 7)
    add_edge(3, 4, 9)

    mst_weight, mst_structure = kruskals_algorithm(V, edge_list)

    print(f"Total MST Weight: {mst_weight}")
    for parent_node, child_node, edge_weight in mst_structure:
        print(f"Edge: {parent_node} -> {child_node} (Weight: {edge_weight})")
