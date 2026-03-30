class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left: List[int], n: int, right: List[int], m: int):
            l = r = 0
            res = []

            while l < n and r < m:
                if left[l] <= right[r]:
                    res.append(left[l])
                    l += 1
                else:
                    res.append(right[r])
                    r += 1
            
            if l < n:
                res = res + left[l:]
            elif r < m:
                res = res + right[r:]

            return res
         
        def mergeSort(arr: List[int]):
            
            if len(arr) <= 1:
                return arr
            
            mid = (len(arr) // 2)
            leftArr = mergeSort(arr[:mid])
            rightArr = mergeSort(arr[mid:])

            return merge(leftArr, len(leftArr), rightArr, len(rightArr))
        
        return mergeSort(nums)