class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        list1=[0]*len(nums)
        for n in nums:
            dict1[n]=dict1.get(n,0)+1
        list1=sorted(dict1.keys(),key=lambda x: dict1[x], reverse=True)
        return list1[:k]