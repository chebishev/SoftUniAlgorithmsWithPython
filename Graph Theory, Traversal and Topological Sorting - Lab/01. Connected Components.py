nodes = int(input())
graph = [[int(x) for x in input().split()] for _ in range(nodes)]
visited = [False] * nodes


def dfs(node, graph, visited, component):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited, component)
    component.append(node)


for node in range(nodes):
    if visited[node]:
        continue

    component = []
    dfs(node, graph, visited, component)
    print(f"Connected component: {' '.join([str(x) for x in component])}")

# test inputs:

# 9
# 3 6
# 3 4 5 6
# 8
# 0 1 5
# 1 6
# 1 3
# 0 1 4
#
# 2

# 0
