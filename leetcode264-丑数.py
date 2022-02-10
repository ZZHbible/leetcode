class Solution:
    def nthUglyNumber(self, n: int) -> int:
        from queue import PriorityQueue
        q = PriorityQueue()
        q.put(1)
        s = set()
        s.add(1)
        n -= 1
        while (n > 0):
            n -= 1
            out = q.get()
            if out * 2 not in s:
                s.add(out * 2)
                q.put(out * 2)
            if out * 3 not in s:
                s.add(out * 3)
                q.put(out * 3)
            if out * 5 not in s:
                s.add(out * 5)
                q.put(out * 5)
        return q.get()

    def nthUglyNumber_dp(self, n: int) -> int:
        dp = [1] * (n + 1)
        dp2, dp3, dp5 = 0, 0, 0
        for i in range(1, n + 1):
            num1, num2, num3 = dp[dp2] * 2, dp[dp3] * 3, dp[dp5] * 5
            dp[i] = min(num1, num2, num3)
            if dp[i] == num1:
                dp2 += 1
            if dp[i] == num2:
                dp3 += 1
            if dp[i] == num3:
                dp5 += 1
        return dp[n - 1]


solution = Solution()
print(solution.nthUglyNumber_dp(10))
