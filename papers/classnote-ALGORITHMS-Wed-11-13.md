$$
\begin{array}{|c|c|}
\hline
\text{} & \text{} \\
\hline
\text{} & \text{} \\
\hline
\end{array}
$$

* Maximum Independent Set PROBLEM
    - independent set: no two vertices are adjacent, no edges connecting any pair of vertices in the set

        ``` mermaid
        graph LR
            A --- B
            B --- C
            C --- D
            D --- A
        ```

        - Independent Set: {A, C}

        ``` mermaid
        graph LR
            A --- B
            B --- C
            C --- D
            D --- E
            E --- F
            F --- A
        ```

        - Independent Set: {A, C, E}

        ``` mermaid
        graph LR
            A --- B
            B --- H
            H --- G
            G --- A
            A --- C
            D --- B
            F --- H
            G --- E
            C --- D
            D --- F
            F --- E
            E --- C
        ```

        - Independent Set: {A, D, E, H}

    - an independent set of the largest possible size for a given graph is called a maximum independent set
        - Example algorithm: examine every vertex subset and check whether it is an independent set between there find largest size (brute force)
        - approximation algorithm:
            ?

* Hamiltonian Cycle
    - Hamiltonian path: a path that visits each vertex exactly once in undirected graph

        ``` mermaid
        graph LR
            0 --- 1
            1 --- 2
            2 --- 4
            4 --- 3
            3 --- 0
            1 --- 3
            1 --- 4
        ```
    - Hamiltonian path: {0, 1, 2, 4, 3}

    - Hamiltonian cycle: a Hamiltonian path + if there is an edge connecting the last vertext to the 1st vertex

    - Naive Approach: examine every possible permutation of vertices and check whether it is a Hamiltonian cycle
        - time complexity: $O(n!)$
        $$
        \begin{array}{l}
        \text{while there are untried permutations:} \\
        \qquad \text{generate the next permutation} \\
        \qquad \text{if the permutation is a Hamiltonian cycle and there is an edge from the last vertex to the first vertex:} \\
        \qquad \qquad \text{return the cycle} \\
        \end{array}
        $$

* Backtracking Algorithm

$$
\begin{array}{l}
\text{Create an empty path array and add vertex 0 to it.} \\
\text{Starting from vertex 1, try to add all vertices to the path array, checking if there is an edge ,,,,} \\
\end{array}
$$

* Traveling Salesman Problem
    - Given a set of cities and the distance between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the origin city
    - NP-hard problem
    - Assume that we know that hamiltonian cycles exist, and want to find the minimum weight hamiltonian cycle

    - naive algorithm:
$$
\begin{array}{rl}
\text{1} & \text{Let 1 be the starting and ending point for the TSP problem.} \\
\text{2} & \text{Generate all (n-1)! permutations of cities.} \\
\text{3} & \text{Calculate the cost of every permutation and keep track of the minimum cost permutation.} \\
\text{4} & \text{Return the permutation with the minimum cost.} \\
\end{array}
$$

    - Approximation using MST:
        (the graph should be triangle inequality which is the least distance to reach any vertex $j$ from vertex $i$ is the direct edge between $i$ and $j$ rather than through the other vertex $k$)
            - $a \lt b + c$
            - $b \lt a + c$
            - $c \lt a + b$
        the approximation will return a path that is at most twice the optimal path

$$
\begin{array}{rl}
\text{1} & \text{Let 1 be the starting and ending point for the TSP problem.} \\
\text{2} & \text{Construct MST with vertex 1 as the root using Prim's algorithm.} \\
\text{3} & \text{List all vertices visited in preorder traversal of MST. This is the approximate solution.} \\
\end{array}
$$

        - To prove that the approximation algorithm is at most twice the optimal path,
            * Full walk: list all vertices when they are first visited in preorder, it also visits vertices when they are returned after a subtree is visited
            - 이거 때문에 triangle inequality 를 만족해야 함
            - triangle inequality를 만족하는 지 여부는 approximation 적용 전에 모든 엣지에 대해 조사(확인)해야 함

        - Characteristics
            - The cost of the best possible TSP tour is never less than the cost of MST
            - the cost of full walk is at most twice the cost of MST
            - The output of the approximation algorithm is less than the cost of the full walk

* Set Cover
    - Given a universe of elements $U = \{ \cdots \}$, a collection of subsets of $U$, $S = \{S_1, S_2, \cdots, \}$, where every subset has an associated cost, the problem is to find the smallest subset of $S$ that covers all elements in $U$
    Example
        - $U = \{1, 2, 3, 4, 5\}$, $S = \{ S_1, S_2, S_3 \}$, $S_1 = \{4, 1, 3\}$, $S_2 = \{2, 5\}$, $S_3 = \{1, 4, 3, 2 \}$
        - Cost($S_1$) = 5, Cost($S_2$) = 10, Cost($S_3$) = 3

        - $S_3$, $S_2$ $\to$ cost = 13
        - $S_1$, $S_2$ $\to$ cost = 15
        $\to$ $S_3, S_2$ is the smallest subset that covers all elements in $U$

        - Approximation Greedy algorithm:
        $$
        \begin{array}{l}
        \text{Let } U \text{is the universe of elements }, S \text{is the collection of subsets, and } C \text{is the cost of each subset.} \\
        \text{Let } I \text{be the set of elements included in the cover so far, initially empty.} \\
        \text{Do the following while } I \text{is not same as } U: \\
        \qquad \text{Find the subset } S_i \text{ whose cost ratio } \frac{C_i}{|S_i - I|} \text{ is minimum.} \\
        \qquad \text{Add } S_i \text{ to } I.
        \end{array}
        $$














### References

$\tag*{}\label{n} \text{[n] }$
