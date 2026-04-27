# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.list1=[]
        def helper(root):
            if(not root):
                self.list1.append("N")
                return
            self.list1.append(str(root.val))
            helper(root.left)
            helper(root.right)
        helper(root)
        print(self.list1)
        return ",".join(self.list1)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals=data.split(",")
        self.i=0
        def dfs():
            if(vals[self.i]=="N"):
                self.i+=1
                return None
            node=TreeNode(int(vals[self.i]))
            self.i+=1
            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()
            

        