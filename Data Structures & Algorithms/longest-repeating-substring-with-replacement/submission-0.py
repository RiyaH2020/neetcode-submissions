class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        unique_chars = set(s)
        maxLen = 0

        for target in unique_chars:
            left = 0
            replacements = 0

            for right in range(len(s)):
                if s[right] != target:
                    replacements += 1

                while replacements > k:
                    if s[left] != target:
                        replacements -= 1
                    left += 1

                maxLen = max(maxLen, right - left + 1)

        return maxLen
