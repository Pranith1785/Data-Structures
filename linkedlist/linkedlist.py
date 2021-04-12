
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

    def push(self, newdata):
        '''
        Insert node at beginning
        '''
        new_node = Node(newdata)
        new_node.next = self.head
        self.head = new_node

    def insertNode(self, prev_node, new_data):

        if prev_node is None:
            return("Not able to insert")

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node.next

    def append(self, new_data):
        '''
        Adding new data at the end of Linkedlist
        '''
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return("added at beginning")

        temp = self.head
        while(temp.next):
            temp = temp.next

        temp.next = new_node

    def printList(self):
        '''Prints the list of values in linked list'''
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def getLength(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count

    def insertNodeAtPosition(self, position, data):
        new_node = Node(data)
        temp = self.head
        for _ in range(position-1):
            temp = temp.next
        prev = temp.next
        temp.next = new_node
        new_node.next = prev

    def deletelist(self):
        current = self.head
        while current:
            prev = current.next
            print("delete : ", current.data)
            del current.data
            current = prev

    def deleteNode(self, keyValue):

        temp = self.head

        if temp.head:
            if temp.data == keyValue:
                self.head = temp.next
                temp = None
                return()

        while(temp):
            if temp.data == keyValue:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None


def compareLists(l1, l2):

    while(l1 is not None and l2 is not None):
        if l1.data != l2.data:
            return False
        l1 = l1.next
        l2 = l2.next

    if l1 is not None:
        return False

    if l2 is not None:
        return False

    return True


l1 = LinkedList()
l1.append(10)
l1.append(33)

l2 = LinkedList()
l2.append(1)
l2.append(2)
l2.append(8)
l2.append(10)
l2.append(15)


print(compareLists(l1.head, l2.head))
