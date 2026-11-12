class Solution:
    def search(self, n: List[int], t: int) -> int:
        l, r = 0, len(n) - 1

        while l <= r:
            m = ((r - l) // 2) + l

            if n[m] > t:
                r = m - 1
            elif n[m] < t:
                l = m + 1
            else:
                return m
        
        return -1