class Solution:
    def solveEquation(self, equation: str) -> str:
        q = [0] * 2
        sign, flag, num = 1, 1, 0
        for i, ch in enumerate(equation):
            if ch == '=':
                q[1] = q[1] + num * flag * sign
                sign, flag, num = -1, 1, 0
            elif ch == 'x':
                if i > 0 and equation[i - 1] == '0':
                    continue
                q[0] = q[0] + 1 * sign * flag if not num else q[0] + num * sign * flag
                num = 0
            elif ch == '+' or ch == '-':
                q[1] = q[1] + num * flag * sign
                num = 0
                flag = 1 if ch == '+' else -1
            else:
                num = num * 10 + int(ch)

        if num:
            q[1] = q[1] + num * flag * sign
        if not q[0]:
            if not q[1]:
                return "Infinite solutions"
            return "No solution"

        q[1] = q[1] / q[0]
        if q[1] == int(q[1]):
            q[1] = int(q[1])
        return "x=" + str(-q[1])


solution = Solution()
print(solution.solveEquation("1+1=x"))
