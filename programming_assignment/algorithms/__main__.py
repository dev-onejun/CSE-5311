"""
CSE-5311: Design and Analysis of Algorithms
Fall 2024, Computer Science and Engineering, University of Texas at Arlington, Arlington, TX, USA
Professor: Dr. Negin Fraidouni

Writer: Wonjun Park
UTA ID: 1002237177
wxp7177@mavs.uta.edu

Programming Assignment 1

- Lint: Black
"""

if __name__ == "__main__":
    """
    This is the test purpose code for the prim_algorithm function.
    Will erase before submitting.
    """
    import random
    import networkx as nx

    from graph import Graph
    from prim import prim_algorithm

    NUM_NODES = 20
    NUM_EDGES = 30

    nodes = [str(i) for i in range(NUM_NODES)]
    edges = []

    nx_graph = nx.gnm_random_graph(NUM_NODES, NUM_EDGES)
    # Check for connectivity and regenerate if not connected
    while not nx.is_connected(nx_graph):
        nx_graph = nx.gnm_random_graph(NUM_NODES, NUM_EDGES)

    for u, v in nx_graph.edges():
        weight = random.randint(1, 100)
        nx_graph.edges[u, v]["weight"] = weight
        edges.append((str(u), str(v), weight))

    nx_mst_graph = nx.minimum_spanning_tree(nx_graph, algorithm="prim")
    nx_mst_edges = nx_mst_graph.edges(data=True)
    nx_mst_edges = [(str(u), str(v), data["weight"]) for u, v, data in nx_mst_edges]

    print(f"nx_mst_edges {nx_mst_edges}")
    print(f"{len(nx_mst_edges)}")

    graph = Graph(nodes, edges)
    print(f"graph: {graph}")

    custom_mst_edges = prim_algorithm(graph).get_edges()

    print(f"custom_mst_edges: {custom_mst_edges}")
