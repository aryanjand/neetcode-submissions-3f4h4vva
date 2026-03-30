class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(1, numRows):
            last_row = res[-1]
            cur_row = [1]
            for i in range(len(last_row) - 1):
                cur_val = last_row[i]
                next_val = last_row[i + 1]
                cur_row.append(cur_val + next_val)
            cur_row.append(1)
            res.append(cur_row)
        return res