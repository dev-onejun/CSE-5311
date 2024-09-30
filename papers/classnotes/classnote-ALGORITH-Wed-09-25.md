$$
\begin{array}{|c|c|}
\hline
\text{} & \text{} \\
\hline
\text{} & \text{} \\
\hline
\end{array}
$$

##### Graph Theory

- set of $(V, E)$
$$
V = {a, b, c, d, e}
e = {ab, bd, ac, cd, de}
$$

- Vertex - using array
- Edges - using 2d array
- Adjacency - 2 vertices are adjcent if there is an edge connecting them
- Path - set of edges between vertices

Operations on Graphs
1. Add a vertex
2. add an edge
3. display vertex

* Depth First Traversal
rule 1: visit the adjacent unvisited neighbor. Mark it as visited, print it, and push it on a stack. # note that it is In-order? traversal
rule 2: If no adjcent vertex is found, pop up a vertex from the stack.
rule 3: repeat rule 1 and 2 until the stack is empty.

``` plaintext
DFS_iterative(G, s):
    let S be a stack
    S.push(s)
    mark s as visited
    while S is not empty:
        v = S.pop()
        for all neighbors w of v:
            if w is not visited:
                s.push(w)
                mark w as visited

DFS_recursive(G, s):
    mark s as visited
    for all neighbors w of s:
        if w is not visited:
            DFS_recursive(G, w)
```

* Breadth First Traversal (Use Queue)
rule 1: visit the adjacent unvisited neighbor. Mark it as visited, print it, and push it on a queue.
rule 2: If no adjcent neighbor is found, remove the first vertex from the queue.
rule 3: repeat rule 1 and 2 until the queue is empty.

``` plaintext
BFS(G, s):
    let Q be a queue
    Q.enqueue(s)
    mark s as visited
    while Q is not empty:
        v = Q.dequeue()
        for all neighbors w of v:
            if w is not visited:
                Q.enqueue(w)
                mark w as visited
```

* Non Directed Graph: Edges are not directed
* Directed Graph: Edges has a direction
* Simple Graph: No self loops, no multiple edges between 2 same vertices
    - maximum number of edges in a simple graph is $n(n-1)/2$ ($n C_2$)
    - valid simple graph with $n$ vertices is $2^{n(n-1)/2}$ (2: either edge or no edge, $n(n-1)/2$: the number of edges)

* Degree of a vertex: number of vertices which are adjacent
    - In $n$ nodes, $0 \leq \text{degree} \leq n-1$
    - In a directed graph
        - In-degree: number of edges coming into a vertex
        - Out-degree: number of edges going out of a vertex

* Adjacency
- 2 vertices are adjacent if there is an edge connecting them
- 2 edges are adjacent if they point to the same vertex

* Distance between 2 vertices: number of edges in the shortest path between vertex $U$ and $V$. $d(U, V)$

* Eccentricity of a vertex: the maximum distance between a vertex and all other vertices in the graph. $e(v) = \max(d(v, u))$

* when $G(V, E)$ is a graph, $\sum_i deg(v_i) = 2|E|$

* BFS in graph can be applied to finding the shortest path, Minimum Spanning Tree (MST) of unweighted graph, GPS navigation, Detecting cycle in undirected graph, find all nodes within one connected components, etc.
    - Coplexity of BFS is $O(V+E)$
* DFS in graph can be applied to detect cycle, find topological sorting, test if a graph is bipartite, find connected compaonents, etc.
    - Complexity of DFS is $O(V+E)$

* Representation of a graph
    With
    - Adjacency Matrix
    - Adjacency List

    - Adjacency matrix: matrix A[v][v]
    if there is an edge $v_x$ and $v_y$ $\to$ $\begin{cases} A[V_x][V_y] = 1 \\ A[V_y][V_x] = 1 \end{cases}$

    In undirected graph

||a|b|c|d|
|---|---|---|---|---|
|a|0|1|1|0|
|b|1|0|1|0|
|c|1|1|0|1|
|d|0|0|1|0|

    In directed graph

