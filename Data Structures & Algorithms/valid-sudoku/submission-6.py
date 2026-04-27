class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=len(board)
        cols=len(board[0])
        for r in range(rows):
            row_set=set()
            for c in range(cols):
                if(board[r][c]!="."):
                    if board[r][c] in row_set:
                        return False
                    row_set.add(board[r][c])
        for c in range(cols):
            col_set=set()
            for r in range(rows):
                if(board[r][c]!="."):
                    if board[r][c] in col_set:
                        return False
                    col_set.add(board[r][c])
        
        for r in range(0,rows,3):
            for c in range(0,cols,3):
                block_set=set()
                for i in range(3):
                    for j in range(3):
                        if(board[r+i][c+j]!="."):
                            if(board[r+i][c+j] in block_set):
                                return False
                            block_set.add(board[r+i][c+j])
        return True
