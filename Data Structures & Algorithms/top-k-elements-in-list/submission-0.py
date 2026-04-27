class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            if(nums[i] in dict1):
                dict1[nums[i]]+=1
            else:
                dict1[nums[i]]=1
        sorted_dict=dict(sorted(dict1.items(),key=lambda item:item[1], reverse=True))
        key_list=list(sorted_dict.keys())
        return key_list[:k]
        