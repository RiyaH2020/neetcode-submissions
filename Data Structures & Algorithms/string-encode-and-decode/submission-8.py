class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        print(s)
        list1=[]
        i=0
        len1=""
        while(i<len(s)):
            if(s[i]!='#'):
                len1=len1+s[i]
                i=i+1
            elif(s[i]=='#'):
                flag=1
                print(len1)
                list1.append(s[i+1:i+int(len1)+1])
                i=i+int(len1)+1
                len1=""
                
        return list1

            
            
            

       
