class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0

        # First pass
        for i in range(n):
            for k in range(i, n - 1):
                if not (
                    (k % 2 != 0 and arr[k] > arr[k + 1]) or (k % 2 == 0 and arr[k] < arr[k + 1])
                ):
                    break
                res = max(res, k - i + 1)
        
        # Second pass
        for i in range(n):
            for k in range(i, n - 1):
                if not (
                    (k % 2 == 0 and arr[k] > arr[k + 1]) or (k % 2 != 0 and arr[k] < arr[k + 1])
                ):
                    break
                res = max(res, k - i + 1)
        
        return res + 1