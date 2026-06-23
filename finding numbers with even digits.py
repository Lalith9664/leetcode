class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        c=sum(1 for i in nums if len(str(i))%2==0)
        return c