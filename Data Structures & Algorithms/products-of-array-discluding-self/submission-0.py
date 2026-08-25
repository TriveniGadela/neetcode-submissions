class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[]
        po=1
        for i in nums:
            p.append(po)
            po=po*i
        s=1
        for i in range(len(nums)-1,-1,-1):
            p[i]=p[i]*s
            s=s*nums[i]
        return p
        