
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = (nums[0], 1)      

        for i in range(1, len(nums)):
            key, value = res
            if key == nums[i]:
                res = (key, value + 1)
            else:
                value -= 1
                if not value:
                    res = (nums[i], 1)
                else:
                    res = (key, value)
        
        return res[0]

