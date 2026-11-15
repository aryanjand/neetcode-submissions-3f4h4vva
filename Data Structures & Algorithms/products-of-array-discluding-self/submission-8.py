class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = nums + [1]
        prefix = suffix = 1
        res = [1] * n

        # Prefix
        for i in range(n):
            prefix *= nums[i - 1]
            res[i] *= prefix

        # Postfix
        for i in range(n - 1, -1, -1):
            suffix *= nums[i + 1]
            res[i] *= suffix

        return res
