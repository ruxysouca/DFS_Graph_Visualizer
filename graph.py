class DirectedGraph:

    def __init__(self):
        self.nodes ={}
        self.adj = {}
        self.rev_adj = {}

    def add_node(self, node_id, x, y):
        if node_id not in self.nodes:
            self.nodes[node_id] = (x, y)
            self.adj[node_id] = []
            self.rev_adj[node_id] = []

    def add_edge(self, u, v):
        if u in self.nodes and v in self.nodes:
            if v not in self.adj[u]:
                self.adj[u].append(v)
                self.rev_adj[v].append(u)

    def iterative_dfs_finish_order(self):
        visited = set()
        finish_order = []

        for start_node in self.nodes:
            if start_node not in visited:
                stack = [[start_node, 0]]
                visited.add(start_node)

                while stack:
                    curr, neighbor_idx = stack[-1]

                    if neighbor_idx < len(self.adj[curr]):
                        neighbor = self.adj[curr][neighbor_idx]
                        stack[-1][1] += 1

                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append([neighbor, 0])

                    else:
                        finish_order.append(curr)
                        stack.pop()

        return finish_order
