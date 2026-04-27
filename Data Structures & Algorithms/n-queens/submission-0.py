class Solution:
    def isSafe(self,row, col,board):
            r=row-1
            while r>=0:
                if(board[r][col]=="Q"):
                    return False
                r-=1
            r,c=row-1,col-1
            while(r>=0 and c>=0):
                if(board[r][c]=="Q"):
                    return False
                r-=1
                c-=1
            r,c=row-1,col+1
            while(r>=0 and c<len(board)):
                if board[r][c]=="Q":
                    return False
                r-=1
                c+=1
            return True
    def solveNQueens(self, n: int) -> List[List[str]]:

        res=[]
        board=[["."]*n for _ in range(n)]
    

        def helper(row):
            if(row==n):
                copy=["".join(row) for row in board]
                res.append(copy)
                return
            for col in range(n):
                if self.isSafe(row,col,board):
                    board[row][col]="Q"
                    helper(row+1)
                    board[row][col]="."
        helper(0)
        return res
        