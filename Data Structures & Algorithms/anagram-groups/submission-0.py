import copy

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copyStrs = copy.deepcopy(strs)
        copyStrs = ["".join(sorted(word)) for word in copyStrs]
        res = {word: [] for word in copyStrs}

        for index, word in enumerate(copyStrs):
            res[word].append(strs[index])
        
        return list(res.values())