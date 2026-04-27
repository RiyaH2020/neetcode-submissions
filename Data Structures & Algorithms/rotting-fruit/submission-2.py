class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        queue=deque()
        visited=set()
        time=0
        fresh=0
        directions=[[-1,0],[0,1],[1,0],[0,-1]]

        def bfs():
            nonlocal fresh
            nonlocal time
            while(queue):
                new_rotten=0
                for _ in range(len(queue)):
                    row,col=queue.popleft()
                    for dr,dc in directions:
                        r=row+dr
                        c=col+dc
                        if(0<=r<rows and 0<=c<cols and (r,c) not in visited and grid[r][c]==1):
                            visited.add((r,c))
                            queue.append((r,c))
                            grid[r][c]=2
                            fresh-=1
                            new_rotten+=1
                if(new_rotten>0):
                    time+=1
               

                






        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==2 and (r,c) not in visited):
                    visited.add((r,c))
                    queue.append((r,c))
                elif(grid[r][c]==1):
                    fresh+=1
        bfs()

        return time if fresh==0 else -1