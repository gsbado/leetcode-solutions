#Problem: https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        valid_nums1 = nums1[:m]
        allNums = valid_nums1 + nums2
        allNums.sort()
        for i in range(len(allNums)):
            nums1[i] = allNums[i]