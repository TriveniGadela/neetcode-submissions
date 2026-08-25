class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi=0
        h=set(nums)
        for i in h:
            if i-1 not in h:
                count=1
                current=i
                while current+1 in h:
                    current+=1
                    count+=1
                maxi=max(maxi,count)
        return maxi

        