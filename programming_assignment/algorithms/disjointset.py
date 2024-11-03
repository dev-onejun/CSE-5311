class DisjointSet(object):
    def __init__(self, nodes: list[str]):
        """
        Initialize the disjoint set with the nodes
        """

        self.__parent: dict[str, str] = {node: node for node in nodes}
        self.__rank: dict[str, int] = {node: 0 for node in nodes}

    def find(self, node: str) -> str:
        """
        Find the representative of the set containing the `node`
        """

        # Path Compression
        if self.__parent[node] != node:
            self.__parent[node] = self.find(self.__parent[node])

        return self.__parent[node]

    def union(self, node1: str, node2: str):
        """
        Union the sets containing the `node1` and `node2`
        """

        root1, root2 = self.find(node1), self.find(node2)

        # Union by Rank
        if self.__rank[root1] < self.__rank[root2]:
            self.__parent[root1] = root2
        elif self.__rank[root1] > self.__rank[root2]:
            self.__parent[root2] = root1
        else:
            self.__parent[root2] = root1
            self.__rank[root1] += 1
