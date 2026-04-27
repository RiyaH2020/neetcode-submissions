class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited=set()
        queue=deque()
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        rows=len(board)
        cols=len(board[0])
        for r in range(rows):
            if(board[r][0]=="O" and (r,0) not in visited):
                queue.append((r,0))
                visited.add((r,0))
            if(board[r][cols-1]=="O" and (r,cols-1) not in visited):
                queue.append((r,cols-1))
                visited.add((r,cols-1))
        for c in range(cols):
            if(board[0][c]=="O" and (0,c) not in visited):
                queue.append((0,c))
                visited.add((0,c))
            if(board[rows-1][c]=="O" and (rows-1,c) not in visited):
                queue.append((rows-1,c))
                visited.add((rows-1,c))
        while(queue):
            for i in range(len(queue)):
                row,col=queue.popleft()
                for dr,dc in directions:
                    r=row+dr
                    c=col+dc
                    if(r>=0 and c>=0 and r<rows and c<cols and (r,c) not in visited and board[r][c]=="O"):
                        visited.add((r,c))
                        queue.append((r,c))
        for r in range(rows):
            for c in range(cols):
                if((r,c) not in visited):
                    board[r][c]="X"