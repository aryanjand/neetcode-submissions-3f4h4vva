import copy

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = copy.deepcopy(nums)
        for element in temp:
            nums.append(element)
        
        return nums