class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = (nums[0], 0)

        for n in nums:
            key, count = res
            if n == key:
                res = (key, count + 1)
            else:
                if count <= 1:
                    res = (n, 1)
                else:
                    res = (key, count - 1)
        
        return res[0]