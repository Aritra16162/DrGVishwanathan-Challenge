class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n = set(ransomNote)
        m = set(magazine)

        for char in n:
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True