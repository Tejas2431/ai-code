from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            if vertex == goal:
                print("\nGoal found:", goal)
                return
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    
    print("\nGoal not found.")

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = input("Enter the goal node: ")

print("BFS Traversal:")
bfs(graph, start_node, goal_node)
