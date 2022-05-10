
HOW TO USE THIS TOOL:

- This tool is used to find reoccurring motifs in graphs.
- EX1Q1 will output all motifs (connected sub-graphs) of size n, 
  where n is a user input. Since isomorphic sub-graphs for our purposes
  are the same, we exclude isomorphic subgraphs.
- EX1Q2 will output all motifs (connected sub-graphs) of size n, 
  but this time a user input graph is also considered, and in addition 
  we check for each of the motifs how many times it appears in the graph.
- The "netwrokx" library was used to check:
  1) If a given graph is connected. Disconnected motifs are of no 
     interest for us.
  2) If a given graph is isomorphic to a graph which was considered 
     earlier. If so, disregard this graph.
- All user input demands are specified when running the code.