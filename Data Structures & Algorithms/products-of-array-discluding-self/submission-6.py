class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = nums.count(0)
        if count > 1:
            return [0] * n

        prefix = suffix = 1
        res = [1] * n

        # Prefix
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Postfix
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
