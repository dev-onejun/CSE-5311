# Programming Assignment 1

**Wonjun Park** \
Computer Science \
University of Texas at Arlington \
Arlington, TX, USA

### OVERVIEW

![System Architecture](../papers/assets/Programming-Assignment-1-System-Design.svg)

``` plaintext
.
├── INSTRUCTION.md
├── README.md
├── algorithms
│   ├── __init__.py
│   ├── __main__.py
│   ├── disjointset.py
│   ├── graph.py
│   ├── kruskal.py
│   └── prim.py
├── data
├── demo
│   ├── css
│   ├── app.py
│   ├── index.html
│   └── pyscript.toml
├── evaluation.py
├── requirements-dev.txt
├── requirements-test.txt
├── tests
    ├── __init__.py
    └── test_algorithms.py
```

+ algorithms: The manually implemented module for the Minimum Spanning Tree algorithms
+ tests: The test cases for the algorithms
+ demo: The directory for the demo

- evaluation.py: The script for the algorithm evaluation
- requirements-dev.txt: packages used while developing the project
- requirements-test.txt: packages required for running the test cases

### INSTALLATION

[![Programming Assignment 1 Pytest](https://github.com/dev-onejun/CSE-5311/actions/workflows/pytest.yml/badge.svg?branch=feat%2Fp1)](https://github.com/dev-onejun/CSE-5311/actions/workflows/pytest.yml)

The project passed the test cases run on Python 3.11, 3.12, and 3.13 versions. Any other versions are not guaranteed to work.

Although the core algorithms do not require any external packages, to evaluate the algorithms, you need to install a `networkx` package for generating a random graph.

You can simply install the required packages and run the evaluation script by running the following command:

``` bash
$ pip install -r requirements-test.txt
$ python evaluation.py --algorithm prim kruskal optimized_kruskal
```

The script will run the evaluation with the data stored in the `data` directory.

In addition, if you want to run several test cases concurrently, you can run the following command:

``` bash
# Ensure that you install `parallel` package on your system. (ex. apt install parallel)
$ parallel -j 6 python evaluation.py --algorithm {1} ::: prim kruskal optimized_kruskal
```

The result will show the comparison between the Kruskal, Prim, and Optimized Kruskal algorithms in terms of the number of input sizes and the time complexity.

### DATA GENERATION

In order to generate the random graph data, you can run the following command:

``` bash
$ python evaluation.py --nodes 10 20 30 --edges 20 40 60 --generate
```

The above command will generate random graphs (num_nodes, num_edges) as (10, 20), (20, 40), and (30, 60) and store them in the `data` directory.

You can download the pre-generated data from the [link](https://1drv.ms/u/s!Ak9f7WgKWrGQi7ZC733bgsMzqhZUCA?e=tJGwba).

### DEMO

[LINK](https://dev-onejun.github.io/CSE-5311/programming_assignment/demo)

### REPORT

[PDF](https://dev-onejun.github.io/CSE-5311/papers/programming_assignment_1.pdf), [HTML](https://dev-onejun.github.io/CSE-5311/papers/programming_assignment_1.html)
