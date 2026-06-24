class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n=len(s)
        b=[]
        for i in range(n):
            if s[i]==c:
                b.append(i)
        l=[]
        for i in range(n):
            n=float('inf')
            for k in range(len(b)):
                a=abs(i-b[k])
                if a<n:
                    n=a
            l.append(n)
        return l

