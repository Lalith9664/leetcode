class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)

        i = 0
        j = len(l) - 1
        s='aeiouAEIOU'
        while i < j:
            if l[i] in s and l[j] in s:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            elif not l[i] in s:
                i += 1
            elif not l[j] in s:
                j -= 1

        return "".join(l)