||a|b|c|d|
|---|---|---|---|---|
|a|0|1|1|0|
|b|0|0|1|0|
|c|0|0|0|1|
|d|0|0|0|0|

    - Adjacency List: array of A[v] of linked lists
        an entry A[v] represents the linked list of vertices adjcent v_x

        with the same graph above, the adjacency list is

        a -> b -> c
        b -> a -> c
        c -> a -> b -> d
        d -> c

* Connected Graph: there is a path between every pair of vertices
  Disconnected Graph: there is no path between at least 2 vertices
  - DFS or BFS can be used to determine if a graph is connected or not

* Complete Graph: graph with n mutual vertices. all vertices are connected to each other

* Cycle Graph: a simple graph with n>=3 vertices and n edges, forming a cycle. (삼각형, 사가형, ...)
  Acyclic Graph: a graph with no cycle

* Bipartite Graph: a graph $G(V, E)$ is bipartite if $V$ can be partitioned into 2 sets $V_1$ and $V_2$ such that every edge connects a vertex in $V_1$ to a vertex in $V_2$
  - DFS or BFS can be used to determine if a graph is bipartite or not
  - 혼자 있는 노드는 둘 중 아무 set에 넣어도 된다. 이 경우에도 bipartite graph이다.
  Complete Bipartite Graph: every vertex in $V_1$ is connected to every vertex in $V_2$ and vice versa

* Complement Graph: a graph $G(V, E)$ is a complement of $G'(V, E')$ if $E \cap E' = \emptyset$ and $E \cup E' = V \times V$. In other words, when G is a simple graph, G- is complement graph if it includes all possible edges that are not in G.
  - $|E(G)| + |E(G')| = |E(K_n)| = n(n-1)/2$

  - Example. Let G is a simple graph with 9 vertices and 12 edges. Find n of edges in complement graph.
    - $\frac{9 \times 8}{2} = 36$, $36 - 12 = 24$
  - Example. Let G is a simple graph with 40 edges and G' is a complement graph with 38 edges. Find n of vertices in G.
    - $40 + 38 = 78 = \frac{n(n-1)}{2} \to n = 13$

* Tree: a connected acyclic graph
- $n$ nodes, $n-1$ edges
- if 1 mor edge is added preserving a definition of a simple graph, it becomes a cycle

    * Spaning Tree: a subgraph of a graph $G(V, E)$ that includes all vertices of $G$ and is a tree (n-1 edges)
    - 5 Properties
        ...?

    - Applications: civil network planning, computer network routing protocol, cluster analysis, etc.

    * Minimum Spanning Tree (MST): with a weighted graph, MST is a spanning tree with the smallest sum of edge weights

* Cut Vertex: when a graph G is connected, a vertex v is a cut vertex if removing v and all edges incident to v results in a disconnected graph
Example with 8 nodes

``` plaintext
    a - b - c - d
    |   |   |   |
    e - f   g - h
```
b,c are a cut vertex

  Cut Edge: when a graph G is connected, an edge e is a cut edge if removing e results in a disconnected graph

  - Whenever cut edge exists, cut vertex exists
  - if cut vertex exists, a cut edge may or may not exist

  Cut Set: a subset of edges whose removal disconnects the graph
  Example with 5 nodes

  ``` plaintext
      a - b - c
      |   |
      d - e
  ```
  {the edge between b and c}, {the edge between a and b, the edge between b and e} and so on are cut sets

  Practice. Suppose that a group of 5 people A, B, C, D, and E. The following pairs of people are qquainted with each other: A-C, A-D, B-C, C-D, C-E.
    a) Draw a graph to represent the relationship
    b) List the vertex set and edge set
    c) Draw an adjacency matrix to represent G

||A|B|C|D|E|
|---|---|---|---|---|---|
|A|0|0|1|1|0|
|B|0|0|1|0|0|
|C|1|1|0|1|1|
|D|1|0|1|0|0|
|E|0|0|1|0|0|

  Practice. Given a graph with no cycles. we want to consider it as a tree and assign a root node such that the tree has the maximum height. How can we do this?
    - Find the longest path and make either the end nodes as the root node






### References

$\tag*{}\label{n} \text{[n] }$
