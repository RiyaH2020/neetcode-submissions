class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res=[]
        len1=""
        i=0
        while(i<len(s)):
            if(s[i].isdigit()):
                len1+=s[i]
                i=i+1
                continue
            else:
                t=int(len1)
                res.append(s[i+1:i+1+t])
                i=i+1+t
                len1=""
        return res
            

