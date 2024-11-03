$$
\begin{array}{c}
\hline
\\
\begin{align*}
& \large{\mathbf{\text{Programming Assignment 1:}}} \\
& \large{\mathbf{\text{An Implementation of Finding Minimum Spanning Tree From Scratch Using Python}}} \\
\end{align*}
\\
\\
\hline
\\
\mathbf{\text{Wonjun Park}} \\
\text{Computer Science} \\
\text{University of Texas at Arlington} \\
\text{Arlington, TX, USA} \\
\text{wxp7177@mavs.uta.edu}
\end{array}
$$

***Abstract*** \
Among 4 types of given candidate projects, this project implemented project 4, Minimum Spanning Tree algorithms. The key part of the implementation which belongs to the `programming_asignment/algorithms` module only used Python without any packages and libraries. The project included Kruskal and Prim algorithms, the well-known algorithms for finding the minimum spanning tree from a given graph. Although the initial implementation of Kruskal algorithm succeeded to find the minimum spanning tree, the paper introduced the optimized method for the algorithm.

$\cdots$ The optimized method increased the efficiency of the algorithm by reducing the number of iterations. $\cdots$
As a result, the paper compared the two algorithms and showed the optimized Kruskal algorithm outperformed the Prim algorithm in terms of the number of iterations and the time complexity.

<!--
**Acronym & Abbreviation**
- MST: Minimum Spanning Tree
- GUI: Graphical User Interface
    -->

### I. INTRODUCTION

$\quad$ As a emergence of Internet, Information Technology, a new market, expanded rapidly, connecting people and companies around the world as well as providing a lot of wealth. Computer Network, the basic idea of the Internet, became a core part of Computer Science. A data structure, graph, has been used to represent the network, and the Minimum Spanning Tree (MST) is one of intetersting topics in the graph theory. The MST is a subgraph of a given graph that connects all vertices without any cycles and has the minimum total edge weight.

$\quad$ Prim and Kruskal algorithms are two fundamental methods to find the MST in a connected, weighted, and undirected graph [[1](#mjx-eqn-1)].

### II. DESIGN

#### A. Algorithm

$\quad$ Following the project instruction, the project did not utilize any packages and libraries for the main algorithms. Besides the development of the basic Kruskal and Prim algorithms, the project showed the optimized Kruskal algorithm.

**Kruskal Algorithm** $\quad$

**Prim Algorithm** $\quad$

**Optimized Kruskal Algorithm** $\quad$

#### B. Test

$\quad$ All implemented algorithms were tested on MacOS 15.1 and Ubuntu 22.04 with several Python versions (3.11, 3.12, 3.13). The test ran on both local computers and GitHub Actions.

$\quad$ The pytest [[2](#mjx-eqn-2)] framework is a testing framework used in many projects.

$\quad$ While Pytest enabled the test automation, the networkx library was used to generate a random graph and to check the correctness of the implemented algorithms by comparing the results with the networkx's MST.

#### C. Graphic User Interface

$\quad$ Web applications have benefits of cross-platform, easy deployment, and cost-effective for both developers and users. Normally, HTML, CSS, and JavaScript are the components of the web client application. However, the project used Python to implement the Graphical User Interface (GUI) to run designed algorithms and to visualize the results. Specifically, PyScript [[3](#mjx-eqn-3)] ran the Python code on the web browser as well as matplotlib [[4](#mjx-eqn-4)] visualized the results.

![System Design](./assets/Programming-Assignment-1-System-Design.svg)
$\text{Fig. 1. System Architecture}$

### III. IMPLEMENTATION

All codes are in the `programming_assignment` repository,

#### A. Numeric Results

$\quad$ .

However, it is hard to randomly create that a graph is connected since the number of edges increases exponentially as the number of vertices increases. Specifically, the probability that a graph is connected becomes lower as the number of nodes grows.

evaluation.py

#### B. Demo

... The link to the demo is in the *APPENDIX* section.

### IV. CONCLUSION

$\quad$ The paper reviewed the project which implemented Kruskal and Prim algorithms for finding the Minimum Spanning Tree from a given graph as well as its GUI interface for the detailed demonstration. The project also adopted a disjoint set data structure to use path compression to optimize the Kruskal algorithm.

The optimized Kruskal algorithm outperformed

All algorithms were compared in terms of the number of input sizes and the time complexity, resulting in ... the best.

### REFERENCES

$$\tag*{}\label{1} \text{[1] Debmalya Panigrahi, COMPSCI 330: Design and Analysis of Algorithms, "Minimum Spanning Tree", Mar. 1st, 2016, }\\ \text{https://courses.cs.duke.edu/spring18/compsci330/Notes/mst.pdf, accessed in Nov. 2th, 2024}$$
$$\tag*{}\label{2} \text{[2] pytest, "pytest: helps you write better programs", https://docs.pytest.org/en/stable/, accessed in Nov. 2th, 2024}$$
$$\tag*{}\label{3} \text{[3] PyScript, "<py>", https://pyscript.net, accessed in Nov. 2th, 2024}$$
$$\tag*{}\label{4} \text{[4] matplotlib, "Matplotlib: Visualization with Python", https://matplotlib.org, accessed in Nov. 2th, 2024}$$

### APPENDIX

* Report - [pdf](https://dev-onejun.github.io/CSE-5311/papers/programming_assignment_1.pdf), [html](https://dev-onejun.github.io/CSE-5311/papers/programming_assignment_1.html)
* Demo - [html]()
