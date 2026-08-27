class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(numbers)):
            s=target-numbers[i]
            if s in a:
                return [a[s],i+1]
            a[numbers[i]]=i+1
