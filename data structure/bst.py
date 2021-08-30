class BiTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.lchild = None
        self.rchild = None

class BST:
    def __init__(self) -> None:
        self.root = None