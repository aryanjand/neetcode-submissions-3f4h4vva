class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        for i, _ in enumerate(nums):
            for j, num in enumerate(nums):
                if i != j:
                    res[i] *= num
        return res
