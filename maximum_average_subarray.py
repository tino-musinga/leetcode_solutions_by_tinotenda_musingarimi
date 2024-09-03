class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        highest = sum(nums[:k])/k
        print(highest)
        for i in range(len(nums) - k+1):
            current = sum(nums[i:i+k])/k
            if current > highest:
                highest = current
        return highest
    
x = Solution()
#num = [1,12,-5,-6,50,3]
nm = [0,1,1,3,3]
print(x.findMaxAverage(nm, 4))

        