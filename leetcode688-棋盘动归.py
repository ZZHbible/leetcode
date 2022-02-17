class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0] * n for i in range(n)] for j in range(k + 1)]
        for i in range(n):
            for j in range(n):
                dp[0][i][j] = 1
        directions = [[-1, 2], [-1, -2], [-2, 1], [-2, -1], [1, 2], [1, -2], [2, 1], [2, -1]]
        for step in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for direction in directions:
                        if i + direction[0] >= 0 and i + direction[0] < n and j + direction[1] >= 0 and j + direction[
                            1] < n:
                            dp[step][i][j] += 1 / 8 * dp[step - 1][i + direction[0]][j + direction[1]]

        return dp[k][row][column]


solution = Solution()
print(solution.knightProbability(3, 2, 0, 0))
