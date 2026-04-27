class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Row check
        for row in range(9):
            t_l = [x for x in board[row] if x != '.']
            if len(t_l) != len(set(t_l)):
                return False

        # Column check
        for col in range(9):
            t_l = [board[r][col] for r in range(9) if board[r][col] != '.']
            if len(t_l) != len(set(t_l)):
                return False

        # 3x3 box check
        for i in range(3):
            for j in range(3):
                t_l = []
                for r in range(i*3, i*3 + 3):
                    for c in range(j*3, j*3 + 3):
                        if board[r][c] != '.':
                            t_l.append(board[r][c])
                if len(t_l) != len(set(t_l)):
                    return False

        return True
