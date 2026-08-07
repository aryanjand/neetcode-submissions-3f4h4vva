class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        n = len(nums)
        k = k % n

        for i in range(k // 2):
            temp = nums[i]
            nums[i] = nums[k - 1 - i]
            nums[k - 1 - i] = temp


        for i in range((n - k) // 2):
            temp = nums[i + k]
            nums[i + k] = nums[n - 1 - i]
            nums[n - 1 - i] = temp