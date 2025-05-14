# Analysis of Algorithms Final Project: Campus Walkway Graph
import networkx as nx
import matplotlib.pyplot as plt

# This is our Data: Each walkway from locations includes the steps and time in seconds
walkways = [
    {"from": "Credit Union Pavilion", "to": "Soda Center", "steps": 93, "time": 310},
    {"from": "Soda Center", "to": "Bookstore", "steps": 66, "time": 228},
    {"from": "Bookstore", "to": "Cafe Louis", "steps": 19, "time": 37},
    {"from": "Cafe Louis", "to": "Oliver Hall", "steps": 37, "time": 102},
    {"from": "Oliver Hall", "to": "Chapel", "steps": 15, "time": 32},
    {"from": "Cafe Louis", "to": "Library", "steps": 55, "time": 143},
    {"from": "Library", "to": "Recreation Center", "steps": 73, "time": 237},
    {"from": "Credit Union Pavilion", "to": "Brosseau Hall", "steps": 62, "time": 205},
    {"from": "Brosseau Hall", "to": "Galileo Hall", "steps": 24, "time": 45},
    {"from": "Galileo Hall", "to": "Sichel Hall", "steps": 25, "time": 49},
    {"from": "Oliver Hall", "to": "Dante Hall", "steps": 26, "time": 48},
    {"from": "Dante Hall", "to": "Garaventa Hall", "steps": 22, "time": 42},
    {"from": "Sichel Hall", "to": "Garaventa Hall", "steps": 77, "time": 245},
    {"from": "Brosseau Hall", "to": "Galileo Hall", "steps": 43, "time": 119},
    {"from": "Chapel", "to": "Galileo Hall", "steps": 47, "time": 128},
    {"from": "Chapel", "to": "Dante Hall", "steps": 48, "time": 132},
    {"from": "Library", "to": "Dante Hall", "steps": 22, "time": 40},
    {"from": "Garaventa Hall", "to": "Recreation Center", "steps": 45, "time": 125},
    {"from": "Chapel", "to": "Brosseau Hall", "steps": 34, "time": 93},
    {"from": "Dante Hall", "to": "Galileo Hall", "steps": 57, "time": 158},
]

G = nx.Graph()

for walkway in walkways:
    node1 = walkway["from"]
    node2 = walkway["to"]
    steps = walkway["steps"]
    time = walkway["time"]
    weight = (steps + time) / 2
    G.add_edge(node1, node2, weight=weight)

print("Campus Walkways and Weights:")
for u, v, data in G.edges(data=True):
    print(f"{u} <--> {v} : weight = {data['weight']}")

# Dijkstra's algorithm example
shortest_path = nx.dijkstra_path(G, source="Recreation Center", target="Chapel", weight="weight")
print("\nDijkstra's Shortest path from Recreation Center to Chapel:")
print(" -> ".join(shortest_path))

# Bellman-Ford algorithm example
bellman_ford_path = nx.bellman_ford_path(G, source="Recreation Center", target="Chapel", weight="weight")
bellman_ford_length = nx.bellman_ford_path_length(G, source="Recreation Center", target="Chapel", weight="weight")
print("\nBellman-Ford path from Recreation Center to Chapel:")
print(" -> ".join(bellman_ford_path))
print(f"Total weight: {bellman_ford_length:.2f}")

# Floyd-Warshall example
fw_distances = nx.floyd_warshall(G, weight="weight")
fw_distance = fw_distances["Recreation Center"]["Chapel"]
print("\nFloyd-Warshall distance from Recreation Center to Chapel:")
print(f"Total weight: {fw_distance:.2f}")

# User input for shortest path
print("\nType two locations on campus to find the fastest walkway route between them.")
print("Options:", list(G.nodes))
user_source = input("Enter starting location: ")
user_target = input("Enter destination location: ")

if user_source in G.nodes and user_target in G.nodes:
    try:
        user_path = nx.dijkstra_path(G, source=user_source, target=user_target, weight="weight")
        total_weight = nx.dijkstra_path_length(G, source=user_source, target=user_target, weight="weight")
        print(f"\nFastest route from {user_source} to {user_target}:")
        print(" -> ".join(user_path))
        print(f"Total path weight (avg. of steps and time): {total_weight:.2f}")
    except nx.NetworkXNoPath:
        print(f"No path exists between {user_source} and {user_target}.")
else:
    print("One or both locations are not valid campus locations.")

# Visualization
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, "weight")
rounded_labels = {k: f"{v:.1f}" for k, v in edge_labels.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=rounded_labels, font_size=8)
plt.title("Saint Mary's College Campus Graph", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.show()
