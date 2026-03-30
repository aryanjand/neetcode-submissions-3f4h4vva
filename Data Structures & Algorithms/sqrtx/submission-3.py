class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x

        while left <= right:
            mid = (right - left) // 2 + left
            print(left, mid, right)
            product = mid * mid
            if product > x:
                right = mid - 1
            elif product < x:
                left = mid + 1
            else:
                return mid

        return right