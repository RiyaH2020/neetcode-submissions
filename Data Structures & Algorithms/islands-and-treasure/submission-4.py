class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        queue=deque()
        directions=[(1,0),(0,1),(0,-1),(-1,0)]
        def bfs():
            while(queue):
                row,col=queue.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if(0<=r<rows and 0<=c<cols and (r,c) not in visited and grid[r][c]!=-1):
                        grid[r][c]=grid[row][col]+1
                        visited.add((r,c))
                        queue.append((r,c))





        for row in range(rows):
            for col in range(cols):
                if(grid[row][col]==0 and (row,col) not in visited):
                    visited.add((row,col))
                    queue.append((row,col))
        bfs()

