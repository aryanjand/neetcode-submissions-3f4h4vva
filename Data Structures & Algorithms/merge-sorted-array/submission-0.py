import copy
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copyNums1 = copy.deepcopy(nums1)
        index = index1 = index2 = 0

        while index1 < m and index2 < n:
            if copyNums1[index1] < nums2[index2]:
                nums1[index] = copyNums1[index1]
                index1 += 1
            else:
                nums1[index] = nums2[index2]
                index2 += 1
            index += 1
        
        while index1 < m:
            nums1[index] = copyNums1[index1]
            index1 += 1
            index += 1
        
        while index2 < n:
            nums1[index] = nums2[index2]
            index2 += 1
            index += 1