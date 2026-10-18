import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quickSort(l, r):
            if r - l <= 0:
                return

            pIndex = random.randint(l, r)
            pivot = nums[pIndex]
            # Move pivot to the end
            nums[pIndex], nums[r] = nums[r], nums[pIndex]

            cur = l
            for i in range(l, r):
                if nums[i] < pivot:
                    nums[cur], nums[i] = nums[i], nums[cur]
                    cur += 1

            # Place the pivot in its correct sorted position
            nums[cur], nums[r] = nums[r], nums[cur]


            # Recursively sort the subarrays on either side of the pivot
            quickSort(l, cur - 1)
            quickSort(cur + 1, r)

        quickSort(0, len(nums) - 1)
        return nums
