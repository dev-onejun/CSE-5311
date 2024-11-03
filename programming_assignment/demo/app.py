import random

import matplotlib.pyplot as plt
import networkx as nx

from pyscript import display, document
from pyscript.web import page

from algorithms import Graph
from algorithms import (
    prim_algorithm,
    kruskal_algorithm_with_path_compression,
)


def make_graph(num_nodes: int, num_edges: int) -> tuple[Graph, nx.Graph]:
    nodes = [str(i) for i in range(num_nodes)]
    edges = []

    nx_graph = nx.gnm_random_graph(num_nodes, num_edges)
    while not nx.is_connected(nx_graph):
        nx_graph = nx.gnm_random_graph(num_nodes, num_edges)

    for u, v in nx_graph.edges():
        weight = random.randint(1, 100)
        nx_graph.edges[u, v]["weight"] = weight
        edges.append((str(u), str(v), weight))

    return Graph(nodes, edges), nx_graph


def make_figure(mst: Graph, nx_graph: nx.Graph):
    num_steps = len(mst.get_edges())
    cols = 3
    rows = (num_steps + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
    axes = axes.flatten()

    pos = nx.spring_layout(nx_graph)

    i, mst_so_far = 0, []  # Keep track of edges added to the MST
    for i, (u, v, weight) in enumerate(mst.get_edges()):
        u, v = int(u), int(v)
        mst_so_far.append((u, v))

        axes[i].cla()
        nx.draw(
            nx_graph,
            pos,
            ax=axes[i],
            with_labels=True,
            node_color="lightgray",
            edge_color="gray",
        )
        nx.draw_networkx_edges(
            nx_graph,
            pos,
            edgelist=mst_so_far,
            ax=axes[i],
            edge_color="red",
            width=2,
        )
        nx.draw_networkx_edge_labels(
            nx_graph,
            pos,
            edge_labels={(u, v): d["weight"] for u, v, d in nx_graph.edges(data=True)},
            ax=axes[i],
        )

        axes[i].set_title(f"Step {i + 1}: Add edge ({u}, {v})")

    # Hide any empty axes
    for j in range(i + 1, len(axes)):
        axes[j].axis("off")
    plt.tight_layout()

    return fig


def generate(event):
    num_nodes = document.querySelector("#num_nodes").value
    num_edges = document.querySelector("#num_edges").value

    graph, nx_graph = make_graph(int(num_nodes), int(num_edges))

    mst_prim = prim_algorithm(graph)
    mst_kruskal = kruskal_algorithm_with_path_compression(graph)

    prim_fig = make_figure(mst_prim, nx_graph)
    # prim_fig.suptitle("Prim's Algorithm", fontsize=16)
    kruskal_fig = make_figure(mst_kruskal, nx_graph)
    # kruskal_fig.suptitle("Kruskal's Algorithm", fontsize=16)

    fig_titles = page.find(".fig-title")
    for fig_title in fig_titles:
        fig_title.style["display"] = "block"

    display(prim_fig, target="prim")
    display(kruskal_fig, target="kruskal")
