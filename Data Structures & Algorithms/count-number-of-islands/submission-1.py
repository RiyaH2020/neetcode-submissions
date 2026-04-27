class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        visit=set()
        rows=len(grid)
        cols=len(grid[0])

        def bfs(row,col):
            queue=deque()
            directions=[[-1,0],[1,0],[0,-1],[0,1]]
            queue.append((row,col))
            visit.add((row,col))
            while queue:
                row,col=queue.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if(r<rows and c<cols and r>=0 and c>=0):
                        if(grid[r][c]=="1" and (r,c) not in visit):
                            visit.add((r,c))
                            queue.append((r,c))



        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]=="1" and (r,c) not in visit):
                    bfs(r,c)
                    islands+=1
        return islands