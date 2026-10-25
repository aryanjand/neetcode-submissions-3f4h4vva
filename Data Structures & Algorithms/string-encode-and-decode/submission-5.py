class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)) + "#" + s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            separator = s.find("#", i)

            word_length = int(s[i:separator])
            i = separator + 1
            
            word = s[i : word_length + i]
            i += word_length

            res.append(word)

        return res
