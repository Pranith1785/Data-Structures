
class Queue():

    def __init__(self):
        self.qu = []
        self.front = None
        self.rear = None
        self.size = 0

    ## Adding element to start
    def enQueue(self,data):
        self.qu.append(data)
        if self.front is None:
            self.front = 0
            self.rear = 0
        else:
            self.rear = self.size
        self.size += 1

    ## Removes the element from last
    def deQueue(self):

        self.qu.pop(0)
        self.size -= 1
        if self.size >0:
            self.rear -= 1
        else:
            self.front = None
            self.rear = None

    def getFirst(self):
        return self.qu[self.front]

    def getLast(self):
        return self.qu[self.rear]
        

q = Queue()
q.enQueue(3)
q.enQueue(4)
print(q.getFirst())
q.deQueue()
print(q.getFirst())