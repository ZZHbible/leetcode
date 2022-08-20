class MyCircularQueue:

    def __init__(self, k: int):
        self.k=k+1
        self.l=[-1]*(k+1) # 用比原队列大小+1，来方便判断队列空与满
        self.head=0
        self.tail=0


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.l[self.tail]=value
        self.tail=(self.tail+1)%self.k
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head=(self.head+1)%self.k
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[self.head]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.l[self.tail-1]


    def isEmpty(self) -> bool:
        return self.tail==self.head


    def isFull(self) -> bool:
        return (self.tail+1)%(self.k)==self.head