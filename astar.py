from queue import PriorityQueue

def astar(grid, start, end):
    h = lambda a, b: abs(a[0]-b[0]) + abs(a[1]-b[1])
    q = PriorityQueue()
    q.put((0, start))
    came = {start: None}
    cost = {start: 0}

    while not q.empty():
        _, cur = q.get()
        if cur == end:
            path = []
            while cur:
                path.append(cur)
                cur = came[cur]
            return path[::-1]

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = cur[0]+dx, cur[1]+dy
            nxt = (nx, ny)
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==0:
                new_cost = cost[cur]+1
                if nxt not in cost or new_cost < cost[nxt]:
                    cost[nxt] = new_cost
                    q.put((new_cost + h(nxt, end), nxt))
                    came[nxt] = cur
    return None

# Example
grid = [
  [0,1,0,0],
  [0,1,0,1],
  [0,0,0,0],
  [1,1,0,0]
]
start = (0,0)
end = (3,3)

print("Path:", astar(grid, start, end))
