class Solution:
    def _isAlphanumeric(self, char: str) -> bool:
        return (ord("a") <= ord(char) <= ord("z")) or (ord("0") <= ord(char) <= ord("9"))

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self._isAlphanumeric(s[left]):
                left += 1
            while left < right and not self._isAlphanumeric(s[right]):
                right -= 1

            if left < right and s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
