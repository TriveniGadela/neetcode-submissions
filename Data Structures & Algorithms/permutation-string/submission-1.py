class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        h1={}
        h2={}
        for i in s1:
            h1[i]=h1.get(i,0)+1
        left=0
        right=0
        while right<len(s2):
            h2[s2[right]]=h2.get(s2[right],0)+1
            if right-left+1>len(s1):
                h2[s2[left]]-=1
                if h2[s2[left]]==0:
                    del h2[s2[left]]
                left+=1
            if h1==h2:
                return True
            right+=1
        return False
        