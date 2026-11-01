class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        longest = 1

        for start in range(n):
            prevDirection = 0

            for end in range(start + 1, n):
                if arr[end] == arr[end - 1]:
                    break
                
                direction = 1 if arr[end] > arr[end - 1] else -1

                if direction == prevDirection:
                    break
                
                prevDirection = direction
                longest = max(longest, end - start + 1)
        
        return longest