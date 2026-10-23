import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(freq, n) for n, freq in count.items()]
        heapq.heapify_max(heap)

        return [heapq.heappop_max(heap)[1] for _ in range(k)]