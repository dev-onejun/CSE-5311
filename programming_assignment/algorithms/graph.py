class Graph(object):
    def __init__(self, nodes: list[str] = [], edges: list[tuple[str, str, int]] = []):
        """
        Parameters:
            * self.__nodes: list[str] - list of nodes in the graph
                - ex. ['1', '3', '5']
            * self.__edges: dict[str, list[str]] - dictionary of edges in the graph
                -ex. [
        """
        self.__nodes: list[str] = nodes
        self.__edges: list[tuple[str, str, int]] = []

        for edge in edges:
            self.__edges.append(edge)

    def add_node(self, node: str):
        """
        Add a node to the graph
        """
        self.__nodes.append(node)

    def add_edge(self, edge: tuple[str, str, int]):
        """
        Add an edge to the graph
        """
        self.__edges.append(edge)

    def get_nodes(self) -> list[str]:
        """
        Return the nodes in the graph
        """
        return self.__nodes

    def get_edges(self) -> list[tuple[str, str, int]]:
        """
        Return the edges in the graph
        """
        return self.__edges

    def __str__(self) -> str:
        """
        Return the string representation of the graph
        """
        return f"Graph(nodes={self.__nodes}, edges={self.__edges})"

    '''
    def __len__(self) -> int:
        """
        Return the number of nodes in the graph
        """
        return len(self.__nodes)
        '''
