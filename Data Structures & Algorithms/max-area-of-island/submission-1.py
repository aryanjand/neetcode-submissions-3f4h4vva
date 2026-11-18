class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def dfs(coordinate: tuple[int, int]) -> int:
            r, c = coordinate
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or coordinate in seen or grid[r][c] == 0:
                return 0

            seen.add(coordinate)
            return 1 + dfs((r + 1, c)) + dfs((r - 1, c)) + dfs((r, c + 1)) + dfs((r, c - 1))

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 or (r, c) in seen:
                    continue

                area = dfs((r, c))
                maxArea = max(area, maxArea)
        
        return maxArea
