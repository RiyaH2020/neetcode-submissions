class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1=[0]*26
        list2=[0]*26
        for char in s:
            p=ord(char)-ord('a')
            list1[p]+=1
        for char in t:
            p=ord(char)-ord('a')
            list2[p]+=1
        if(list1==list2):
            return True
        else:
            return False
