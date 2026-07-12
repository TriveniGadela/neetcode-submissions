from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=Counter(nums)
        b=sorted(a.items(),key=lambda x: x[1],reverse=True)
        m=[]
        for i in range(k):
            m.append(b[i][0])
        return m
        