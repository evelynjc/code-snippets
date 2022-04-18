# BFS: iterative only (queue)
# graph =
from collections import deque


def bfs(graph, v_start):
    visited = [v_start]
    queue = deque([v_start])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited
