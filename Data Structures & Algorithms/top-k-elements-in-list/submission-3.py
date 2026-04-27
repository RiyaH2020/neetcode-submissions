class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        res=[]
        count=[[] for _ in range(len(nums)+1)]
        for n in nums:
            dict1[n]=1+dict1.get(n,0)
        for n in dict1:
            count[dict1[n]].append(n)
        for  i in range(len(count)-1,0,-1):
            if(count[i]):
                res.extend(count[i])
            if(len(res)>=k):
                return res[:k]



        
        
        