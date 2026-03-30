class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for sI in range(1, len(strs)):
            s = strs[sI]
            i = 0

            while i < len(res) and i < len(s) and res[i] == s[i]:
                i += 1

            res = res[:i]

        return res