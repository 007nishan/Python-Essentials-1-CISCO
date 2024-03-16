"""
file_name = input()

with open(file_name, 'r') as file:
    text = file.read()
sentences = text.split('.')
sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

average_length = sum(len(sentence.split()) for sentence in sentences) / len(sentences)
print(average_length)
"""
"""
import networkx as nx
import random
import matplotlib.pyplot as plt

G = nx.Graph()

for node in range(1,6):
    G.add_node(node)

for _ in range(10):
    node1, node2 = random.sample(range(1,6),2)
    G.add_edge(node1, node2)

print(G.nodes())
print(G.edges())

nx.draw(G, with_labels=True)
plt.show()
"""
"""
import networkx as nx
import random
import matplotlib.pyplot as plt
#parameters
num_points = 10000
radius = 1.0
#Function to check if a point is inside the quarter circle
def is_point_inside_circle(x, y, radius):
    return x**2 + y**2 <= radius**2 and x >=0 and y >= 0
#Monte Carlo simulation for area estimation of a quarter circle
def estimate_area_quarter_circle(num_points, radius):
    inside_points = 0
    for _ in range(num_points):
        x = random.uniform(0, radius)
        y = random.uniform(0, radius)
        if is_point_inside_circle(x, y, radius):
            inside_points += 1
    area_ratio = inside_points/num_points
    estimated_area = area_ratio * (radius**2)
    return estimated_area

estimate_area_quarter_circle(10000, 1.0)
print(estimate_area_quarter_circle(10000, 1.0))

plt.show()

"""

import networkx as nx
import random
import matplotlib.pyplot as plt

G = nx.Graph()

for node in range(1,6):
    G.add_node(node)

while(len(G.edges())!=10):
    node1, node2 = random.sample(range(1,6),2)
    G.add_edge(node1, node2)

print(G.nodes())
print(G.edges())
plt.show()  #this will show the graph