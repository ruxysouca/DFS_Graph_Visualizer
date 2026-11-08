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
                