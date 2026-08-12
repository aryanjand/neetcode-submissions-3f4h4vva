class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(n)]
        cars.sort()

        res, stack = 0, []
        for car in cars:
            _, arrival = car
            stack.append(arrival)

        while stack:
            arrival = stack[-1]
            while stack and stack[-1] <= arrival:
                stack.pop()
            res += 1
        
        return res
