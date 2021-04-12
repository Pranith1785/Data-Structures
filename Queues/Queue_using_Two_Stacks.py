
##Also refer to queues.py file for queues implementation using cyclic linked list
## Below using two stacks
class Queue():

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enQueue(self,data):
        self.s1.append(data)
    
    def deQueue(self):
        if not self.s2 :
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return(self.s2.pop())

    def getFirst(self):
        if self.s2:
            return self.s2[-1]
        else:
            return self.s1[0]


q = Queue()
for _ in range(10):
    a = list(map(int,input().split()))
    if a[0] == 1:
        q.enQueue(a[1])
    elif a[0] == 2:
        q.deQueue()
    else:
        print(q.getFirst())
