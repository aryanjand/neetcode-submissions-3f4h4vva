from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1, left = len(s1), 0
        s1Set, window = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}, {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for c in s1:
            s1Set[c] += 1

        for right in range(len(s2)):
            window[s2[right]] += 1
            if right - left + 1 > lenS1:
                window[s2[left]] -= 1
                left += 1

            if window == s1Set:
                return True

        return False

