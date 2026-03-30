class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        pre = ([1] * (nums_len + 1))
        post = ([1] * (nums_len + 1))
        res = ([1] * nums_len)

        prod = 1
        for i, n in enumerate(nums):
            prod *= n
            pre[i + 1] = prod
        
        prod = 1
        for i, n in enumerate(nums[::-1]):
            prod *= n
            post[nums_len - i - 1] = prod
        
        for i in range(nums_len):
            res[i] = pre[i] * post[i + 1]
        
        return res
