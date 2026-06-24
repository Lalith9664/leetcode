class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=list(word1)
        w2=list(word2)

        i=0
        j=0
        m=[]
        while i<len(word1) and j<len(word2):
            m.append(w1[i])
            i+=1
            m.append(w2[j])
            j+=1
        while i<len(word1):
            m.append(w1[i])
            i+=1 
        while j<len(word2):
            m.append(w2[j])
            j+=1
        return "".join(m)