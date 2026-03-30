class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        LENGTH = len(nums)
        left = right = 0
        window = set()


        while right < LENGTH and k != 0:
            if nums[right] in window:
                return True

            if right - left >= k:
                window.remove(nums[left])
                left += 1

            window.add(nums[right])
            right += 1
        
        return False