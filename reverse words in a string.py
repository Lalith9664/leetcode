class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        s=list(s)
        s.reverse()
        return (" ".join(map(str,s)))