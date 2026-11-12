from collections import deque

graph = {
    "A":  ["L", "I1"],
    "L":  ["A", "P", "I2", "I1"],
    "I1": ["A", "L", "O"],
    "P":  ["L", "I2"],
    "I2": ["L", "P", "O"],
    "O":  ["I1", "I2"],
}


def label(v):
    return v[0]


def bfs(start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        v = queue.popleft()
        order.append(label(v))
        for n in graph[v]:
            if n not in visited:
                visited.add(n)
                queue.append(n)
    return order


def dfs(v, visited=None, order=None):
    if visited is None:
        visited, order = set(), []
    visited.add(v)
    order.append(label(v))
    for n in graph[v]:
        if n not in visited:
            dfs(n, visited, order)
    return order


if __name__ == "__main__":
    print("BFS:", " - ".join(bfs("A")))
    print("DFS:", " - ".join(dfs("A")))