from collections import defaultdict, deque

def bfs(graph, start, target):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_node, path = queue.popleft()

        if current_node == target:
            return path

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

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

    path_start_to_target = bfs(graph, start_node, target_node)
    path_end_to_target = bfs(graph, ending_node, target_node)

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
