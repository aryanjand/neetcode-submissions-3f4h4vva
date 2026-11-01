class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = longest = maxFreq = 0
        count = [0] * 26
        n = len(s)
        for right in range(n):
            count[ord(s[right]) - ord('A')] += 1
            maxFreq = max(maxFreq, count[ord(s[right]) - ord('A')])

            while (right - left + 1) - maxFreq > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)
        
        return longest