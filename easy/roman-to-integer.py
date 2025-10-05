#Problem: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        roman_mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in range(len(s)):
            if i < len(s) - 1 and roman_mapping[s[i]] < roman_mapping[s[i+1]]:
                number -= roman_mapping[s[i]]
            else:
                number += roman_mapping[s[i]]
        
        return number