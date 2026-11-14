class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        water = 0
        l, r = 0, n - 1
        maxLeft, maxRight = height[l], height[r]
        while l <= r:
            if maxLeft < maxRight:
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
                l += 1
            else:
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]
                r -= 1

        return water
