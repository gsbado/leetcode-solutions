#Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):
            j = 0 
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if j == m:
                return i
                
        return -1


#another solution using find:
#class Solution:
#    def strStr(self, haystack: str, needle: str) -> int:
#        return haystack.find(needle)
