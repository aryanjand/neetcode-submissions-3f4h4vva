class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_len, freq = len(nums), {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        heap = [(value * -1, key) for key, value in freq.items()]
        heapq.heapify(heap)
        
        res = []
        for i in range(k):
            element =  heapq.heappop(heap)
            res.append(element[1])   
        
        return res