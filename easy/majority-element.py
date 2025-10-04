#Problem: https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countNumbers = {}
        for num in nums:
            if num in countNumbers:
                countNumbers[num] += 1
            else:
                countNumbers[num] = 1
            if countNumbers[num] > (len(nums)/2):
                return num
