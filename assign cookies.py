class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        c=0
        n=len(g)
        a=len(s)
        i=0
        j=0
        while j<a and i<n:
            if s[j]>=g[i]:
                c+=1
                i+=1
            j+=1
        return c