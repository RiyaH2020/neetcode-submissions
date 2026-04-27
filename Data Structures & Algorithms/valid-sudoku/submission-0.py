class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            col_list=[]
            for j in range(9):
                if(board[i][j]!="."):
                    col_list.append(board[i][j])
            if(len(col_list)!=len(set(col_list))):
                return False
        
        for j in range(9):
            col_list=[]
            for i in range(9):
                if(board[i][j]!="."):
                    col_list.append(board[i][j])
            if(len(col_list)!=len(set(col_list))):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box_vals = []
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != ".":
                            box_vals.append(val)
                if len(box_vals) != len(set(box_vals)):
                    return False



        

        return True
                
        