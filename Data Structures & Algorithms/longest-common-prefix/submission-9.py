class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for s in strs:
            if len(res) > len(s):
                res = res[: len(s)]

            for i in range(min(len(res), len(s))):
                if res[i] != s[i]:
                    res = res[:i]
                    break

        return res
