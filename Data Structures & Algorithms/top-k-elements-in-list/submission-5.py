import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(freq, n) for n, freq in count.items()]
        heapq.heapify_max(heap)

        res = []

        for i in range(k):
            _, n = heapq.heappop_max(heap)
            res.append(n)

        return res 