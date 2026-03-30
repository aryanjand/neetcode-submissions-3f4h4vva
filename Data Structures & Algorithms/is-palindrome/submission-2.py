class Solution:
    def isAlphanumeric(self, s: str):
        return ((ord('A') <= ord(s) <= ord('Z')) or (ord('a') <= ord(s) <= ord('z')) or (ord('0') <= ord(s) <= ord('9')))

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while (left <= right):
            while(left <= right and not self.isAlphanumeric(s[left])):
                left += 1
            while(left <= right and not self.isAlphanumeric(s[right])):
                right -= 1
            if (left <= right and s[left].lower() != s[right].lower()):
                return False
            left += 1
            right -= 1
        return True