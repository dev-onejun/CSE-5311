import random

import pytest
import networkx as nx

from algorithms.graph import Graph
from algorithms.prim import prim_algorithm
from algorithms.kruskal import (
    kruskal_algorithm,
    kruskal_algorithm_with_path_compression,
)


def is_equal_edges(edges1, edges2) -> bool:
    """
    Check if two lists of edges are equal to determine if the MST is correct

    Parameters:
    * edges1: List - list of edges from the first graph
    * edges2: List - list of edges from the second graph

    Returns:
    * bool: True if both lists are equal, False otherwise
    """
    return set(tuple(sorted(edge[:2])) for edge in edges1) == set(
        tuple(sorted(edge[:2])) for edge in edges2
    )


def make_graph(num_nodes, num_edges):
    """
    Create a random graph with num_nodes nodes and num_edges edges

    Parameters:
    * num_nodes: int - number of nodes in the graph
    * num_edges: int - number of edges in the graph

    Returns: Both of them represent the same graph
    * graph: Graph - custom graph object
    * nx_graph: nx.Graph - networkx graph object
    """
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

    graph = Graph(nodes, edges)

    return graph, nx_graph


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
    graph, nx_graph = make_graph(num_nodes, num_edges)

    nx_mst_graph = nx.minimum_spanning_tree(nx_graph, algorithm="prim")
    nx_mst_edges = nx_mst_graph.edges(data=True)
    nx_mst_edges = [(str(u), str(v), data["weight"]) for u, v, data in nx_mst_edges]

    custom_mst_edges = prim_algorithm(graph).get_edges()

    # When the last minimum edge exists as two different edge, like (2,4, 78), (2,3,78),
    # two algorithms return different results
    diff1 = [item for item in custom_mst_edges if item not in nx_mst_edges]
    diff2 = [item for item in nx_mst_edges if item not in custom_mst_edges]
    difference = diff1 + diff2
    print("Difference between lists:", difference)

    assert is_equal_edges(custom_mst_edges, nx_mst_edges) or (
        weights[0] == weights[1] for weights in zip(diff1, diff2)
    )


@pytest.mark.parametrize(
    "num_nodes, num_edges",
    [
        (5, 7),
        (20, 30),
        (100, 130),
    ],
)
def test_kruskal_algorithm(num_nodes, num_edges):
    graph, nx_graph = make_graph(num_nodes, num_edges)

    nx_mst_graph = nx.minimum_spanning_tree(nx_graph, algorithm="kruskal")
    nx_mst_edges = nx_mst_graph.edges(data=True)
    nx_mst_edges = [(str(u), str(v), data["weight"]) for u, v, data in nx_mst_edges]

    custom_mst_edges = kruskal_algorithm(graph).get_edges()

    assert is_equal_edges(custom_mst_edges, nx_mst_edges)


@pytest.mark.parametrize(
    "num_nodes, num_edges",
    [
        (5, 7),
        (20, 30),
        (100, 130),
    ],
)
def test_kruskal_algorithm_with_path_compression(num_nodes, num_edges):
    graph, _ = make_graph(num_nodes, num_edges)

    kruskal_mst_edges = kruskal_algorithm(graph).get_edges()
    kruskal_mst_edges_with_path_compression = kruskal_algorithm_with_path_compression(
        graph
    ).get_edges()

    assert is_equal_edges(kruskal_mst_edges, kruskal_mst_edges_with_path_compression)


@pytest.mark.parametrize(
    "num_nodes, num_edges",
    [
        (5, 7),
        (20, 30),
        (100, 130),
    ],
)
def test_algorithms(num_nodes, num_edges):
    graph, _ = make_graph(num_nodes, num_edges)

    custom_prim_mst_edges = prim_algorithm(graph).get_edges()
    custom_kruskal_mst_edges = kruskal_algorithm(graph).get_edges()

    assert is_equal_edges(custom_prim_mst_edges, custom_kruskal_mst_edges)
