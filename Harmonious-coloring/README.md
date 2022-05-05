# Harmonious-coloring
The scope of this project is to determine the harmonious chromatic number of a graph.

The project contains:

1. Two input files for the program: harmoniuos.in and harmoniuos_adj.in

2. A sorce file for a program in C/C++:  harmonious_number.cpp

The program can take as input a graph given in file harmonious.in by the list of its edges or a lists of graphs with the same number of vertices given by adjacent lists, given in file harmoniuos_adj.in. These input files have the following structure:

harmonious.in: on  first line the number of vertices are given, then each of the next lines contain two numbers representing the extremities of an edge

harmonious_adj.in: on  first line the number of vertices  and the number of graphs are given, then the adjacent list for each graph in the following format (see 3_regular_graph_8_vertices for an example):

- first a line "Graph x" where x is the number/name of the graph 

- then each line has structure i  v1 v2 ... where the first number is the current vertex and next numbers are its neighbours


3. Three input file samples: 3_regular_graph_8_vertices.in, 3_regular_graph_10_vertices.in and 3_regular_graph_12_vertices.in containing the adjacent lists of all 3-regular graphs with 8, 10 and 12 vertices, respectively.

4. The output files with harmonious chromatic number of 3-regular graphs: 3_regular_graph_8_vertices.out, 3_regular_graph_10_vertices.out and 3_regular_graph_12_vertices.out

5. One input file sample with interesintg 3-regular graphs with more than 12 vertices 3_regular_graph_other.in and the output files with harmonious chromatic number of these graphs 3_regular_graph_other.out 



