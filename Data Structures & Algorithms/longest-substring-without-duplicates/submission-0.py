class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = l = 0

        for r in s:
            while r in window:
                window.remove(s[l])
                l += 1

            window.add(r)
            res = max(res, len(window))
        
        return res
