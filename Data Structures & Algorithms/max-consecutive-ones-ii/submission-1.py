class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_ones = 0  # number of consecutive 1s before the last 0
        cur_ones = 0   # current run of consecutive 1s
        max_ones = 0

        for n in nums:
            if n == 1:
                cur_ones += 1
            else:
                # flip this zero: total ones = prev_ones + 1 + cur_ones
                max_ones = max(max_ones, prev_ones + 1 + cur_ones)
                prev_ones = cur_ones  # the run before this zero
                cur_ones = 0           # reset current run

        # handle the case if the array ends with 1s
        max_ones = max(max_ones, prev_ones + 1 + cur_ones)

        return min(max_ones, len(nums))

