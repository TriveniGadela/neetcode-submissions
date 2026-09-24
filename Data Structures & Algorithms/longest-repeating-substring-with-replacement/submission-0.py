class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        h={}
        maxi=0
        n=0
        while right<len(s):
            h[s[right]]=h.get(s[right],0)+1
            n=max(n,h[s[right]])
            if right-left+1-n>k:
                h[s[left]]-=1
                if h[s[left]]==0:
                    del h[s[left]]
                left+=1
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi
