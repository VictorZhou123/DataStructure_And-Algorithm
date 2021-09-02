from bst import BiTreeNode, BST

class AVLNode(BiTreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.bf = 0   # bf:balance factor

class AVLTree(BST):
    def __init__(self, interable):
        super().__init__(interable)

    def rotate_left(self, p, c):  # p是父节点，c是子节点
        '''''
        左旋
        '''''
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        p.parent = c
        c.lchild = p

        p.bf, c.bf = 0, 0

        return c

    def rotate_right(self, p, c):  # p是父节点，c是子节点
        '''''
        右旋
        '''''
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c

        p.bf, c.bf = 0, 0

        return c

    def rotate_right_left(self, p, c):
        g = c.lchild
        gbf = g.bf
        self.rotate_right(c, g) # 右旋
        self.rotate_left(p, g)  # 左旋

        # 对于旧的bf进行判断，推导出新的bf
        # 在经过左旋和右旋之后，三个点的bf都归零了
        if gbf < 0:
            p.bf = -1
        elif gbf > 0:
            c.bf = 1
        else: # gbf=0时，即插入的是g节点
            pass
        return g

    def rotate_left_right(self, p, c):
        g = c.lchild
        gbf = g.bf
        self.rotate_left(p, g)  # 左旋
        self.rotate_right(c, g) # 右旋

        # 对于旧的bf进行判断，推导出新的bf
        # 在经过左旋和右旋之后，三个点的bf都归零了
        if gbf > 0:
            p.bf = -1
        elif gbf < 0:
            c.bf = 1
        else: # gbf=0时，即插入的是g节点
            pass
        return g

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if not p.lchild:
                    node = AVLNode(val)
                    p.lchild = node
                    node.parent = p
                    break
                else:
                    p = p.lchild
            elif val > p.data:
                if not p.rchild:
                    node = AVLNode(val)
                    p.rchild = node
                    node.parent = p
                    break
                else:
                    p = p.rchild
            else:
                return

        # 更新整个二叉树的bf值，并且进行旋转
        while node.parent: # 保证插入节点node的父节点不为空
            if node.parent.lchild is node: # 如果node是其父节点的左树根节点
                if node.parent.bf > 0:
                    node.parent.bf = 0
                    break
                elif node.parent.bf < 0: # node.parent.bf == -1, 更新后会变成-2
                    g = node.parent.parent # 为了连接旋转后的子树
                    x = node.parent        # 旋转前子树的根
                    if node.bf < 0: # node左重右轻=>右旋
                        n = self.rotate_right(node.parent, node) # 旋转后的树的根节点为n
                    else: # node右重左轻 or node左右一样重 => 左旋再右旋
                        n = self.rotate_left_right(node.parent, node)
                else: # node.parent.bf == 0，更新后变成-1，无需进行旋转操作
                    node.parent.bf = -1
                    node = node.parent
                    continue
            elif node.parent.rchild is node: # 如果node是其父节点的右树根节点
                if node.parent.bf < 0: #父节点左重右轻
                    node.parent.bf = 0
                    break
                elif node.parent.bf > 0:
                    if node.bf > 0: # node右重左轻=>左旋
                        self.rotate_left(node.parent, node)
                    else: # node左重右轻 or node左右一样重 => 先右旋再左旋
                        self.rotate_right_left(node.parent, node)
                else:
                    node.parent.bf = 1
                    node = node.parent
                    continue
        
            # 链接旋转后的子树
            n.parent = g
            if not g:
                self.root = n
                break
            else:
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break

if __name__ == "__main__":
    tree = AVLTree([9,8,7,6,5,4,3,2,1])

    tree.pre_order(tree.root)
    print("")
    tree.in_order(tree.root)