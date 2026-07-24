from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        res, maxFreq = 0, 0
        left = 0

        for right, char in enumerate(s):
            freq[char] += 1
            windowSize = right - left + 1
            maxFreq = max(maxFreq, freq[char])

            if windowSize - maxFreq <= k:
                res = max(res, windowSize)
            else:
                freq[s[left]] -= 1
                left += 1

        return res