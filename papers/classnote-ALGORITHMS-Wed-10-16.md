$$
\begin{array}{|c|c|}
\hline
\text{} & \text{} \\
\hline
\text{} & \text{} \\
\hline
\end{array}
$$

* Weighted Graphs

    - Spanning Tree with the minimum total weights is Minimum Spanning Tree
        - How to find?
            - Naive Approach
                1) List all Spanning Tree for the graph
                2) Calculate total weight for each Spannign Tree
                3) Choose the one with the minimum weight

            - Kruskal's Algorithm (Greedy)
                1) Sort all edges by their weights in increasing order
                2) Pick the edge with the smallest weight and check if the edge forms a cycle with MST you constructed so far. If yes, discard it. If no, add it to the MST.
                3) Repeat step 2 until there are V-1 edges

                ``` plaintext
                Kruskal(G):
                    A = {}

                    for each v in G.v:
                        MakeSet(v)

                    for each (u, v) in G.E ordered by weight:
                        if FindSet(u) != FindSet(v):
                            A = A U {(u, v)}
                            Union(FindSet(u), FindSet(v))

                    return A
                ```

            - Prim's Algorithm (Dijkstra? - 다익스트라는 weigth(거리)의 누적합이고, Prim은 그때그때 최소값)
                1) Initialize MST(a 비다tree) with a vertex chosen randomly
                2) Find all edges that connect the tree to new vertices. Find the minimum and add it to tree
                3) Keep repeating step 2, until there are V-1 edges

                ``` plaintext
                Prim(G):
                    reach_set = {}
                    unreached_set = G.v
                    A = {}

                    while unreached_set is not empty:
                        find an edge e=(X, Y) which are
                            1) X in reach_set
                            2) Y in unreached_set
                            3) edge weight is the minimum

                        spanning_tree = spanning_tree U {e}
                        reach_set = reach_set U {Y}
                        unreached_set = unreached_set - {Y}
                ```

* Programming Project
    - Due Date: Nov. 10th
    - Any programming language is fine
    - TA Demo: spreadsheet 받을 거고, 거기에 입력해서 스케쥴 잡기

    - Goal: compare these algorithms. In report, want to see a graph of each algorithms for how much they take time to run.

    - 당연하지만, 패키지 쓰지 말것


* Shortest Path
1) Single Source Single Destination (SSSD) Problem
2) Single Source Multiple Destinatino (SSMD) Problem
3) Multiple Source Single Destination (MSSD) Problem
4) Multiple Source Multiple Destination (MSMD) Problem

(content)
- Dijkstra (with non-weights edge)
- Bellman-Ford (with negative weights edge)

    * Dijkstra Algorithm: SSMD (SSSD도 가능)
        1) Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
        2) Assign a distance value to every node.
            - 0 for the source node
            - infty for all other nodes
        3) For the current node, consider all of its unvisited neighbors and calculate their tentative distances through the current node.
            Compare the newly calculated distance to the current assigned value and assign the smaller one.
        4) When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited and remove it from the unvisited set.
        5) If we have reached the destination node, stop the algorithm.
        6) Otherwise, select the unvisited node that is marked with the smallest distance. Make it as the new "current node" and go back to step 3.

        ``` plaintext
        Dijkstra(G, source_node):
            create a set of all nodes Q (Unvisited set)

            for each vertex v in G:
                dist[v] = infty
                parent[v] = None
                add v to Q
            distance[source_node] = 0

            while Q is not empty:
                u = vertex in Q with min dist[u]
                remove u from Q

                for each neighbor v of u:
                    new_dist = dist[u] + length(u, v)
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        parent[v] = u

            return dist, parent
        ```

    * Bellman-Ford Algorithm
    - Slower than Dijkstra, but able to handle negative weights (음수 웨이트의 싸이클이 있으면, 다익스트라는 계속 무한으로 순환함)
        1) Initialize the distance to the source node as 0, and all other nodes as infty
        2) For all edges, if the distance to the destination node becomes shorter by taking another edge, update the distance with new lower value
        3) At iteration i, when we scan all edges, the algorithm finds all the shortest paths of length at most i edges ??
            The algorithm needs to scan all edges V-1 times to find the shortest path of length V-1 edges ??
            Than, the last scan will be performed and if any distance is updated in this scan, it means there is a negative cycle ??

        모든 엣지에 대한 리스트 만들어놓고 (고정된 엣지 순서 가지고), V-1번 돌면서 그때그때 최솟값을 갱신해나가는 방식 (한 반복동안 업데이트 없으면 V-1 전에 반복 종료)

        ``` plaintext
        Bellman-Ford(G, source_node):
            distance = []
            parent = []

            for each vertex v in G:
                distance[v] = infty
                parent[v] = None
            distance[source_node] = 0

            for i = 1 to V-1:
                for each edge (u, v) and weight w in G.E:
                    if distance[u] + w < distance[v]:
                        distance[v] = distance[u] + w
                        parent[v] = u

            for each edge (u, v) and weight w in G.E:
                if distance[u] + w < distance[v]:
                    Error "Graph contains Negative Cycle"

            return distance, parent
        ```






### References

$\tag*{}\label{n} \text{[n] }$
