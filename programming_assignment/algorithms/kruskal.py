from .graph import Graph


def kruskal_algorithm(graph: Graph) -> Graph:
    """
    Kruskal's algorithm to find the minimum spanning tree of a graph

    Parameters:
    * graph: Graph - the graph to find the minimum spanning tree

    Return:
    * mst: Graph - the minimum spanning tree of the graph
    """

    edges = graph.get_edges().copy()
    sorted_edges = sorted(edges, key=lambda x: x[2])
    V = len(graph.get_nodes())

    mst = Graph(graph.get_nodes())
    for edge in sorted_edges:
        # Condition for faster execution
        if len(mst.get_edges()) == V - 1:
            break

        if not mst.has_cycle(edge=edge):
            mst.add_edge(edge)

    return mst
