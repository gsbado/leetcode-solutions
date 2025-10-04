#Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        countNumbers = []

        for num in nums:
            if num not in countNumbers:
                countNumbers.append(num)

        k = len(countNumbers)

        for i in range (k):
            nums[i] = countNumbers[i]
            
        return k
