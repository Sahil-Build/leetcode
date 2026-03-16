1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen={}
4        for i,num in enumerate(nums):
5            diff=target-num
6            if diff in seen:
7                return [seen[diff],i]
8            seen[num]=i
9            
10        