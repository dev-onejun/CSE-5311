$$
\begin{array}{|c|c|}
\hline
\text{} & \text{} \\
\hline
\text{} & \text{} \\
\hline
\end{array}
$$

* Topological Sort
    - Given Directed Acyclic Graph, find an ordering of vertices such that for every edge $(u, v)$, $u$ comes before $v$ in the ordering.

    ex. somebody is getting ready to go out, () must wear the following: shirt, briefs, pants, socks, shoes, ...
            (pants should go on after briefs, socks are put on beffore shoes)
        - .


* Critical Path Method (CPM)
- project modeling technique used to plan and manage complex projects.

    ex. Suppose given a project with a set of tasks, each task is associated with a performance time. We want to know how much time required for performing compelete tasks serially.

    - Critical time: the minimum time required to complete the project (when some tasks (that are possible) are performed in parallel)
        - A task which are no prerequisite tasks: critical time = performance time
        - A task which requires prerequisites: critical time = performance time of the task + maximum critical time of prerequisites

        -> * Conditions:
                - we must know execution time of each task
                - we need to record critical time for each task
                - we need to know previous task with the longest critical time

    - Critical Path: 각 노드의 (최종) critical time에 영향을 미치는 것들을 이은 path


* NP-Completeness (Nondeterministic Polynomial)
    - Tractable problems: solvable in polynomial time. any problems bound by $n^k$ for some constant $k$.
    - Intractable problems: solvable in super-polynomial time.
        ex. enumerate all binary strings of length $n$. Find powerset (set of all sets) of a set with $n$ elements.
            - Finding the longest simple path in a graph
            - optimal way to schedule tasks on a factory machine under scheduling and deadline constraints ?
            - determining whether boolean formulas can be satisfied simultaneously
            - the cheapest way to visit all of cities without repeating any city and returning to the starting city
    - Unsolvable Problems: no algorithms can be given guaranteed to solve all instances of the problem.
        ex. halting problem: given a descriptino of a program and an input, determine when the program will halt.
            ``` pseudo code
            while True: continue
            ```


...


* Clique: a subset of
    * how to find the edge that splits the graph into two parts? (NP-Complete)
        - find the complement of the given graph
        - return True if complement graph is bipartite (complement에서 한 group에 속한 노드들끼리는 원래 그래프에서 clique가 되기 때문)


* Vertex Cover: for undirected graph is a subset of vertices such that for every edge $(u, v)$, either $u$ or $v$ is in vertex cover.
    * how to find the edge that splits the graph into two parts? (NP-Complete)
        - find the complement of the given graph
        - return True if complement graph is bipartite (complement에서 한 group에 속한 노드들끼리는 원래 그래프에서 vertex cover가 되기 때문)
















### References

$\tag*{}\label{n} \text{[n] }$
