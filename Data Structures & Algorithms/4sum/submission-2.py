class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if (i != j - 1) and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                
                while left < right:
                    quadruplet = [nums[i], nums[j], nums[left], nums[right]]
                    fourSum = sum(quadruplet)

                    if fourSum > target:
                        right -= 1
                    elif fourSum < target:
                        left += 1
                    else:
                        result.append(quadruplet)
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

        return result
