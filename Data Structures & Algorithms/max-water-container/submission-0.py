class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxi=0
        while left<right:
            a=min(heights[left],heights[right])
            width=right-left
            maxi=max(maxi,a*width)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxi