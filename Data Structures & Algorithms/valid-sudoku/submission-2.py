class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board[0]), len(board)
        
        for r in range(ROWS):
            seen = set()
            for i in range(9):
                if board[r][i] == '.':
                    continue
                if board[r][i] in seen:
                    return False
                else:
                    seen.add(board[r][i])
        
        for c in range(COLS):
            seen = set()
            for i in range(9):
                if board[i][c] == '.':
                    continue
                if board[i][c] in seen:
                    return False
                else:
                    seen.add(board[i][c])
        
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (square % 3) * 3 + i
                    c = (square // 3) * 3 + j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
        return True