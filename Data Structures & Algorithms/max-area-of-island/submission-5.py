class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        queue=deque()
        maxArea=0
        visited=set()

        def bfs(row,col):
            area=1
            queue.append((row,col))
            while (queue):
                row,col=queue.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if(0<=r<rows and 0<=c<cols and grid[r][c]==1 and (r,c) not in visited):
                        queue.append((r,c))
                        area+=1
                        visited.add((r,c))
            return area
        
        for row in range(rows):
            for col in range(cols):
                if(grid[row][col]==1 and (row,col) not in visited):
                    visited.add((row,col))
                    area=bfs(row,col)
                    maxArea=max(area,maxArea)
        return maxArea