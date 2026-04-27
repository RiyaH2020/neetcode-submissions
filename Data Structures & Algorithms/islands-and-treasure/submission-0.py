class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited=set()
        rows=len(grid)
        cols=len(grid[0])

        def helper(row,col):
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            visited.add((row,col))
            queue=deque()
            queue.append((row,col,0))
            while(queue):
                row,col,dist=queue.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if(r>=0 and c>=0 and r<rows and c<cols):
                        if(grid[r][c]!=-1 and (r,c) not in visited):
                            visited.add((r,c))
                            grid[r][c]=min(grid[r][c],dist+1)
                            queue.append((r,c,1+dist))
        for r in range(rows):
            for c in range(cols):
                if((r,c) not in visited and grid[r][c]==0):
                    visited.add((r,c))
                    helper(r,c)
                    visited=set()




                    

