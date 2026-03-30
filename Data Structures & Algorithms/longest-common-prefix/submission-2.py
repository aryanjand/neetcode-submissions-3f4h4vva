class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for s in strs:
            left = right = 0

            while left < len(res) and right < len(s) and res[left] == s[right]:
                left += 1
                right += 1

            res = res[:left]

        return res