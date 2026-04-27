class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        res=[]
        for s in strs:
            temp=str(sorted(s))
            if temp in dict1:
                dict1[temp]+=[s]
            else:
                dict1[temp]=[s]
        for key in dict1:
            res.append(dict1[key])
        return res

        