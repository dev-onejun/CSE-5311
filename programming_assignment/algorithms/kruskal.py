from .graph import Graph
from .disjointset import DisjointSet


def kruskal_algorithm(graph: Graph) -> list[Graph]:
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

    mst_edges = mst.get_edges()
    mst_steps = [mst_edges[:i] for i in range(1, len(mst_edges) + 1)]
    mst_graphs: list[Graph] = []
    for step in mst_steps:
        mst_graph = Graph(nodes=mst.get_nodes(), edges=step)
        mst_graphs.append(mst_graph)

    return mst_graphs


def kruskal_algorithm_with_path_compression(graph: Graph) -> list[Graph]:
    """
    Kruskal's algorithm to find the minimum spanning tree of a graph with path compression

    Parameters:
    * graph: Graph - the graph to find the minimum spanning tree

    Return:
    * mst: Graph - the minimum spanning tree of the graph
    """

    edges = graph.get_edges().copy()
    sorted_edges = sorted(edges, key=lambda x: x[2])
    V = len(graph.get_nodes())

    mst = Graph(graph.get_nodes())
    disjoint_set = DisjointSet(graph.get_nodes())
    for edge in sorted_edges:
        # Condition for faster execution
        if len(mst.get_edges()) == V - 1:
            break

        root1, root2 = disjoint_set.find(edge[0]), disjoint_set.find(edge[1])
        if root1 != root2:
            mst.add_edge(edge)
            disjoint_set.union(edge[0], edge[1])

    mst_edges = mst.get_edges()
    mst_steps = [mst_edges[:i] for i in range(1, len(mst_edges) + 1)]
    mst_graphs: list[Graph] = []
    for step in mst_steps:
        mst_graph = Graph(nodes=mst.get_nodes(), edges=step)
        mst_graphs.append(mst_graph)

    return mst_graphs
