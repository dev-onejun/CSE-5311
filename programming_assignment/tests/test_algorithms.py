import random

import pytest
import networkx as nx

from algorithms.graph import Graph
from algorithms.prim import prim_algorithm
from algorithms.kruskal import kruskal_algorithm


def is_equal_edges(edges1, edges2) -> bool:
    return set(tuple(sorted(edge[:2])) for edge in edges1) == set(
        tuple(sorted(edge[:2])) for edge in edges2
    )


@pytest.mark.parametrize(
    "num_nodes, num_edges",
    [
        (5, 7),
        (20, 30),
        (100, 130),
        # (10_000, 13_000),
        # (100_000_000, 130_000_000),
    ],
)
def test_prim_algorithm(num_nodes, num_edges):
    nodes = [str(i) for i in range(num_nodes)]
    edges = []

    nx_graph = nx.gnm_random_graph(num_nodes, num_edges)
    # Check for connectivity and regenerate if not connected
    while not nx.is_connected(nx_graph):
        nx_graph = nx.gnm_random_graph(num_nodes, num_edges)

    for u, v in nx_graph.edges():
        weight = random.randint(1, 100)
        nx_graph.edges[u, v]["weight"] = weight
        edges.append((str(u), str(v), weight))

    nx_mst_graph = nx.minimum_spanning_tree(nx_graph, algorithm="prim")
    nx_mst_edges = nx_mst_graph.edges(data=True)
    nx_mst_edges = [(str(u), str(v), data["weight"]) for u, v, data in nx_mst_edges]

    nx_mst_edges = sorted(nx_mst_edges, key=lambda x: (x[0], x[1]))
    print(f"nx_mst_edges {nx_mst_edges}")
    print(f"{len(nx_mst_edges)}")

    graph = Graph(nodes, edges)
    custom_mst_edges = prim_algorithm(graph).get_edges()

    print(f"graph: {graph}")
    custom_mst_edges = sorted(custom_mst_edges, key=lambda x: (x[0], x[1]))
    print(f"custom_mst_edges: {custom_mst_edges}")
    assert is_equal_edges(custom_mst_edges, nx_mst_edges)
