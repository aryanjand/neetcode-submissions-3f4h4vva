class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not k:
            return False
   
        LENGTH = len(nums)
        window = []
        i = j = 0


        while j < LENGTH:
            if nums[j] in window:
                return True

            if len(window) >= k:
                window.remove(nums[i])
                i += 1

            window.append(nums[j])
            j += 1
        
        return False