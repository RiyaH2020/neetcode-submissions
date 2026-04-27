class Solution:
            def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
                rows,cols=len(grid),len(grid[0])
                visited=set()
                directions=[(-1,0),(1,0),(0,1),(0,-1)]
                max_area=0
                queue=deque()
                for r in range(rows):
                    for c in range(cols):
                        if grid[r][c]==1 and (r,c) not in visited:
                            area=0
                            queue.append((r,c))
                            visited.add((r,c))
                            while queue:
                                cr,cc=queue.popleft()
                                area+=1
                                for dr,dc in directions:
                                    nr,nc=cr+dr,cc+dc
                                    if(0<=nr<rows and 0<=nc<cols and
                                    grid[nr][nc]==1 and (nr,nc) not in visited):
                                        queue.append((nr,nc))
                                        visited.add((nr,nc))
                            max_area=max(area,max_area)
                return max_area


