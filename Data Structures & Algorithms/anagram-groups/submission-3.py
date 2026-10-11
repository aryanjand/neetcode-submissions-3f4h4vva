from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        map = defaultdict(list)

        for s in strs:
            scopy = "".join(sorted(s))

            map[scopy].append(s)
        
        for key, values in map.items():
            res.append(values)
        
        return res