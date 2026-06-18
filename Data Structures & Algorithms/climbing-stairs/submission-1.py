class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {}

        def dfs(n):
            if n in memory:
                return memory[n]

            if n <= 0:
                if n == 0:
                    return 1
                if n < 0:
                    return 0

            res = dfs(n - 1) + dfs(n - 2)
            memory[n] = res

            return memory[n]

        return dfs(n)
