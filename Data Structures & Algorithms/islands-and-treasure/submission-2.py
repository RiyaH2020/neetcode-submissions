class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        queue=deque()
        def addele(r,c):
            if(r>=rows or c>=cols or r<0 or c<0 or (r,c) in visited or grid[r][c]==-1):
                return
            visited.add((r,c))
            queue.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==0 and (r,c) not in visited):
                    queue.append((r,c))
                    visited.add((r,c))
        dist=0
        while(queue):
            for i in range(len(queue)):
                r,c=queue.popleft()
                grid[r][c]=dist
                addele(r+1,c)
                addele(r,c+1)
                addele(r-1,c)
                addele(r,c-1)
            dist+=1
        
