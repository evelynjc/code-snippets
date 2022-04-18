# preferred in coding tests
# graph = { 1: [2,3], ... }
def dfs_recursive(graph, v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = dfs_recursive(graph, w, visited)
    return visited
