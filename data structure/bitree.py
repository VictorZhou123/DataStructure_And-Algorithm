class BiNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

a = BiNode("A")
b = BiNode("B")
c = BiNode("C")
d = BiNode("D")
e = BiNode("E")
f = BiNode("F")
g = BiNode("G")


e.lchild = a
e.rchild = g
a.rchild = c
g.rchild = f
c.lchild = b
c.rchild = d

def pre_order(root):
    if root:
        print(root.data, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)

def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)

def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")

def leve_order(root):
    queue = []
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.data, end=",")
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)

leve_order(e)