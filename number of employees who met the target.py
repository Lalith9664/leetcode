class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        c=sum(1 for i in hours if i>=target)
        return c