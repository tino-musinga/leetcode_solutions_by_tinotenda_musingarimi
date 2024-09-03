class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        net_alt = [0]
        for i in gain:
            current = net_alt[-1] + i
            net_alt.append(current)
        return max(net_alt)
    
x = Solution()
gain = [-5,1,5,0,-7]
print(x.largestAltitude(gain))