from collections import defaultdict

def dfs(graph, current, target, visited):
    if current == target:
        return [current]

    visited.add(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, target, visited)
            if path:
                return [current] + path

    return []

def main():
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))
    
    graph = defaultdict(list)

    for _ in range(num_edges):
        src, dest = input("Enter edge (source destination): ").split()
        graph[src].append(dest)
        graph[dest].append(src)

    start_node = input("Enter the starting node: ")
    ending_node = input("Enter the ending node: ")
    target_node = input("Enter the target node: ")

    visited = set()
    path_start_to_target = dfs(graph, start_node, target_node, visited)
    visited = set()
    path_end_to_target = dfs(graph, ending_node, target_node, visited)

    if path_start_to_target:
        print("Path from", start_node, "to", target_node, ":", path_start_to_target)
        print("Target node is present.")
    elif path_end_to_target:
        print("Path from", ending_node, "to", target_node, ":", path_end_to_target)
        print("Target node is present.")
    else:
        print("No node present.")

if _name_ == "_main_":
    main()
