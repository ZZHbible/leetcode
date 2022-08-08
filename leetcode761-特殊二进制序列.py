class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s

        cnt = left = 0
        subs = list()

        for i, ch in enumerate(s):
            if ch == "1":
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    subs.append("1" + self.makeLargestSpecial(s[left + 1:i]) + "0")  # 内部特殊子串排序
                    left = i + 1

        subs.sort(reverse=True)
        return "".join(subs)


solution = Solution()
solution.makeLargestSpecial("11011000")
