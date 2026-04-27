class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i,j,k):
            if(k==len(word)):
                return True
            if(i<0 or j<0 or i>=len(board) or j>=len(board[0])):
                return False
            if(board[i][j]!=word[k]):
                return False
            temp=board[i][j]
            board[i][j]="#"
            found=(helper(i+1,j,k+1)or
            helper(i-1,j,k+1)or
            helper(i,j+1,k+1)or
            helper(i,j-1,k+1))
            board[i][j]=temp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if(helper(i,j,0)):
                    return True
        return False


            

