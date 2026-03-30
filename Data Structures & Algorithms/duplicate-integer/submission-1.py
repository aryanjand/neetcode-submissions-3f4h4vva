class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exist = set()
        n = len(nums)

        for i in range(n):
            if nums[i] in exist:
                return True
            else:
                exist.add(nums[i])
        return False
