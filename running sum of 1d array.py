class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        c=[]
        s=0
        for i in nums:
            s+=i
            c.append(s)
        return c