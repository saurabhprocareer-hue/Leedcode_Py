class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longLen = 0
        strLen = len(s)
        idxMp = {}
        i=0

        for j in range(strLen):
            if s[j] in idxMp:
                i = max(idxMp[s[j]], i)

            longLen = max(longLen, j - i + 1)
            idxMp[s[j]] = j +1



        
        return longLen