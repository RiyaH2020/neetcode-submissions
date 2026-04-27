class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=set()
        queue=deque()
        rows=len(grid)
        fresh=0
        cols=len(grid[0])
        def makeRotten(r,c):
            if(r>=rows or c>=cols or r<0 or c<0 or (r,c) in visited or grid[r][c]!=1):
                return
            grid[r][c]=2
            queue.append((r,c))
            visited.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==2 and (r,c) not in visited):
                    queue.append((r,c))
                    visited.add((r,c))
                elif(grid[r][c]==1):
                    fresh+=1
        if(fresh==0):
            return 0
        time=0
        while(queue):
            for i in range(len(queue)):
                (r,c)=queue.popleft()
                makeRotten(r+1,c)
                makeRotten(r,c+1)
                makeRotten(r,c-1)
                makeRotten(r-1,c)
            time+=1
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c]==1):
                    return -1
        return time-1



