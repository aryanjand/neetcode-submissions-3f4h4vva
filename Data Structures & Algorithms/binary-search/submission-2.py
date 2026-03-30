class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = ((right - left) // 2) + left

            if target < nums[mid]:
                right = right - 1
            elif target > nums[mid]:
                left = left + 1
            else:
                return mid

        return -1