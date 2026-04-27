class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        list1=[]
        for l in strs:
            str1="".join(sorted(l))
            if(str1 in dict1):
                dict1[str1]+=[l]
            else:
                dict1[str1]=[l]
        for k in dict1:
            list1.append(dict1[k])
        return list1


        