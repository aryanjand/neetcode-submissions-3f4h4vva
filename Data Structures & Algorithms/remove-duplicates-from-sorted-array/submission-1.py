class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 1
        left, right = 0, 1
        k = 0
        while right < len(nums):
            if left == right:
                right += 1
            elif nums[left] == nums[right]:
                nums.pop(right)
            else:
                left += 1
        return len(nums)