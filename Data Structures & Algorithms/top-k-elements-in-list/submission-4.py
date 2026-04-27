class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        list2=[0]*k
        for i in range(len(nums)):
            if(nums[i] in dict1):
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]]=1
        list1=sorted(dict1.items(),key=lambda item: item[1], reverse=True )
        for t in range(k):
            list2[t]=list1[t][0]
           
        return list2
        