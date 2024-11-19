class Solution:
    def minDepth(self, root) -> int:
        def dfs(root):
            if not root:
                return 0
            if not root.left:
                return 1 + dfs(root.right)
            elif not root.right:
                return 1 + dfs(root.left)
            return 1 + min(dfs(root.left), dfs(root.right))
        return dfs(root)