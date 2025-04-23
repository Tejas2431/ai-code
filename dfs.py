def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # Process the node

    if start == goal:
        print(f"Goal node '{goal}' found!")
        return True  # Found the goal

    for neighbor in graph[start]:
        if neighbor not in visited:
            found = dfs(graph, neighbor, goal, visited)
            if found:
                return True  # Goal found in recursion

    return False  # Goal not found

# Example graph (undirected)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Take goal node from user
goal_node = input("Enter the goal node: ").strip().upper()

# Run DFS
if not dfs(graph, 'A', goal_node):
    print(f"Goal node '{goal_node}' not found in the graph.")
