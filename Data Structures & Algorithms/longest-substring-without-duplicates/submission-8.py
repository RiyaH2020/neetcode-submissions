class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxlen = 0
        n = len(s)
        char_set = set()  # track current window

        while right < n:
            if s[right] not in char_set:
                char_set.add(s[right])
                maxlen = max(maxlen, right - left + 1)
                right += 1
            else:
                char_set.remove(s[left])
                left += 1

        return maxlen
