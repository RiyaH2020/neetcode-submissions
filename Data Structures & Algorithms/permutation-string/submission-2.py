class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = {}
        for c in s1:
            map1[c] = map1.get(c, 0) + 1

        window = {}
        left = 0
        n = len(s1)

        for right in range(len(s2)):
            c = s2[right]

            if c in map1:
                window[c] = window.get(c, 0) + 1

                # If count exceeds, shrink from left
                while window[c] > map1[c]:
                    window[s2[left]] -= 1
                    if window[s2[left]] == 0:
                        del window[s2[left]]
                    left += 1

            else:
                # Character not in map1 → reset window
                window.clear()
                left = right + 1

            # Check for match
            if right - left + 1 == n and window == map1:
                return True

        return False
