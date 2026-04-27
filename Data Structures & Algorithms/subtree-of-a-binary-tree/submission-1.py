# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root,subRoot):
            if(root==None and subRoot==None):
                return True
            if(not root or not subRoot):
                return False
            if(root.val==subRoot.val):
                left=isSameTree(root.left,subRoot.left)
                right=isSameTree(root.right,subRoot.right)
                if(left==True and right==True):
                    return True
                else:
                    return False
            else:
                return False
        if(not subRoot):
            return True
        if(not root):
            return False
        if(isSameTree(root,subRoot)):
            return True
        else:
            left=self.isSubtree(root.left,subRoot)
            right=self.isSubtree(root.right,subRoot)
            if(left==True or right==True):
                return True
            else:
                return False
            