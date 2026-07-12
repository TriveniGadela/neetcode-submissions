class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h={}
        for i in nums:
            if i in h:
                return True
                break
            else:
                h[i]=h.get(i,0)+1
        else:
            return False

        