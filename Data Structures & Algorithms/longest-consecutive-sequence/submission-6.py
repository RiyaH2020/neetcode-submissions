class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        max_len=0
        for n in set1:
            if n-1 not in set1:
                c=1
                i=n
                while i+1 in set1:
                    i=i+1
                    c=c+1
                max_len=max(max_len,c)
        return max_len

        