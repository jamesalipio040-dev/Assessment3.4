from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree():
    root = Node("A")
    root.left = Node("L")
    root.right = Node("I")
    root.left.left = Node("P")
    root.left.right = Node("I")
    root.right.left = Node("O")
    return root


def bfs(root):
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def dfs(node, result=None):
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.value)
    dfs(node.left, result)
    dfs(node.right, result)
    return result


if __name__ == "__main__":
    tree = build_tree()
    print("BFS:", " - ".join(bfs(tree)))
    print("DFS:", " - ".join(dfs(tree)))