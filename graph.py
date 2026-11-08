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

    def get_strongly_connected_components(self):
        finish_order = self.iterative_dfs_finish_order()

        visited = set()
        scc_list = []

        for node in reversed(finish_order):
            if node not in visited:
                component = []
                stack = [node]
                visited.add(node)

                while stack:
                    curr = stack.pop()
                    component.append(curr)

                    for neighbor in self.rev_adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)

                scc_list.append(component)

        return scc_list

    def has_cycles(self):
        sccs = self.get_strongly_connected_components()

        for comp in sccs:
            if len(comp) > 1:
                return True

            node = comp[0]
            if node in self.adj[node]:
                return True

        return False