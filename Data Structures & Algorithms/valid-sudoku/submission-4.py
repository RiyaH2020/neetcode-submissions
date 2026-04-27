class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # Column-major labeled boxes

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                if (val in rows[i] or 
                    val in cols[j] or 
                    val in boxes[(j // 3) * 3 + (i // 3)]):  # your mapping
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[(j // 3) * 3 + (i // 3)].add(val)
        
        return True
