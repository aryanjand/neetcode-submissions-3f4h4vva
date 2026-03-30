class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = COLS = 9
        ROWS_MAP = defaultdict(set)
        COLS_MAP = defaultdict(set)
        SQUARES_MAP = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in COLS_MAP[c] or board[r][c] in ROWS_MAP[r] or board[r][c] in SQUARES_MAP[(r // 3, c // 3)]:
                    return False
                
                COLS_MAP[c].add(board[r][c])
                ROWS_MAP[r].add(board[r][c])
                SQUARES_MAP[(r // 3, c // 3)].add(board[r][c])
        
        return True