class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        eucliden = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l, r):
            pivotIdx = r
            pivotDist = eucliden(points[pivotIdx])
            i = l
            for j in range(l, r):
                if eucliden(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        left, right = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(left, right)
            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
        return points[:k]
