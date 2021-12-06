class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s)):
            num = ord(s[i]) - ord('0')
            if i > 0:
                last = ord(s[i - 1]) - ord('0')
                if last == 0:
                    if num > 0 and num < 10:
                        dp[i + 1] = dp[i]
                    else:
                        return 0
                else:
                    temp = last * 10 + num
                    if num == 0:
                        if temp == 10 or temp == 20:
                            dp[i + 1] = dp[i - 1]
                        else:
                            return 0
                    else:
                        if temp <= 26:
                            dp[i + 1] = dp[i] + dp[i - 1]
                        else:
                            dp[i + 1] = dp[i]

            else:
                if num > 0 and num < 10:
                    dp[i + 1] = dp[i]
                else:
                    return 0

        return dp[len(s)]

solution=Solution()
print(solution.numDecodings("2101"))
