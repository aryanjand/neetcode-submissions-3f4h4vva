class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + "$" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            count = int(s[i:j])
            word = s[j+1:j+count+1]
            res.append(word)
            i = count + j + 1

        return res