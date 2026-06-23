class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        row = 0

        top, bottom = 0, ROWS - 1
        while top <= bottom:
            mid = ((bottom - top) // 2) + top
            value = matrix[mid][0]

            if value < target:
                row = mid
                top = mid + 1
            elif value > target:
                bottom = mid - 1
            else:
                return True
        
        left, right = 0, COLS - 1
        while left <= right:
            mid = ((right - left) // 2) + left
            value = matrix[row][mid]

            if value < target:
                left = mid + 1
            elif value > target:
                right = mid - 1
            else:
                return True
        
        return False