class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertBST(root,data):
    if not root:
        return TreeNode(data=data)
    if data < root.data:
        root.left = insertBST(root.left,data)
    elif data > root.data:
        root.right = insertBST(root.right,data)
    return root

root = TreeNode(4)
insertBST(root,7)
insertBST(root,2)
insertBST(root,1)
insertBST(root,3)