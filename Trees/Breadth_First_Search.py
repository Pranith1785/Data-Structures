
## Level Order Traversal or Breadth First Search
from collections import deque

class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree():

    def __init__(self):
        self.root = None
    
    def insertLeaf(self,data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left :
                        current = current.left
                    else:
                        current.left = new_node
                        break
                else:
                    if current.right :
                        current = current.right
                    else:
                        current.right = new_node
                        break


## Level Order Traversal or Breadth First Search
### Method 1 : using list
def bfs(root):
    
    if root is None:
        return 
    ##Create empty list or queue
    queue = []
    queue.append(root)
    while(len(queue)>0):
        print(queue[0].data,end=" ")
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def bfs1(root):
    
    if root is None:
        return 
    ##Create empty list or queue
    queue = deque()
    queue.append(root)
    while(len(queue)>0):
        node = queue.popleft()
        print(node.data,end=" ")
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


## Created a Tree
tree = BinaryTree()

arr = [1,2,5,3,4,6]

for i in range(len(arr)):
    tree.insertLeaf(arr[i])

print(bfs(tree.root))
print(bfs1(tree.root))

