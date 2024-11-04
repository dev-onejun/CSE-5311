#!python

from algorithms import Graph
from algorithms import (
    prim_algorithm,
    kruskal_algorithm,
    kruskal_algorithm_with_path_compression,
)

from argparse import ArgumentParser
import time, random, pickle, os

import networkx as nx


def get_args():
    parser = ArgumentParser(description="Evaluate the performance of the algorithms")

    parser.add_argument(
        "--nodes",
        type=int,
        nargs="+",
        default=[10, 100, 1_000, 10_000, 100_000],
        help="Number of nodes in the graph",
    )
    parser.add_argument(
        "--edges",
        type=int,
        nargs="+",
        default=[20, 200, 2_000, 20_000, 200_000],
        help="Number of edges in the graph",
    )
    parser.add_argument(
        "--algorithm",
        type=str,
        nargs="+",
        default=["prim", "optimized_kruskal"],
        help="Algorithm to evaluate: prim, kruskal, optimized_kruskal",
    )
    parser.add_argument(
        "--generate",
        type=bool,
        default=False,
        help="If specified, generate the graph. Otherwise, use the pre-generated graph in the data folder",
    )

    return parser.parse_args()


def save_graph_to_file(graph: Graph):
    with open(
        f"data/graph_{len(graph.get_nodes())}_{len(graph.get_edges())}.pkl", "wb"
    ) as f:
        pickle.dump(graph, f)


def load_graph_from_file(path: str):
    with open(path, "rb") as f:
        graph = pickle.load(f)
    return graph


def generate_graph(num_nodes_list: list, num_edges_list: list):
    for num_nodes, num_edges in zip(num_nodes_list, num_edges_list):
        nodes = [str(i) for i in range(num_nodes)]
        edges = []

        random_graph = nx.gnm_random_graph(num_nodes, num_edges)
        while not nx.is_connected(random_graph):
            random_graph = nx.gnm_random_graph(num_nodes, num_edges)

        for u, v in random_graph.edges():
            weight = random.randint(1, 100)
            random_graph.edges[u, v]["weight"] = weight
            edges.append((str(u), str(v), weight))

        graph = Graph(nodes, edges)
        save_graph_to_file(graph)


def main():
    args = get_args()

    find_mst_algorithms = []
    if "prim" in args.algorithm:
        find_mst_algorithms.append(prim_algorithm)
    if "kruskal" in args.algorithm:
        find_mst_algorithms.append(kruskal_algorithm)
    if "optimized_kruskal" in args.algorithm:
        find_mst_algorithms.append(kruskal_algorithm_with_path_compression)

    if args.generate:
        num_nodes_list, num_edges_list = args.nodes, args.edges
        '''
        from math import comb
        num_edges_list = [comb(num_nodes, 2) for num_nodes in num_nodes_list]
        '''
        generate_graph(num_nodes_list, num_edges_list)
    else:
        graph_paths = os.listdir("data")
        graphs = [load_graph_from_file(f"data/{path}") for path in graph_paths]

        for graph in graphs:
            for find_mst in find_mst_algorithms:
                print(
                    f"Graph with {len(graph.get_nodes())} nodes and {len(graph.get_edges())} edges"
                )

                start_time = time.time()

                find_mst(graph)

                end_time = time.time()

                execution_time = end_time - start_time
                print(
                    f"\t Algorithm {find_mst.__name__} Execution time: {execution_time} seconds"
                )


if __name__ == "__main__":
    main()
