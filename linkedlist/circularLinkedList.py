

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList():
    def __init__(self):
        self.head = None

    def push(self, data):
        new_Node = Node(data)
        temp = self.head

        new_Node.next = self.head

        if self.head != None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_Node
        else:
            new_Node.next = new_Node

        self.head = new_Node

    def printList(self):

        temp = self.head
        if self.head != None:
            while(True):
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break


cl = CircularLinkedList()
cl.push(2)
cl.push(5)
cl.printList()
