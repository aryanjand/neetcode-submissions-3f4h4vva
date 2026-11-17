class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        res = 0

        def dfs(coordinate):
            row, col = coordinate
            if (
                row < 0
                or row >= ROWS
                or col < 0
                or col >= COLS
                or coordinate in seen
                or grid[row][col] == "0"
            ):
                return

            seen.add(coordinate)

            dfs((row + 1, col))
            dfs((row - 1, col))
            dfs((row, col + 1))
            dfs((row, col - 1))

            return

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0" or (r, c) in seen:
                    continue

                dfs((r, c))
                res += 1

        return res
