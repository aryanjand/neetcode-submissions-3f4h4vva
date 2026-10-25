class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = 0
        cur_max = 0
        max_sum = float("-inf")
        cur_min = 0
        min_sum = float("inf")

        for x in nums:
            cur_max = max(x, cur_max + x)
            max_sum = max(max_sum, cur_max)
            cur_min = min(x, cur_min + x)
            min_sum = min(min_sum, cur_min)
            total_sum += x

        if max_sum < 0:
            return max_sum
        return max(max_sum, total_sum - min_sum)