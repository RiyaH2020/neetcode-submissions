class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        list1=[]
        for s in strs:
            s1=''.join(sorted(s))
            if(s1 in hashmap):
                hashmap[s1]=hashmap[s1]+[s]
            else:
                hashmap[s1]=[s]
        for string in hashmap:
            list1.append(hashmap[string])

        return list1
            

        