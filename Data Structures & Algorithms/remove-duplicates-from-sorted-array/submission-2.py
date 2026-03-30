class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        nums_len = len(nums)
        while right < nums_len:
            nums[left] = nums[right]
            while right < nums_len and nums[right] == nums[left]:
                right += 1
            left += 1
        return left