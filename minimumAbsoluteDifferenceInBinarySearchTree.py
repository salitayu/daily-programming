class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            l.append(node.val)
            if node.right:
                dfs(node.right)
            dfs(root)
            return min(b - a for a, b in zip(l, l[1:]))