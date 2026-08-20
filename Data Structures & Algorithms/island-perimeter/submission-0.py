class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        perimeter = 0
        directions = [-1, 1]

        for r in range(ROWS):
            for c in range(COLS):
                land = grid[r][c]
                if land:
                    # ROWS
                    for d in directions:
                        if not (0 <= r + d < ROWS) or not grid[r + d][c]:
                            perimeter += 1
                    # COLS
                    for d in directions:
                        if not (0 <= c + d < COLS) or not grid[r][c + d]:
                            perimeter += 1
        return perimeter