class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        arr = []
        def inOrderTraverse(node, arr):
            if node is not None:
                inOrderTraverse(node.left, arr)
                arr.append(node.val)
                inOrderTraverse(node.right, arr)
        inOrderTraverse(root, arr)
        return len(arr)