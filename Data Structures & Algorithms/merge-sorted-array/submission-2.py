import copy
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """  

        nums1.reverse()
        nums2.reverse()
        i1, i2, i = n, 0, 0
        total = m + n

        while i1 < total and i2 < n:
            if nums1[i1] > nums2[i2]:
                nums1[i] = nums1[i1]
                i1 += 1
            else:
                nums1[i] = nums2[i2]
                i2 += 1
            i += 1
        
        while i1 < total:
            nums1[i] = nums1[i1]
            i += 1
            i1 += 1
        
        while i2 < n:
            nums1[i] = nums2[i2]
            i += 1
            i2 += 1
        
        nums1.reverse()