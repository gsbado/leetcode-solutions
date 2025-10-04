#Problem: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexList = {}
        i = 0
        for num in nums:
            item = target - num
            if item in indexList:
                return [indexList[item],i]
            indexList[num] = i
            i += 1
        return []