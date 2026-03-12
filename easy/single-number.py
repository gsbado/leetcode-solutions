#Problem: https://leetcode.com/problems/single-number/
    
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        doubleNums = []
        singleNums = []

        for num in nums:
            if num not in singleNums:
                singleNums.append(num)
            elif num in singleNums:
                doubleNums.append(num)

        doubleNum = set(singleNums) - set(doubleNums)
        return doubleNum.pop()