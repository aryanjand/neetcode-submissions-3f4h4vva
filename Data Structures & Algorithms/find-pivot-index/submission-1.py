class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n

        for i in range(n):
            prefix[i] = prefix[i - 1] + nums[i] if i > 0 else nums[i]

        for i in range(n):
            leftSum = prefix[i - 1] if i > 0 else 0
            rightSum = prefix[n - 1] - prefix[i]
            if leftSum == rightSum:
                return i
        return -1
