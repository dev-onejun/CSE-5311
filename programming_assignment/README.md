# Programming Assignment 1

**Wonjun Park** \
Computer Science \
University of Texas at Arlington \
Arlington, TX, USA

### OVERVIEW

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
├── demo
│   ├── css
│   ├── html
│   ├── scripts
│   └── index.html
├── evaluation.py
├── requirements-dev.txt
├── requirements-test.txt
├── tests
    ├── __init__.py
    └── test_algorithms.py
```

+ algorithms: The module for the Minimum Spanning Tree algorithms
+ tests: The test cases for the algorithms
+ demo: The directory for the demo

- evaluation.py: The script for the algorithm evaluation

### INSTALLATION

[![Programming Assignment 1 Pytest](https://github.com/dev-onejun/CSE-5311/actions/workflows/pytest.yml/badge.svg?branch=feat%2Fp1)](https://github.com/dev-onejun/CSE-5311/actions/workflows/pytest.yml)

The project passed the test cases run on Python 3.11, 3.12, and 3.13 versions. Any other versions are not guaranteed to work.

Although the core algorithms do not require any external packages, to evaluate the algorithms, you need to install a `networkx` package for generating a random graph.

You can simply install the required packages and run the evaluation script by running the following command:

``` bash
$ pip install -r requirements-test.txt
$ python evaluation.py
```

The result will show the comparison between the Kruskal, Prim, and Optimized Kruskal algorithms in terms of the number of input sizes and the time complexity.

### DEMO

[LINK](https://dev-onejun.github.io/CSE-5311/demo/programming_assignment_1/demo/index.html)



### REPORT

[PDF](https://dev-onejun.github.io/CSE-5311/papers/programming_assignment_1.pdf), [HTML](https://dev-onejun.github.io/CSE-5311/papers/programming_assignment_1.html)
