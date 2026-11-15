class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.P = [[0] * COLS for _ in range(ROWS)]
        total = 0

        for r in range(ROWS):
            total = 0
            for c in range(COLS):
                total += matrix[r][c]
                self.P[r][c] = total

        for c in range(COLS):
            for r in range(1, ROWS):
                self.P[r][c] += self.P[r - 1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        if row1 == 0 and col1 == 0:
            return self.P[row2][col2]
        if row1 == 0:
            return self.P[row2][col2] - self.P[row2][col1 - 1]
        if col1 == 0:
            return self.P[row2][col2] - self.P[row1 - 1][col2]

        return (
            self.P[row2][col2]
            - self.P[row1 - 1][col2]
            - self.P[row2][col1 - 1]
            + self.P[row1 - 1][col1 - 1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
