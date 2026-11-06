class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        main_iter = iter(t)

        return all(char in main_iter for char in s)