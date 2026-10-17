class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(l, r, nums):
            if l == r:
                return

            mid = l + ((r - l) // 2)
            mergeSort(l, mid, nums)
            mergeSort(mid + 1, r, nums)

            merge(l, mid, r, nums)

        def merge(l, mid, r, nums):
            left, right = nums[l : mid + 1], nums[mid + 1 : r + 1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] < right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        mergeSort(0, len(nums) - 1, nums)

        return nums
