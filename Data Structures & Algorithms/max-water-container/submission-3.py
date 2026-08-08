class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left, right = 0, len(heights) - 1

        while left < right:
            w = right - left
            l = min(heights[left], heights[right])
            res = max(res, l * w)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return res