from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, pMap = defaultdict(int), defaultdict(int)

        for x, y in zip(s, t):
            sMap[x] += 1
            pMap[y] += 1
        
        return sMap == pMap