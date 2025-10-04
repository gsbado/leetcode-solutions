#Problem: https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_mapping = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        stack = []

        for char in s:
            if char in parentheses_mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if parentheses_mapping[top] != char:
                    return False
        return not stack