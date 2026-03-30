from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = (0, 0)

        for n in nums:
            count[n] += 1
        
        for key, value in count.items():
            maxValue = max(res[1], value)
            res = (key, value) if res[1] < value else res
        
        return res[0]

