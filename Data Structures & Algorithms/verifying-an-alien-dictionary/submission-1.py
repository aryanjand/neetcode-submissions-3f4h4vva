class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        key = {char: index for index, char in enumerate(order)}
        
        for i in range(1, len(words)):
            word1, word2 = words[i-1], words[i]
            minWordLenght = min(len(word1), len(word2))
            index = 0
            while index < minWordLenght:
                char1, char2 = word1[index], word2[index]
                if key[char1] > key[char2]:
                    return False
                elif key[char1] < key[char2]:
                    break
                index += 1

            if len(word1) > len(word2) and word1[0:len(word2)] == word2:
                return False
        
        return True