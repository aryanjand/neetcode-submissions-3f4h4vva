class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cur = 0
        for n in nums:
            cur = cur + 1 if n == 1 else 0
            res = max(res, cur)
        return res