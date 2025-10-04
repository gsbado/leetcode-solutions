#Problem: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        validChar = []
        for c in s:
            if ('a' <= c.lower() <= 'z') or ('0' <= c <= '9'):
                validChar.append(c.lower())
        s = ''.join(validChar)
        return s == s[::-1]