class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, (len(heights) - 1)
        maxArea = 0

        while (left < right):
            lenght = min(heights[left], heights[right])
            width = right - left
            area = lenght * width
            maxArea = max(area, maxArea)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return maxArea
