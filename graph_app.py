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
        for node_id, (nx, ny) in self.graph.nodes.items():
            dist_sq = (x - nx) ** 2 + (y - ny) ** 2
            if dist_sq <= self.node_radius ** 2:
                return node_id

        return None

    def clamp_coordinates(self, x, y, padding = 10):
        margin = self.node_radius + padding
        clamped_x = max(margin, min(x, 800 - margin))
        clamped_y = max(margin, min(y, 550 - margin))

        return clamped_x, clamped_y

    def is_valid_node_position(self, x, y):
        min_distance = self.node_radius * 4
        for node_id, (nx, ny) in self.graph.nodes.items():
            dist = ((x-nx) ** 2 + (y-ny) ** 2) ** 0.5
            if dist < min_distance:
                return False

        return True

    def on_left_click(self, event):
        clicked_node = self.get_node_at(event.x, event.y)

        if clicked_node is None:
            clamped_x, clamped_y = self.clamp_coordinates(event.x, event.y)

            if not self.is_valid_node_position(clamped_x, clamped_y):
                return

            new_id = len(self.graph.nodes) + 1
            self.graph.add_node(new_id, clamped_x, clamped_y)
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
        clicked_node = self.get_node_at(event.x, event.y)

        if clicked_node is not None:
            if self.start_node == clicked_node:
                self.start_node = None
            else:
                self.start_node = clicked_node

            self.paths = {}
            self.path_list = []
            self.current_path_idx = 0
            self.prev_button.config(state = tk.DISABLED)
            self.next_button.config(state = tk.DISABLED)
            self.path_label.config(text = "Path: 0/0")

            self.redraw()

    def redraw(self):
        self.canvas.delete("all")

        active_path = []
        if self.path_list and 0 <= self.current_path_idx < len(self.path_list):
            active_path = self.path_list[self.current_path_idx]

        active_edges = set(zip(active_path[:-1], active_path[1:]))
        active_nodes = set(active_path)

        for u, neighbors in self.graph.adj.items():
            x1, y1 = self.graph.nodes[u]
            for v in neighbors:
                x2, y2 = self.graph.nodes[v]

                dx, dy = x2 - x1, y2 - y1
                dist = (dx**2 + dy**2)**0.5
                if dist > 0:
                    target_x = x2 - (dx / dist) * self.node_radius
                    target_y = y2 - (dy / dist) * self.node_radius
                else:
                    target_x, target_y = x2, y2

                if (u, v) in active_edges:
                    edge_color = "#28a745"
                    edge_width = 3
                else:
                    edge_color = "#6c757d"
                    edge_width = 1

                self.canvas.create_line(
                    x1, y1, target_x, target_y,
                    arrow = tk.LAST, arrowshape = (10, 12, 5),
                    fill = edge_color, width = edge_width
                )

        for node_id, (x, y) in self.graph.nodes.items():
            r = self.node_radius
            fill_color = "#f8f9fa"
            outline_color = "#343a40"
            outline_width = 2

            if node_id in active_nodes:
                fill_color = "#d4edda"
                outline_color = "#28a745"
                outline_width = 3

            if node_id == self.start_node:
                fill_color = "#fff3cd"
                outline_color = "#ffc107"
                outline_width = 3

            if node_id == self.selected_node_for_edge:
                outline_color = "#007bff"
                outline_width = 3

            self.canvas.create_oval(
                x - r, y - r, x + r, y + r,
                fill = fill_color, outline = outline_color, width = outline_width
            )

            self.canvas.create_text(
                x, y,
                text = str(node_id), font = ("Courier", 10, "bold"), fill = "#212529"
            )

    def show_prev(self):
        if self.current_path_idx > 0:
            self.current_path_idx -= 1
            self.path_label.config(text = f"Path: {self.current_path_idx + 1}/{len(self.path_list)}")
            self.next_button.config(state = tk.NORMAL)

            if self.current_path_idx == 0:
                self.prev_button.config(state = tk.DISABLED)

            self.redraw()

    def show_next(self):
        if self.current_path_idx < len(self.path_list) - 1:
            self.current_path_idx += 1
            self.path_label.config(text=f"Path: {self.current_path_idx + 1}/{len(self.path_list)}")
            self.prev_button.config(state=tk.NORMAL)

            if self.current_path_idx == len(self.path_list) - 1:
                self.next_button.config(state=tk.DISABLED)

            self.redraw()

    def run_algorithms(self):
        if not self.graph.nodes:
            messagebox.showwarning(title = "Warning", message = "There are no nodes in the graph!")
            return

        if self.start_node is None:
            messagebox.showwarning(title = "Warning", message = "Please select a start node using right-click!")
            return

        if self.graph.has_cycles():
            messagebox.showerror(title = "Error", message = "The graph contains cycles! The algorithm requires a DAG.")
            return

        dist, self.paths = self.graph.shortest_path_from_source(self.start_node)

        self.path_list = [path for path in self.paths.values() if len(path) > 1]
        self.current_path_idx = 0

        if self.path_list:
            self.path_label.config(text = f"Path: 1/{len(self.path_list)}")
            self.prev_button.config(state = tk.DISABLED)

            if len(self.path_list) > 1:
                self.next_button.config(state = tk.NORMAL)
            else:
                self.next_button.config(state = tk.DISABLED)

        else:
            self.path_label.config(text = "No reachable paths!")
            self.prev_button.config(state = tk.DISABLED)
            self.next_button.config(state = tk.DISABLED)

        self.redraw()

    def reset_graph(self):
        pass