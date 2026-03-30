# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         nums_len = len(nums)
#         res = [1] * nums_len

#         prefix = 1
#         for i in range(nums_len):
#             res[i] *= prefix
#             prefix *= nums[i]


#         postfix = 1
#         for i in range(nums_len -1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
        
#         return res



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        res = [1] * nums_len

        prefix = 1
        for i, n in enumerate(nums):
            prefix *= n
            if i < nums_len - 1:
                res[i + 1] = prefix

        # post
        postfix = 1
        for i, n in enumerate(nums[::-1]):
            postfix *= n
            if i < nums_len - 1:
                res[nums_len - i - 2] *= postfix
        
        return res