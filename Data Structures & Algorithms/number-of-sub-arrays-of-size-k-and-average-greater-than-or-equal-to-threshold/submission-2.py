class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = left = window = 0

        for i in range(min(len(arr), k - 1)):
            window += arr[i]    

        for right in range(k - 1, len(arr)):
            window += arr[right]
            avg = window / k
            res += 1 if avg >= threshold else 0
            window -= arr[left]
            left += 1
        
        return res

