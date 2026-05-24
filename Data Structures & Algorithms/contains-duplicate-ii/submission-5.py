class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        i = 0

        for j, n in enumerate(nums):
            if abs(i - j) > k:
                window.remove(nums[i])
                i += 1
            if n in window:
                return True
            window.add(n)
        
        return False