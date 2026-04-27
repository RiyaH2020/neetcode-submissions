class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=set()
        queue=deque()
        rows=len(grid)
        cols=len(grid[0])
        directions=[[-1,0],[1,0],[0,1],[0,-1]]
        count=0
        def dfs(r,c):
            if(r>=rows or c>=cols or r<0 or c<0 or (r,c) in visited):
                return
            if(grid[r][c]=="0"):
                return
            visited.add((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    dfs(r,c)
                    count+=1
        return count

            

