class Solution(object):
    def isValid(self, s):
        stack = []
        dic = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in dic.values():
                stack.append(char)
            elif char in dic:
                if not stack or stack[-1] != dic[char]:
                    return False
                stack.pop()
            else:
                return False

        return not stack
