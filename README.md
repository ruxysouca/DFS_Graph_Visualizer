# DFS Graph Visualizer

An interactive python desktop application built with `tkinter` for constructing directed graphs, detecting cycles with strongly connected components, and visualizing shortest paths in directed acyclic graphs in *O(n + m)* time.

---

## Features

* **Interactive Graph Builder:**
  * **Left-Click on empty space:** Places a new node with automatic boundary clamping and minimum-distance collision prevention.
  * **Left-Click on two nodes:** Creates a directed edge (`u → v`) with directional arrow clipping at the target node's perimeter.
  * **Right-Click on a node:** Toggles the source node (`S`) highlighted in yellow.
* **Cycle Detection (Kosaraju's SCC Algorithm):** Validates whether the directed graph is acyclic before computing shortest paths, alerting the user if any cycle or self-loop is present.
* **Linear-Time DAG Shortest Paths:** Uses iterative DFS finish times to compute a topological ordering and relaxes edges in *O(n + m)* time.
* **Sequential Path Navigation:** Step through every reachable shortest path from source `S` one at a time using `< Prev` and `Next >` buttons without visual clutter.

---

## Project Structure

```text
DFS_Graph_Visualizer/
├── main.py         # Application entry point
├── graph.py        # DirectedGraph data structure & graph algorithms (Iterative DFS, Kosaraju SCC, Topological Sort, Shortest Path)
├── graph_app.py    # Tkinter GUI, canvas rendering, coordinate clamping, and user interaction handlers
├── README.md       # Project documentation
└── LICENSE         # MIT License
