class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        highest = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= highest:
                result.append(True)
            else:
                result.append(False)
        return result
    
x = Solution()
candies = [2,3,5,1,3]
extra_candies = 3
print(x.kidsWithCandies(candies, extra_candies))