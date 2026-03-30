class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s) // 2
        lenArr = len(s)
        for i in range(mid):
            temp = s[i]
            s[i] = s[lenArr - 1 - i]
            s[lenArr - 1 - i] = temp