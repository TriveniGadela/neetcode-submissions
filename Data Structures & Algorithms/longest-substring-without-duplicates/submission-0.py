class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h={}
        left=0
        right=0
        maxi=0
        while right<len(s):
            h[s[right]]=h.get(s[right],0)+1
            while h[s[right]]>1:
                h[s[left]]-=1
                if h[s[left]]==0:
                    del h[s[left]]
                left+=1
            maxi=max(maxi,right-left+1)
            right+=1
        return maxi
