import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for _, word in enumerate(strs):
            key = [0 for _ in range(26)]
            for char in word:
                key[ord(char) - ord('a')] = key[ord(char) - ord('a')] + 1
            key = tuple(key)
            
            if res.get(key):
                res[key].append(word)
            else:
                res[key] = []
                res[key].append(word)

        return list(res.values())