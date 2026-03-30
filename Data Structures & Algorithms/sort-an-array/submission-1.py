class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr: List[int], start: int, mid: int, end: int):
            l, r = start, mid + 1
            i, temp = 0, [0] * (end - start + 1)

            while l <= mid and r <= end:
                if arr[l] <= arr[r]:
                    temp[i] = arr[l]
                    l += 1
                else:
                    temp[i] = arr[r]
                    r += 1
                i += 1
            

            while l <= mid:
                temp[i] = arr[l]
                l += 1
                i += 1
            
            while r <= end:
                temp[i] = arr[r]
                r += 1
                i += 1

            arr[start:end+1] = temp

        def mergeSort(arr: List[int], left: int, right: int) -> List[int]:

            if right - left + 1 <= 1:
                return arr
            
            mid = left + ((right - left) // 2)

            mergeSort(arr, left, mid)
            mergeSort(arr, mid + 1, right)

            merge(arr, left, mid, right)

            return arr
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums