class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            s=target-nums[i]
            if s in h:
                return [h[s],i]
                break
            h[nums[i]]=i

        