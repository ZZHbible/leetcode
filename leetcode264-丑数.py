
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        from queue import PriorityQueue
        q=PriorityQueue()
        q.put(1)
        s=set()
        s.add(1)
        n-=1
        while(n > 0):
            n-=1
            out=q.get()
            if out*2 not in s:
                s.add(out*2)
                q.put(out*2)
            if out*3 not in s:
                s.add(out*3)
                q.put(out*3)
            if out*5 not in s:
                s.add(out*5)
                q.put(out*5)
        return q.get()

solution=Solution()
print(solution.nthUglyNumber(11))