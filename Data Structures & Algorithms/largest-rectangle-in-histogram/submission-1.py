class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        maxi=0
        n=len(heights)
        for i in range(len(heights)):
            while st and heights[st[-1]]>heights[i]:
                h=heights[st.pop()]
                if st:
                    width=i-st[-1]-1
                else:
                    width=i
                maxi=max(maxi,h*width)
            st.append(i)
        while st:
            h=heights[st.pop()]
            if st:
                width=n-st[-1]-1
            else:
                width=n
            maxi=max(maxi,h*width)
        return maxi