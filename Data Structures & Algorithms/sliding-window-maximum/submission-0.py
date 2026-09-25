from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq=deque()
        l=[]
        for i in range(len(nums)):
            while dq and i-dq[0]>=k:
                dq.popleft()
            while dq and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                l.append(nums[dq[0]])
        return l

                
        