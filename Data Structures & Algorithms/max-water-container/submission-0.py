class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        lenNums = len(heights)

        for i in range(lenNums):
            for j in range(i + 1, lenNums):
                lenght = min(heights[i], heights[j])
                width = j - i
                area = lenght * width
                maxArea = max(area, maxArea)
        return maxArea
