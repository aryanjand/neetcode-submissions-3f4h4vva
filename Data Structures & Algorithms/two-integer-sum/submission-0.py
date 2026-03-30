class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res, numsLen = [], len(nums)

        for i in range(numsLen):
            for j in range(i + 1, numsLen):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
        return res
                
        