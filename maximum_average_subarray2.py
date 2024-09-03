# class Solution:
#     def findMaxAverage(self, nums: list[int], k: int) -> float:
#         h_window = sum(nums[:k])
#         for i in range(1,len(nums)-k+1):
#             print("element is: ", nums[i])
#             c_window = h_window - nums[i-1] + nums[i+k-1]
#             if c_window > h_window:
#                 h_window = c_window
#         return h_window/k
    
# x = Solution()
# #num = [1,12,-5,-6,50,3]
# nm = [0,1,1,3,3]
# print(x.findMaxAverage(nm, 4))



