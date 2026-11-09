import tkinter as tk
from tkinter import messagebox
from graph import DirectedGraph

class GraphApp:

    def __init__(self, window):
        self.window = window
        self.window.title("DFS Graph Visualizer")

        self.graph = DirectedGraph()
        self.node_radius = 20

        self.selected_node_for_edge = None
        self.start_node = None
        self.paths = {}
        self.path_list = []
        self.current_path_idx = 0

        self.canvas = tk.Canvas(self.window, bg = "white", width = 800, height = 550)
        self.canvas.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<Button-3>", self.on_right_click)

        self.control_frame = tk.Frame(self.window)
        self.control_frame.grid(row = 1, column = 0, pady = (0, 10))

        self.run_button = tk.Button(self.control_frame, text = "Run Algorithms", command = self.run_algorithms, bg = "#d4edda", font = ("Courier", 10, "bold"))
        self.run_button.grid(row = 0, column = 0, padx = 10)

        self.prev_button = tk.Button(self.control_frame, text = "< Prev", command = self.show_prev, state = tk.DISABLED, font = ("Courier", 10, "bold"))
        self.prev_button.grid(row = 0, column = 1, padx = 5)

        self.path_label = tk.Label(self.control_frame, text = "Path: 0/0", font = ("Courier", 10, "bold"))
        self.path_label.grid(row = 0, column = 2, padx = 10)

        self.next_button = tk.Button(self.control_frame, text = "Next >", command = self.show_next, state = tk.DISABLED, font = ("Courier", 10, "bold"))
        self.next_button.grid(row = 0, column = 3, padx = 5)

        self.reset_button = tk.Button(self.control_frame, text = "Reset Graph", command = self.reset_graph, bg = "#f8d7da", font = ("Courier", 10, "bold"))
        self.reset_button.grid(row = 0, column = 4, padx = 15)

    def get_node_at(self, x, y):
        for node_id, (nx, ny) in self.graph.nodes.item():
            dist_sq = (x - nx) ** 2 + (y - ny) ** 2
            if dist_sq <= self.node_radius ** 2:
                return node_id

        return None

    def on_left_click(self, event):
        clicked_node = self.get_node_at(event.x, event.y)

        if clicked_node is None:
            new_id = len(self.graph.nodes) + 1
            self.graph.add_node(new_id, event.x, event.y)
            self.selected_node_for_edge = None
            self.redraw()
            return

        if self.selected_node_for_edge is None:
            self.selected_node_for_edge = clicked_node
            self.redraw()

        elif self.selected_node_for_edge != clicked_node:
            self.graph.add_edge(self.selected_node_for_edge, clicked_node)
            self.selected_node_for_edge = None
            self.redraw()

        else:
            self.selected_node_for_edge = None
            self.redraw()

    def on_right_click(self, event):
        pass

    def show_prev(self):
        pass

    def show_next(self):
        pass

    def run_algorithms(self):
        pass

    def reset_graph(self):
        pass

    def redraw(self):
        pass