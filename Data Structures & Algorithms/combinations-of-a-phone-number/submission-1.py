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
        digits=list(digits)
        def helper(i,curr):
            if(i>=len(digits)):
                res.append(curr.lower())
                return
            for j in range(len(hash_map[digits[i]])):
                helper(i+1,curr+hash_map[digits[i]][j])
        helper(0,"")
        return res
        