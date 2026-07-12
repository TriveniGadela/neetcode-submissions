class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        for i in s:
            h[i]=h.get(i,0)+1
        for j in t:
            if j in h:
                h[j]-=1
            else:
                h[j]=h.get(j,0)+1
        for i,j in h.items():
            if j!=0:
                return False
                break
        else:
            return True
        