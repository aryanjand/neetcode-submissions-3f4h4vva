class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        for n in range(2, x):
            if n * n > x:
                return n - 1