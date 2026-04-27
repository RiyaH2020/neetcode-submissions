class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        list1=[]
        len1=""
        i=0
        while i< (len(s)):
            if(s[i].isdigit()):
                len1+=s[i]
                print(len1)
                i=i+1
            elif(s[i]=="#"):
                l1=int(len1)
                list1.append(s[i+1:i+1+l1])
                i=i+1+l1
                len1=""
                
        return list1

                

            



