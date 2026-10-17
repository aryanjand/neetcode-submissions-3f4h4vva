from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(l, r):
            if l >= r:
                return

            mid = l + (r - l) // 2

            mergeSort(l, mid)
            mergeSort(mid + 1, r)

            merge(l, mid, r)

        def merge(l, mid, r):
            i = l
            j = mid + 1

            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    i += 1
                else:
                    # Save the element before shifting anything.
                    value = nums[j]

                    # Shift elements right to make room.
                    k = j
                    while k > i:
                        nums[k] = nums[k - 1]
                        k -= 1

                    nums[i] = value

                    # Both sorted regions have shifted.
                    i += 1
                    mid += 1
                    j += 1

        mergeSort(0, len(nums) - 1)
        return nums