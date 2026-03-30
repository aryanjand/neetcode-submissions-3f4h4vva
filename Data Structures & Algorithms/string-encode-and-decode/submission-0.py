class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sindex, slen = 0, len(s)
        res = []

        while sindex < slen:
            wordlen = ''
            
            while s[sindex] != '#':
                wordlen += s[sindex]
                sindex += 1
            sindex += 1 # move forward from delimter

            wordlen = int(wordlen)
            res.append(s[sindex:sindex+wordlen])
            sindex += wordlen

        return res
