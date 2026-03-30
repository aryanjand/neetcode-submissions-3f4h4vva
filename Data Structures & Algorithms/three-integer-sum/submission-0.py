class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, nums_len = set(), len(nums)
        nums.sort()

        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                for k in range(j + 1, nums_len):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(tmp))
        return [list(r) for r in res]