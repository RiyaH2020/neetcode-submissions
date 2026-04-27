class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands=0
        visit=set()
        rows=len(grid)
        cols=len(grid[0])
        maxArea=0
        def bfs(row,col):
            queue=deque()
            visit.add((row,col))
            queue.append((row,col))
            directions=[[1,0],[-1,0],[0,-1],[0,1]]
            area=0
            while(queue):
                row,col=queue.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if(r>=0 and c>=0 and r<rows and c<cols):
                        if(grid[r][c]==1 and (r,c) not in visit):
                            area+=1
                            queue.append((r,c))
                            visit.add((r,c))
            return area

        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==1 and (r,c) not in visit):
                    islands+=1
                    area=1+bfs(r,c)
                    maxArea=max(area,maxArea)
        return maxArea