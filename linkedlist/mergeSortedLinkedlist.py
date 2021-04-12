
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None

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


def mergeLinkedList(l1, l2):

    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data <= l2.data:
        temp = l1
        temp.next = mergeLinkedList(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeLinkedList(l1, l2.next)
    return temp


def mergeLinkedList1(l1, l2):

    if l1 is None:
        return(l2)
    if l2 is None:
        return l1

    if l1.data <= l2.data:
        temp = l1
        l1 = l1.next
    else:
        temp = l2
        l2 = l2.next

    l3 = temp

    while True:
        if l1 is None:
            temp.next = l2
            break
        if l2 is None:
            temp.next = l1
            break

        if l1.data <= l2.data:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next

        temp = temp.next
    return l3


l1 = LinkedList()
l1.append(10)
l1.append(33)

l2 = LinkedList()
l2.append(1)
l2.append(2)
l2.append(8)
l2.append(10)
l2.append(15)


#print(compareLists(l1.head, l2.head))

l3 = mergeLinkedList1(l1.head, l2.head)

temp = l3
while(temp is not None):
    print(temp.data)
    temp = temp.next
