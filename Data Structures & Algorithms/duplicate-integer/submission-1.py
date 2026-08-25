from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=Counter(nums)
        for i,j in a.items():
            if j>1:
                return True
                break
        else:
            return False
       