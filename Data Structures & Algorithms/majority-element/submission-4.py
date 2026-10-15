class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 0

        for n in nums:
            if res == n:
                count += 1
            elif count == 0:
                res = n
                count += 1
            else:
                count -= 1
        
        return res
