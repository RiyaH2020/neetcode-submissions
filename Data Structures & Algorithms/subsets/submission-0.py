class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(nums, curr):
            if not nums:
                res.append(curr)
                return
            
            
            helper(nums[1:], curr + [nums[0]])
         
            helper(nums[1:], curr)

        helper(nums, [])
        return res
