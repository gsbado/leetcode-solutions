#Problem: https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap_m = {}

        for char in magazine:
            if char in hashmap_m:
                hashmap_m[char] += 1
            else:
                hashmap_m[char] = 1

        for char in ransomNote:
            if char not in hashmap_m or hashmap_m[char] == 0:
                return False
            else:
                hashmap_m[char] -= 1

        return True