"""
Campus Network Design using Minimum Cost Spanning Tree
Algorithms: Prim's & Kruskal's

Goal:
Connect all campus buildings with minimum cable cost.
"""

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        # u: source building, v: destination building, w: cable cost
        self.graph.append((u, v, w))

    # ------------------ KRUSKAL'S ALGORITHM ------------------ #
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)

        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

    def kruskal_mst(self):
        result = []
        self.graph.sort(key=lambda x: x[2])  # Sort by weight
        parent, rank = [], []

        for i in range(self.V):
            parent.append(i)
            rank.append(0)

        e = 0  # edges accepted
        i = 0  # index for sorted edges

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        return result

    # ------------------ PRIM'S ALGORITHM ------------------ #
    def prim_mst(self):
        inf = float('inf')
        selected = [False] * self.V
        key = [inf] * self.V
        parent = [-1] * self.V

        key[0] = 0  # Start from building 0

        for _ in range(self.V):
            minKey = inf
            u = -1

            for v in range(self.V):
                if not selected[v] and key[v] < minKey:
                    minKey = key[v]
                    u = v

            selected[u] = True

            for v in range(self.V):
                for edge in self.graph:
                    x, y, w = edge
                    if x == u and y == v and not selected[v] and w < key[v]:
                        key[v] = w
                        parent[v] = u
                    if y == u and x == v and not selected[v] and w < key[v]:
                        key[v] = w
                        parent[v] = u

        mst = []
        for v in range(1, self.V):
            mst.append((parent[v], v, key[v]))

        return mst


# ------------------ MAIN EXECUTION ------------------ #
if __name__ == "__main__":
    print("Campus Network Design System using MST\n")

    # Example campus map (buildings as nodes)
    buildings = 6  # Let's say 6 campus buildings
    g = Graph(buildings)

    # Add building connections (u, v, cable cost)
    edges = [
        (0, 1, 4), (0, 2, 3), (1, 2, 1),
        (1, 3, 2), (2, 3, 4), (3, 4, 2),
        (4, 5, 6), (3, 5, 3)
    ]

    for u, v, w in edges:
        g.add_edge(u, v, w)

    print("Buildings: 0,1,2,3,4,5")
    print("Edges (u, v, cost):", edges, "\n")

    prim_result = g.prim_mst()
    kruskal_result = g.kruskal_mst()

    # Display Prim's result
    print("Prim's MST Result:")
    total_prim = sum(w for _, _, w in prim_result)
    for u, v, w in prim_result:
        print(f"{u} -- {v} | Cost: {w}")
    print("Total Cable Cost:", total_prim, "\n")

    # Display Kruskal's result
    print("Kruskal's MST Result:")
    total_kruskal = sum(w for _, _, w in kruskal_result)
    for u, v, w in kruskal_result:
        print(f"{u} -- {v} | Cost: {w}")
    print("Total Cable Cost:", total_kruskal, "\n")

    print("✅ MST ensures minimum-cost campus network cabling.")
