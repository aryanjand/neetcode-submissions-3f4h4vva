class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for j, num in enumerate(nums):
            if j > k:
                seen.remove(nums[j - k - 1])
            
            if num in seen:
                return True
            
            seen.add(num)
        
        return False