class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        left, longest = 0, 1
        prevDirection = 0
        
        for right in range(1, n):
            if arr[right] > arr[right - 1]:
                direction = 1
            elif arr[right] < arr[right - 1]:
                direction = -1
            else:
                direction = 0

            if direction == 0:
                left = right
            elif direction == prevDirection:
                left = right - 1
            
            prevDirection = direction
            longest = max(longest, right - left + 1)
        
        return longest