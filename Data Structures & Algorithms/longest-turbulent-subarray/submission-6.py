class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, longest = 0, 1
        prevDirection = 0  # 0 > -1 and 0 < 1

        for right in range(1, len(arr)):

            if arr[right - 1] > arr[right] and prevDirection != -1:
                longest = max(longest, right - left + 1)
                prevDirection = -1
            elif arr[right - 1] < arr[right] and prevDirection != 1:
                longest = max(longest, right - left + 1)
                prevDirection = 1
            else:
                if arr[right] == arr[right - 1]:
                    left = right
                else:
                    left = right - 1
                prevDirection = -1 if arr[right - 1] > arr[right] else (1 if arr[right - 1] < arr[right] else 0)
        
        return longest