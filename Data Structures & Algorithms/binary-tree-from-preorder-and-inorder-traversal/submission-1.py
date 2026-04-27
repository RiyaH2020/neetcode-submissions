# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map={val: i for i,val in enumerate(inorder)}
        self.pre_index=0
    
        def helper(l,r):
            if(l>r):
                return None
            root=TreeNode(preorder[self.pre_index])
            self.pre_index+=1
            mid=in_map[root.val]
            root.left=helper(l,mid-1)
            root.right=helper(mid+1,r)
            return root
        return helper(0,len(inorder)-1)