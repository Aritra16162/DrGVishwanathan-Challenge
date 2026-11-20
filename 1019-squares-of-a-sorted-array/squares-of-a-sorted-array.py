class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]**2
            sorted_array = sorted(nums)
        return sorted_array
        