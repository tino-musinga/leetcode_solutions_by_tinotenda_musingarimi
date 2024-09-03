class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s_word1 = set(word1)
        s_word2 = set(word2)
        dict1 = {}
        dict2 = {}
        lis1 = []
        lis2 = []
        if len(word1) != len(word2):
            return False
        if s_word1 != s_word2:
            return False
        for i in word1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        print(dict1)
        for j in word2:
            if j in dict2:
                dict2[j] += 1
            else:
                dict2[j] = 1
        print(dict2)
        for k in dict1:
            if dict1[k] != dict2[k]:
                lis1.append((k, dict1[k]))
                lis2.append(dict2[k])
        
        for x in lis1:
            current_value = x[1]
            if current_value in lis2:
                lis2.remove(current_value)
            else:
                return False
        if not lis2:
            return True


x = Solution()
word1 = "cabbba"
word2 = "abbccc"
print(x.closeStrings(word1, word2))

        
        