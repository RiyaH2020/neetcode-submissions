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

        for i in range(0,9,3):
            for j in range(0,9,3):
                col_list=[]
                for x in range(3):
                    for y in range(3):
                        if(board[i+x][j+y]!="."):  
                            col_list.append(board[i+x][j+y])
                if(len(col_list)!=len(set(col_list))):
                    return False
        return True
            
        