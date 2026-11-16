class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = ((r - l) // 2) + l
            curr = nums[m]
            
            if curr > target:
                r = m - 1
            elif curr < target:
                l = m + 1
            else:
                return m
        
        return -1