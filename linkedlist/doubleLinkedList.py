
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList():

    def __init__(self):
        self.head = None
        print("DL created")

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def append(self, new_data):
        new_node = Node(data=new_data)

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return()

        temp = self.head
        while(temp.next is not None):
            print(temp.data)
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def reverse(self):
        temp = None
        curr = self.head

        while curr != None:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp != None:
            self.head = temp.prev

    def insertNode(self, new_data):
        '''sorted insert of data'''

        new_node = Node(data=new_data)

        if self.head is None:
            self.head = new_node
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            curr = self.head
            while(curr.next != None):
                if (curr.data < new_node.data and curr.next.data >= new_node.data):
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                    new_node.prev = curr
                    return
                else:
                    curr = curr.next
            else:
                curr.next = new_node
                new_node.prev = curr


dl = DoubleLinkedList()

dl.insertNode(3)
dl.insertNode(1)
dl.insertNode(2)
dl.insertNode(5)

temp = dl.head
while temp is not None:
    print(temp.data)
    temp = temp.next

dl.reverse()

