class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count_zeros = 0

        for n in nums:
            if n == 0:
                product *= 1
                count_zeros += 1
            else:
                product *= n
        
        for i, n in enumerate(nums):
            if not count_zeros:
                nums[i] = product // n
            elif count_zeros > 1:
                nums[i] = 0
            else:
                nums[i] = 0 if n != 0 else product
        
        return nums