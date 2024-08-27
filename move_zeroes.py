class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] == 0:
                    if nums[j] != 0:
                        temp = nums[j]
                        nums[i] = temp
                        nums[j] = 0
                        
