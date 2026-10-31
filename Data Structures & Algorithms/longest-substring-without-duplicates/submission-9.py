class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = res = 0
        window = set()

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            res = max(res, R - L + 1)

        return 0 if res == float("inf") else res