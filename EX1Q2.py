import numpy as np
from scipy.sparse.csgraph import laplacian
import networkx as nx
import networkx.algorithms.isomorphism as iso
import itertools


# A function which outputs the grpah to the txt file iff this graph is connected and an isomorphic graph wasnt
# added yet:
def print_graph(graph):
    global string
    global count
    global graphs_array
    global all_connected_subgraphs
    motif_appearances = 0
    # Checking if the graph is connected:
    if nx.is_connected(nx.DiGraph(graph).to_undirected()):
        # check isomorphism. if there is already an isomorphic graph to this one, return:
        for prev_graph in graphs_array:
            if nx.is_isomorphic(nx.DiGraph(graph), nx.DiGraph(prev_graph)):
                return
        count += 1
        print(count)  # print out just to indicate where we are standing
        graphs_array.append(graph.copy())
        string += "#" + str(count) + "\n"
        for connected_subgraph in all_connected_subgraphs:
            if nx.is_isomorphic(nx.DiGraph(graph), connected_subgraph):
                motif_appearances += 1
        string += "count=" + str(motif_appearances) + "\n"
        for row in range(len(graph)):
            for col in range(len(graph)):
                if graph[row, col] == 1:
                    string += str(row+1) + " " + str(col+1) + "\n"


# A recursive function which creates all possible directed graphs of size n*n
def recurse_graph_fill(graph, index):
    if index == graph.size:
        print_graph(graph)
        return
    row = int(index / len(graph))
    col = int(index % len(graph))
    graph[row, col] = 0
    recurse_graph_fill(graph, index + 1)
    if row == col:  # there will be no edge between a vertex and itself
        return
    graph[row, col] = 1
    recurse_graph_fill(graph, index + 1)


if __name__ == '__main__':
    count = 0  # number of subgraphs
    n = int(input("enter n (size of motifs):"))  # input here size of motifs
    edges_list = []
    edge = [-1, -1]
    max_vertex = 0
    while True:
        edge = input("insert new edge (from x to y). to finish enter 0,0:")
        edge = list(int(x) for x in edge.split())
        if edge == [0, 0]:
            break
        if edge[0] == edge[1] or edge[0] < 1 or edge[1] < 1:
            print("invalid input. enter again:")
            continue
        max_vertex = max([max_vertex, max(edge)])
        edges_list.append(edge)
        # create edges here
    graph = np.zeros((max_vertex, max_vertex))
    for edge in edges_list:
        graph[edge[0]-1, edge[1]-1] = 1

    G = nx.DiGraph(graph)
    all_connected_subgraphs = []

    # here we ask for all connected subgraphs of size n from the graph we just created:
    for SG in (G.subgraph(selected_nodes) for selected_nodes in itertools.combinations(G, n)):
        if nx.is_connected(SG.to_undirected()):
            all_connected_subgraphs.append(SG)

    graphs_array = []
    string = ""
    graph = np.zeros((n, n))
    f = open("EX1Q2.txt", "w+")
    if graph.size != 1:
        recurse_graph_fill(graph, 0)
    f.write("n=" + str(n) + "\n")
    f.write("count=" + str(count) + "\n")
    f.write(string)
    f.close()

