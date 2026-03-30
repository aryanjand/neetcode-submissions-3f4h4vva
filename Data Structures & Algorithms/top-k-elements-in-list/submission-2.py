class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_len, freq = len(nums), {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])   
        
        return res