# Stack


def dfs_iterative(graph, v_start):
    visited = []
    stack = [v_start]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited
