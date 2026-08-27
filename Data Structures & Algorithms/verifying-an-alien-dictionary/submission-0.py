class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        key = {}
        for index, char in enumerate(order):
            key[char] = index
        
        wordsCopy = words.copy()
        wordsCopy.sort(key=lambda x: [key[c] for c in x])

        return wordsCopy == words