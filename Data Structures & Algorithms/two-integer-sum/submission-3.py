class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visted = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in visted:
                return [visted[complement], i]
            visted[num] = i
