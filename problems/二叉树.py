class TreeNode():
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


class BinTree():
    def __init__(self):
        self.root = None
        self.ls = []

    def add(self, data):
        node = TreeNode(data)
        if self.root == None:
            self.root = node
            self.ls.append(self.root)
        else:
            rootnode = self.ls[0]
            if rootnode.left == None:
                rootnode.left = node
                self.ls.append(rootnode.left)
            elif rootnode.right == None:
                rootnode.right = node
                self.ls.append(rootnode.right)
                self.ls.pop(0)

    def preOrderTraversal(self,root):
        if root == None:
            return
        print(root.data)
        self.preOrderTraversal(root.left)
        self.preOrderTraversal(root.right)

    def inOrderTraversal(self,root):
        if root == None:
            return
        self.inOrderTraversal(root.left)
        print(root.data)
        self.inOrderTraversal(root.right)

    def postOrderTraversal(self,root):
        if root == None:
            return
        self.postOrderTraversal(root.left)
        self.postOrderTraversal(root.right)
        print(root.data)


if __name__ == '__main__':
    tree = BinTree()
    for i in range(1,11):
        tree.add(i)
    tree.preOrderTraversal(tree.root)
    tree.inOrderTraversal(tree.root)
    tree.postOrderTraversal(tree.root)