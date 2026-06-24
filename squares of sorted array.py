class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        c=[i*i for i in nums]
       
        return sorted(c)