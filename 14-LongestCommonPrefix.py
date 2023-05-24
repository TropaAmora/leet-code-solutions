from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        mini = 201
        conti = False
        for word in strs:
            if len(word) < mini:
                mini = len(word)
        
        for i in range(mini):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    conti = True
                    break
            if conti == False:
                lcp += strs[j][i]
        return lcp