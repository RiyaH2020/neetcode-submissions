class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0:
            return ""
        dp=[[0]*n for _ in range(n)]
        start=0
        maxlen=1
        for i in range(n):
            dp[i][i]=1
        for i in range(n-1):
            if(s[i]==s[i+1]):
                dp[i][i+1]=2
                start=i
                maxlen=2
            else:
                dp[i][i+1]=0
        for l in range(3,n+1):
            for i in range(n-l+1):
                j=i+l-1
                if(s[i]==s[j] and dp[i+1][j-1]>0):
                    dp[i][j]=dp[i+1][j-1]+2
                    if(dp[i][j]>maxlen):
                        start=i
                        maxlen=dp[i][j]
                else:
                    dp[i][j]=0
        return s[start:start+maxlen]
                
