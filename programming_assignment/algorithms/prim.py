from .graph import Graph


def prim_algorithm(graph: Graph) -> Graph:
    """
    Prim's Algorithm Implementation

    Parameters:
        graph: Graph - a graph to find the MST. Defined in graph.py

    Return:
        mst_graph: Graph - a minimum spanning tree of the `graph`.
    """

    unreached_nodes: list[str] = graph.get_nodes().copy()
    edges: list[tuple[str, str, int]] = graph.get_edges().copy()

    mst_edges: list[tuple[str, str, int]] = []
    reached_nodes: list[str] = []

    reached_node = unreached_nodes[0]
    reached_nodes.append(reached_node)
    while len(reached_nodes) < len(unreached_nodes):
        candidate_edges: list[tuple[str, str, int]] = []
        for edge in edges:
            node1, node2, _ = edge

            for visited_node in reached_nodes:
                if visited_node in (node1, node2):
                    if node1 in reached_nodes and node2 in reached_nodes:
                        continue

                    candidate_edges.append(edge)

        # Find the minimum edge in regards to the priority of weight, node1, and node2
        min_edge = min(candidate_edges, key=lambda x: (x[2], x[0], x[1]))
        mst_edges.append(min_edge)
        print(min_edge)

        reached_node = min_edge[1] if min_edge[0] in reached_nodes else min_edge[0]
        reached_nodes.append(reached_node)

    mst_graph: Graph = Graph(nodes=reached_nodes, edges=mst_edges)

    return mst_graph
