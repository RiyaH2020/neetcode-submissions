class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_visited=set()
        a_visited=set()
        p_queue=deque()
        a_queue=deque()
        rows=len(heights)
        cols=len(heights[0])
        for r in range(rows):
            if((r,0) not in p_visited):
                p_visited.add((r,0))
                p_queue.append((r,0))
            if((r,cols-1) not in a_visited):
                a_visited.add((r,cols-1))
                a_queue.append((r,cols-1))
        for c in range(cols):
            if((0,c) not in p_visited):
                p_visited.add((0,c))
                p_queue.append((0,c))
            if((rows-1,c) not in a_visited):
                a_visited.add((rows-1,c))
                a_queue.append((rows-1,c))
        
        while(p_queue):
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for i in range(len(p_queue)):
                row,col=p_queue.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if(r>=0 and c>=0 and r<rows and c<cols and (r,c) not in p_visited and heights[r][c]>=heights[row][col]):
                        p_visited.add((r,c))
                        p_queue.append((r,c))
        while(a_queue):
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            for i in range(len(a_queue)):
                row,col=a_queue.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if(r>=0 and c>=0 and r<rows and c<cols and (r,c) not in a_visited and heights[r][c]>=heights[row][col]):
                        a_visited.add((r,c))
                        a_queue.append((r,c))
        return list((a_visited)& (p_visited))
            
        
