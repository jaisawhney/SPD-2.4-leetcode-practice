class Solution(object):
    def isValid(self, s):
        """
        Question:
        The problem is to determine if a string of parenthesis variants are valid
        Valid, meaning that each opening parenthesis has a matching closing parenthesis
        and that parenthesis are closed in order

        Pseudocode:
        Create a stack to hold seen parenthesis
        Create a hash map to map the closing parenthesis to the opening one

        Iterate over the characters in s
            If character is in the hash map, it must be an opening one, append to the end of stack
            Otherwise, remove from the end of the stack and check if the removed item equals the current character
        Return true if the length of the stack equals zero
        """

        stack = []
        hash_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for char in s:
            if char in hash_map:
                stack.append(char)
            elif not stack or char != hash_map[stack.pop()]:
                return False

        return len(stack) == 0
