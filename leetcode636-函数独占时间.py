from typing import List
from collections import deque


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = deque()
        index = 0
        for log in logs:
            func, status, time = log.split(':')
            if status == 'start':
                if len(stack) > 0:
                    ans[stack[-1]] += (int(time) - index)
                stack.append(int(func))
                index = int(time)
            else:
                num = stack.pop()
                ans[num] += int(time) + 1 - index
                index = int(time) + 1
        return ans


solution = Solution()
print(solution.exclusiveTime(2, ["0:start:0", "0:start:2", "0:end:5", "1:start:7", "1:end:7", "0:end:8"]))
