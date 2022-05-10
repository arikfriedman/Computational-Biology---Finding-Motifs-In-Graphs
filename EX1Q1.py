import numpy as np
from scipy.sparse.csgraph import laplacian
import networkx as nx
import networkx.algorithms.isomorphism as iso


# A function which outputs the grpah to the txt file iff this graph is connected and an isomorphic graph wasnt
# added yet:
def print_graph(graph):
    global string
    global count
    global graphs_array
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
    n = int(input("enter n:"))  # input here number of vertices in the graph
    count = 0  # number of subgraphs
    graphs_array = []
    string = ""
    graph = np.zeros((n, n))
    f = open("EX1Q1.txt", "w+")
    if graph.size != 1:
        recurse_graph_fill(graph, 0)
    f.write("n=" + str(n) + "\n")
    f.write("count=" + str(count) + "\n")
    f.write(string)
    f.close()

