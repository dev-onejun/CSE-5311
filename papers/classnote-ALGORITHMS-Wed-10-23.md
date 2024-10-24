$$
\begin{array}{|c|c|}
\hline
\text{} & \text{} \\
\hline
\text{} & \text{} \\
\hline
\end{array}
$$

* Network Flow Algorithm
    - Networks: send as many packets as possible
    - Transportation: send as many truck as possible

    * Given $G(V, E)$, each edge is associated with a value (capacity). The start node is referred as source node, and the destination node is referred as sink node. The goal is to maximize the total amount of flow from source to sink.
        Conditions:
        - flow on edges should not exceed C(e)
        - for every node (except S, T), incoming flow = outgoing flow
        - if we consider any path, the capacity of the edge which has minimum capacity ???
        - flow for any edge is $0 \leq flow(e) \leq C(e)$

    이 문제를 푸는 2개의 알고리즘이 있다.

    * Ford-Fulkerson's Algorithm
        - Do not need to maintain the amount of flow on each edge. work with the capacity.
        - if f -> amount of flow u -> v, capacity(uv) = f (= amount leftfor that edge) ?????

        ``` plaintext
        Function Ford-Fulkerson(Graph G, S, T)
            initialize amount of flow = 0

            while there exists an augmenting path from S to T in residual graph:
                augment flow between S and T along that path
                update residual graph

            return
        ```
    * Dinic's Algorithm
        - level graph: a graph such that the value of each node is its shortest distance from the source node.
        - blocking flow: includes finding new path from the bottleneck node ??

        ``` plaintext
        function Dinics(graph G, S, T):
            initialize flow for all edges = 0
            F = 0
            Construct level graph

            while there exists an augmenting path in the level graph:
                find blocking flow $f$
                F = F + f
                update level graph

            return F
        ```

* Algorithm Design
- When it comes to designing, the goal is usually set between two of the folliwing:
    1. Most optimal solution OR
    2. A solution that is good enough

    * Brute Force: the simplest to implement and hardest to run
    * Divide and conquer: ex. Binary Search, Merge Sort, Heap Sort, Quick Sort, Depth First Traversal
        - break a problem into a smaller sub problems
        - Recursively solve sub problems.
        - Combine the results into a solution for the original problem.
    * Greedy Algorithm: ex. Prim's, Kruskal's, Dijkstra's
        - a set of partial solutions from which a solution is built
        - an objective function which assigns a value to any partial solution
        - Given a partial solution,
            - consider possible extentions of partial solution
            - discard ones which are not feasible
            - choose those which minimizes the objective function

* Process Scheduling
    - There are two perspectives regarding process scheduling
    1. Multiprogramming view
        - run processes in a sequence (1-2-3-4)
    2. preemptive multitasking/time sharing
        - allow processes to run for a short period of time and switch to another process (1-2-4-3-1-2)

    ex. we want to minimze the total wait time for processes to be completed.

$$
\begin{array}{|c|c|}
\hline
\text{Process i} & \text{time (ms)} \\
\hline
1 & 15 \\
2 & 8 \\
3 & 3 \\
4 & 10
\hline
\end{array}
$$

    - FCFS (First Come First Serve)
        - 15 + 23 + 26 + 36 = 100
    - SJF (Shortest Job First)
        - 3 + 11 + 19 + 29 = 71

        * 증명
        Let i1, i2, i3, i4 , ...
        waiting time = 4 (i1) + 3(i2_ + 2(i3) + 1(i4) 로 정리할 수 있고, 때문에 짧은 프로세스부터 시작하는 것이 효율적임을 증명할 수 있다






























### References

$\tag*{}\label{n} \text{[n] }$
