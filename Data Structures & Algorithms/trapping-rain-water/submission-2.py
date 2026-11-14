class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        l, r = 0, n - 1
        maxPliers = [0] * n
        maxLeft, maxRight = height[l], height[r]

        while l <= r:
            maxLeft, maxRight = max(maxLeft, height[l]), max(maxRight, height[r])

            if maxLeft < maxRight:
                maxPliers[l] = maxLeft
                l += 1
            else:
                maxPliers[r] = maxRight
                r -= 1

        water = sum([maxPliers[i] - height[i] for i in range(n)])
        return water