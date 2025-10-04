#Problem: https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = []
        repeated = set()
        for c in s:
            if c in repeated:
                continue
            if c in chars:
                chars.remove(c)
                repeated.add(c)
            else:
                chars.append(c)
        
        if chars:
            return s.index(chars[0])
        else:
            return -1
        