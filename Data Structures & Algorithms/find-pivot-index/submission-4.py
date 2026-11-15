class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total, n = sum(nums), len(nums)
        leftSum = 0

        for i in range(n):
            rightSum = total - nums[i] - leftSum
            if rightSum == leftSum:
                return i
            leftSum += nums[i]

        return -1
