class Solution:
    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)) + "#" + s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i, s_len = 0, len(s)
        res = []

        while i < s_len:
            j = s.find("#", i)

            word_len = int(s[i:j])
            i = j + 1
            
            word = s[i : word_len + i]
            i += word_len

            res.append(word)

        return res
