class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = left = window = 0

        for i in range(min(len(arr), k)):
            window += arr[i]    

        if window / k >= threshold:
            res += 1

        for right in range(k, len(arr)):
            window += arr[right] - arr[left]
            left += 1
            if window / k >= threshold:
                res += 1
        
        return res
