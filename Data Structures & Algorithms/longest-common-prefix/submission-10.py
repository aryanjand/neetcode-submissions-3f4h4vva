class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for i in range(len(res)):
            for s in strs:
                if i == len(s) or s[i] != res[i]:
                    return s[:i]
        return res
