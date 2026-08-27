class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        key = {char: i for i, char in enumerate(order)}

        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]
            min_length = min(len(word1), len(word2))

            for j in range(min_length):
                char1, char2 = word1[j], word2[j]

                if key[char1] > key[char2]:
                    return False

                if key[char1] < key[char2]:
                    break
            else:
                # All shared characters are equal, so word2
                # must not be a prefix of word1.
                if len(word1) > len(word2):
                    return False

        return True