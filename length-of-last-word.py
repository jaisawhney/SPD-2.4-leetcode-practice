class Solution(object):
    def lengthOfLastWord(self, s):
        """
        Given a string s consisting of words and spaces, return the length of the last word in the string.

        Pseudocode:
        If the interviewer allows the use of built-in methods, we can do the following

        First, handle if the string doesn't exist or is a space
            If it is, return 0

        Otherwise, split the string into a list and return the length of the last word, which is located at index [-1]
        """

        if not s or s == " ":
            return 0
        return len(s.split()[-1])