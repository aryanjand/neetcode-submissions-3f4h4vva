class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, res = 0, 0
        window = {}

        for right in range(len(s)):
            if s[right] in window:
                left = max(left, window[s[right]] + 1)
            
            window[s[right]] = right
            res = max(res, right - left + 1)

        return res