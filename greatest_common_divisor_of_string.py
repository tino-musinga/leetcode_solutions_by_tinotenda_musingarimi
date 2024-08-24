class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l_1 = len(str1)
        l_2 = len(str2)
        if l_1 > l_2:
            if str2 in str1:
                return str1[l_2:]
            else:
                return ""
        else:
            if str1 in str2:
                return str2[l_1:]
            else:
                return ""
            
x = Solution()
print(x.gcdOfStrings("ABC", "ABCAB"))