class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        c=[]
        for i in accounts:
            c.append(sum(i))
        return max(c)