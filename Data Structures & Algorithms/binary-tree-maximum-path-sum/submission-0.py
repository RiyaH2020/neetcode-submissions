# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max=float('-inf')
        def helper(root):
            if not root:
                return 0
            left=max(helper(root.left),0)
            right=max(helper(root.right),0)
            self.global_max=max(self.global_max,root.val+left+right)
            return max(root.val,root.val+max(left,right)) 
        helper(root)
        return self.global_max
        