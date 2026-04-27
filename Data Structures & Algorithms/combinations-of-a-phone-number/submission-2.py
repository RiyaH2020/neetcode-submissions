class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if not digits:
            return []
        hash_map={
            '2':['A','B','C'],
            '3':['D','E','F'],
            '4':['G','H','I'],
            '5':['J','K','L'],
            '6':['M','N','O'],
            '7':['P','Q','R','S'],
            '8':['T','U','V'],
            '9':['W','X','Y','Z']
        }
        def dfs(i,temp):
            if(i>=len(digits)):
                res.append(temp)
                return
            for j in range(len(hash_map[digits[i]])):
                dfs(i+1,temp+hash_map[digits[i]][j])
                
        dfs(0,"")
        res=[r.lower() for r in res]
        return res