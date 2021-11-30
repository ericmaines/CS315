# PA 3 - CS315 Fall 2021
# Erin Maines - e@uky.edu
# 912273694
# 15 November 2021

import sys
import pdb
import queue
import heapq as heap

def initialize_dict(file_name):
    dict = {}
    with open(file_name, 'r') as vertices:
        for line in vertices:
            dict[line[0:-1]] = {
                                'edges': [],
                                'color': [],
                                'pi': [],
                                'd': []
                                }
    return dict

def parse_dict(vertices_file, edges_file):
    cities = initialize_dict(vertices_file)
    with open(edges_file, 'r') as edges:
        for line in edges:
            split_line = line.split(',')

            # structure will now be [City1, City2, weight\n]
            # will represent as {City1: (City2, weight), ...}

            city_and_weight_1 = (split_line[1], split_line[2][0:-1]) #trim off the \n character
            city_and_weight_2 = (split_line[0], split_line[2][0:-1]) #trim off the \n character

            cities[split_line[0]]['edges'].append(city_and_weight_1)
            cities[split_line[1]]['edges'].append(city_and_weight_2) 
            # Access both during the loop so we don't have to iterate again
    return cities

def run_bfs(adj_dict):
    graph = bfs(adj_dict, "Arad")
    print("Arad to Sibiu: ")
    print_path(graph, "Arad", "Sibiu")
    print("\nArad to Craiova:")
    print_path(graph, "Arad", "Craiova")
    print("\nArad to Bucharest:")
    print_path(graph, "Arad", "Bucharest")
    return None

def bfs(graph, search):
    for u in graph.keys():
        graph[u]["color"] = "white"
        graph[u]["d"] = float('inf')
        graph[u]["pi"] = None

    graph[search]["color"] = "gray"
    graph[search]["d"] = 0
    graph[search]["pi"] = None
    que = queue.Queue()
    que.put(search)
    while not (que.empty()):
        u = que.get()
        for e in graph[u]['edges']:
            v = e[0] #select just the name out of the tuple 
            if graph[v]["color"] == "white":
                graph[v]["color"] = "gray"
                graph[v]["d"] = graph[u]["d"] + 1
                graph[v]["pi"] = u
                que.put(v)
        graph[u]["color"] = "black"
    return graph


def print_path(graph, source, dest):
    if dest == source:
        print(source)
    elif graph[dest]["pi"] == None:
        print("No path between those nodes exists")
    else: 
        print_path(graph, source, graph[dest]["pi"])
        print(dest)
        
def run_dijkstras(graph):
    graph = dijkstras(graph, "Arad")
    print("\nDijkstra's: Arad to Bucharest")
    print_path(graph, "Arad", "Bucharest")
    return None

def dijkstras(graph, source):
    graph = initialize_single_source(graph, source)
    known_vertices = queue.PriorityQueue()
    for vertex in graph.keys():
        for edge in graph[vertex]["edges"]:
            known_vertices.put((int(edge[1]), edge[0]))
    while not known_vertices.empty():
        queue_weight, queue_source = known_vertices.get()
        for vertex in graph[queue_source]["edges"]:
            graph = relax(graph, queue_source, vertex[0], vertex[1])
    return graph


def initialize_single_source(graph, source):
    for vertex in graph.keys():
        graph[vertex]["d"] = float('inf')
        graph[vertex]["pi"] = None
    graph[source]["d"] = 0
    return graph

def relax(graph, source, dest, weight):
    combined_weight = graph[source]["d"] + int(weight)
    if graph[dest]["d"] > combined_weight:
        graph[dest]["d"] = combined_weight
        graph[dest]["pi"] = source
    return graph

def run_prims(graph):
    prims(graph, "Arad")
    

def prims(graph, start):
    for vertex in graph.keys():
        graph[vertex]["d"] = float('inf')
        graph[vertex]["pi"] = None
    graph[start]["d"] = 0
    known_vertices = queue.PriorityQueue()
    for vertex in graph.keys():
        for edge in graph[vertex]["edges"]:
            known_vertices.put((int(edge[1]), edge[0]))
    while not known_vertices.empty():
        queue_weight, queue_edge = known_vertices.get()
        for vertex in graph[queue_edge]['edges']:
            breakpoint()
            if graph[vertex[0]]["d"] == float('inf') and int(vertex[1]) > int(queue_weight):
                graph[vertex[0]]["pi"] = queue_edge
                graph[vertex[0]]["d"] =  queue_weight

def print_graph(graph):
    for vertex in graph.keys():
        print(vertex, "->", graph[vertex]["edges"])

def main():
    if sys.argv[1] and sys.argv[2]:
        vertices = sys.argv[1]
        edges = sys.argv[2]
        parsed_dict = parse_dict(vertices, edges)
        print_graph(parsed_dict)
        run_bfs(parsed_dict)
        run_dijkstras(parsed_dict)
        #run_prims(parsed_dict)

if __name__ == "__main__":
    main()
