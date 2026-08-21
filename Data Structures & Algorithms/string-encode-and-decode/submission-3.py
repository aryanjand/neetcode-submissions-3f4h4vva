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
            j = s.find("$", i)
            lenght = int(s[i:j])
            start = j + 1
            end = lenght + start
            word = s[start:end]
            res.append(word)
            i = end

        return res