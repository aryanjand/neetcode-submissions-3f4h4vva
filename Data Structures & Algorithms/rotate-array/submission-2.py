class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sI = len(nums) - (k % len(nums))
        end, start = nums[sI:], nums[:sI]
        eI = sI = i = 0

        while eI < len(end):
            nums[i] = end[eI]
            i += 1
            eI += 1
        while sI < len(start):
            nums[i] = start[sI]
            i += 1
            sI += 1
        