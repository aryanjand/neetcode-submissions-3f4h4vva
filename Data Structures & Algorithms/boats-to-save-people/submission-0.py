class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        numBoats = 0
        people.sort()
        left, right = 0, len(people) - 1

        while left < right:
            total = people[left] + people[right]
            
            if total > limit:
                right -= 1
                numBoats += 1
            else:
                left += 1
                right -= 1
                numBoats += 1
        
        if left == right:
            numBoats += 1
        
        return numBoats