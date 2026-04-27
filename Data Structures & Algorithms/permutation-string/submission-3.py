class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        right=0
        map1={}
        window={}
        n=len(s1)
        for i in s1:
            map1[i]=map1.get(i,0)+1
        for right in range(len(s2)):
            c=s2[right]
            if c in map1:
                window[c]=window.get(c,0)+1
                
                if(window[c]>map1[c]):
                    window[s2[left]]=window[s2[left]]-1
                    if(window[s2[left]]==0):
                        del window[s2[left]]
                    left=left+1
            else:
                window.clear()
                left=right+1
            if(right-left+1==n and window==map1):
                return True
        return False

