class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        for n in nums:
            hash_map[n]=hash_map.get(n,0)+1
        set1=list(set(nums))
        list1=sorted(set1, key=lambda x: hash_map[x],reverse=True)
        return list1[:k]