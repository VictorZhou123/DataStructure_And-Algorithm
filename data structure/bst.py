class BiTreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None

class BST:
    def __init__(self, interable) -> None:
        self.root = None
        if interable:
            for val in interable:
                self.insert_no_rec(val)
    
    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if not p.lchild:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
                else:
                    p = p.lchild
            elif val > p.data:
                if not p.rchild:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
                else:
                    p = p.rchild
    
    def query(self, node, val):
        if not node:
            return None
        elif val < node.data:
            return self.query(node.lchild, val)
        elif val > node.data:
            return self.query(node.rchild, val)
        elif val == node.data:
            print(node.data)
            return node.data
    
    def query_no_rec(self, val):
        p = self.root
        while p:
            if val < p.data:
                p = p.lchild
            elif val > p.data:
                p = p.rchild
            elif val == p.data:
                return p
        return None

    def __remove_node_1(self, node):
        # 情况一，node是叶子节点
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
        elif node == node.parent.rchild:
            node.parent.rchild = None

    def __remove_node_21(self, node):
        # 情况二一，node只有一个左孩子节点
        if not node.parent:
            self.root = node.lchild
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent            

    def __remove_node_22(self, node):
        # 情况二二，node只有一个右孩子节点
        if not node.parent:
            self.root = node.rchild
        # node是它父节点的右孩子
        elif node == node.parent.rchild:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent
        # node是它父节点的左孩子
        else:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent            


    def delete(self, val):
        if self.root: # 不是空树
            node = self.query_no_rec(val)
            if not node: # 要找的节点不存在
                return False
            # 情况一：这个节点没有孩子节点
            if not (node.lchild or node.rchild): 
                self.__remove_node_1(node)

            # 情况三：这个节点有两个孩子节点
            elif node.lchild and node.rchild:
                min_node = node.rchild
                # 找到这个节点的右孩子的最下层左孩子
                while min_node.lchild:
                    if min_node.lchild:
                        min_node = min_node.lchild
                # 将最下层左孩子的值赋给node
                node.data = min_node.data
                # 删除最下层左孩子
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

            # 情况二：这个节点只有一个孩子节点
            else:
                if node.lchild:
                    self.__remove_node_21(node)
                else:
                    self.__remove_node_22(node)


            
    def pre_order(self, root):
        '''''
        前序遍历
        '''''
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    def in_order(self, root):
        '''''
        中序遍历
        '''''
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

if __name__ == "__main__":
    tree = BST([4,6,7,9,2,1,3,5,8])
    tree.in_order(tree.root)
    tree.delete(9)
    print("")
    tree.in_order(tree.root)
