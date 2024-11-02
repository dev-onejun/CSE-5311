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

    def __str__(self) -> str:
        """
        Return the string representation of the graph
        """
        return f"Graph(nodes={self.__nodes}, edges={self.__edges})"

    def add_node(self, node: str) -> None:
        """
        Add a node to the graph
        """
        self.__nodes.append(node)

    def add_edge(self, edge: tuple[str, str, int]) -> None:
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

    def has_cycle(self, **args) -> bool:
        """
        Check the graph will create a cycle

        Parameters:
        * args: dict - dictionary of arguments
            - edge: tuple[str, str, int] - an additional edge to check if it will create a cycle
            - edges: list[tuple[str, str, int]] - an additional list of edges to check if it will create a cycle

        Return:
        * bool - True if adding the edge will create a cycle, False otherwise
        """

        edges = self.__edges.copy()
        if "edge" in args:
            edges.append(args["edge"])
        elif "edges" in args:
            edges += args["edges"]

        adjacency_nodes = {node: [] for node in self.__nodes}
        for source, destination, _ in edges:
            adjacency_nodes[source].append(destination)
            adjacency_nodes[destination].append(source)

        visited = set()

        def _dfs(cur_node, parent) -> bool:
            visited.add(cur_node)

            for neighbor in adjacency_nodes[cur_node]:
                if neighbor not in visited:
                    if _dfs(neighbor, cur_node):
                        return True
                elif neighbor != parent:
                    return True

            return False

        for node in self.__nodes:
            if node not in visited:
                if _dfs(node, None):
                    return True

        return False
