class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l_1 = len(word1)
        l_2 = len(word2)
        new_word = ""
        if l_1 > l_2:
            loop_count = l_2
            i = 0
            while i < loop_count:
                new_word += word1[i]
                new_word += word2[i]
                i += 1
            return new_word + word1[i:]
        else:
            loop_count = l_1
            i = 0
            while i < loop_count:
                new_word += word1[i]
                new_word += word2[i]
                i += 1
            return new_word + word2[i:]

                

x = Solution()
print(x.mergeAlternately("abc", "pq"))
        