class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_parentheses = {'{': '}', '[': ']', '(': ')'}

        for c in s:
            if c in valid_parentheses:
                stack.append(c)
            elif (not stack) or (c != valid_parentheses[stack.pop()]):
                return False

        return not stack
