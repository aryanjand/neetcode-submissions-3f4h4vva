class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0

        for right, n in enumerate(nums):
            if n != val:
                nums[left] = nums[right]
                left += 1

        return left