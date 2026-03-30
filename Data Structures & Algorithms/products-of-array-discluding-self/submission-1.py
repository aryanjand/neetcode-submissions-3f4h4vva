class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count, prod = 0, 1
        nums_len = len(nums)

        for num in nums:
            if num:
                prod *= num
            else:
                zero_count += 1
            
        res = [0] * nums_len
        if zero_count > 1: return res

        for i, num in enumerate(nums):
            if zero_count:
                if not num:
                    res[i] = prod
            else:
                res[i] = prod // num
            
        return res
