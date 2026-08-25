from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=Counter(s)
        for i in t:
            if i in a:
                a[i]-=1
            else:
                a[i]=a.get(i,0)+1
        for i,j in a.items():
            if j!=0:
                return False
                break
        else:
            return True
       