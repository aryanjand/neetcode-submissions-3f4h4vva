class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        window = [arr[i] for i in range(k - 1)]

        for right in range(k - 1, len(arr)):
            window.append(arr[right])
            avg = sum(window) / k
            res += 1 if avg >= threshold else 0
            window.pop(0)
        
        return res

