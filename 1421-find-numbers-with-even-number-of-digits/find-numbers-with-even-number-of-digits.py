class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        # done by aritra
        total_nums = 0 
        for i in range(len(nums)):
            current_nums = nums[i]
            digits = 0

            while current_nums > 0 :
                digits += 1
                current_nums //=10
            
            if digits %2 == 0 :
                total_nums += 1
        return total_nums