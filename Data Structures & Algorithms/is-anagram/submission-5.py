class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = {chr(i + ord('a')): 0 for i in range(26)}
        pMap = {chr(i + ord('a')): 0 for i in range(26)}

        for x, y in zip(s, t):
            sMap[x] += 1
            pMap[y] += 1
        
        return sMap == pMap