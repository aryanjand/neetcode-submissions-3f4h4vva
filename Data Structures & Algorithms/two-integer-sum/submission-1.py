class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visted, numsLen = {}, len(nums)

        for i in range(numsLen):
            diff = target - nums[i]
            if diff in visted:
                return [visted[diff], i]
            else:
                visted[nums[i]] = i
        