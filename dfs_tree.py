class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node, result):
    if node:
        result.append(node.data)
        preorder(node.left, result)
        preorder(node.right, result)


def inorder(node, result):
    if node:
        inorder(node.left, result)
        result.append(node.data)
        inorder(node.right, result)


def postorder(node, result):
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.data)


root = Node("J")
root.left = Node("A")
root.right = Node("M")
root.left.left = Node("E")
root.left.right = Node("S")
root.right.left = Node("A")
root.right.right = Node("L")
root.left.left.left = Node("I")
root.left.left.right = Node("P")
root.left.right.left = Node("I")
root.left.right.right = Node("O")

for name, func in [("Preorder", preorder), ("Inorder", inorder), ("Postorder", postorder)]:
    out = []
    func(root, out)
    print(f"{name}: {' -> '.join(out)}")