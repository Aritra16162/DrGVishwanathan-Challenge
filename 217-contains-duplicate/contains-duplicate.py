class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            if len(set(nums)) != len(nums):
                return True
            else:
                return False