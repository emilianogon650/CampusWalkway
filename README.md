# CampusWalkway
Campus Graph Project — Analysis of Algorithms

Overview
This project models the Saint Mary's College campus as a weighted graph, where:

Nodes represent key campus locations (Library, Recreation Center, Soda Center, etc).
Edges represent the walkways between locations.
Each edge is weighted using a custom formula:
weight = number of steps + time in seconds / 2
​	
 
We use this graph to analyze and compute the most efficient routes across campus using well-known shortest path algorithms.

We used:
Python
NetworkX (graph creation and path algorithms)
Matplotlib (visualization)

Algorithms Implemented
We applied three shortest path algorithms to compare performance and results:

Dijkstra’s Algorithm: Finds the shortest path between two points using edge weights.
Bellman-Ford Algorithm: Computes shortest paths from a single source and supports negative weights (not used here but included for learning).
Floyd-Warshall Algorithm: Computes the shortest paths between all pairs of nodes.
Each algorithm was used to find the shortest path between the Recreation Center and the Credit Union Pavilion and then other locations as well.

Goals
Understand how to represent real-world locations as a graph.
Learn and implement shortest path algorithms.
Visualize the graph and paths using Python tools.
Practice working with weighted graphs and structured data.

Results
The shortest path outputs (using custom weight) were consistent across Dijkstra, Bellman-Ford, and Floyd-Warshall, validating the correctness of the graph and weight formula.
A visual graph of campus locations and path weights was also generated to enhance clarity.
