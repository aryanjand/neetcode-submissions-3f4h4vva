class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1, index2 = 0, 0
        res = ''

        while index1 < len(word1) and index2 < len(word2):
            res = res + word1[index1] + word2[index2]

            index1 += 1
            index2 += 1
        
        if index1 < len(word1):
            res = res + word1[index1:]
        if index2 < len(word2):
            res = res + word2[index2:]
        
        return res