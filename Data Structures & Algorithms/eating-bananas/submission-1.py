class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = ((right - left) // 2) + left
            hours = 0

            for p in piles:
                hours = hours + (p + k - 1) // k
            
            if hours > h:
                left = k + 1
            else:
                res = k
                right = k - 1
        
        return res