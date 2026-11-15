class NumArray:
    def __init__(self, nums: List[int]):
        total, n = 0, len(nums)
        self.prefix = [0] * n

        for i in range(n):
            total += nums[i]
            self.prefix[i] = total

    def sumRange(self, left: int, right: int) -> int:
        rightPrefix = self.prefix[right]
        leftPrefix = self.prefix[left - 1] if left > 0 else 0
        return rightPrefix - leftPrefix


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
