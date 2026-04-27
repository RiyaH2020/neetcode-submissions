class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        list1=[]
        for ele in strs:
            if(tuple(sorted(ele)) in dict1):
                dict1[tuple(sorted(ele))]+=[ele]
            else:
                dict1[tuple(sorted(ele))]=[ele]
        print(dict1)
        for key in dict1:
            list1.append(dict1[key])
        return list1
        