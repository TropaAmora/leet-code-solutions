class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ""
        i = s[::-1]
        dp = [[False] * len(s)  for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            substring = s[i]

        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[j]:
                    dp[i][j] = True

        

        return dp