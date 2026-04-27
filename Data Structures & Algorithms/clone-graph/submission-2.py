"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew={}
        def bfs(node):
            queue=deque()
            queue.append(node)
            copy=Node(node.val)
            oldToNew[node]=copy
            while(queue):
                n=queue.popleft()
                for t in n.neighbors:
                    if(t not in oldToNew):
                        queue.append(t)
                        oldToNew[t]=Node(t.val)
                    oldToNew[n].neighbors.append(oldToNew[t])
            return oldToNew[node]
        return bfs(node) if node else None

                        
