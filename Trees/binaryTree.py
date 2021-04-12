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

### left , root and right node
def inOrder(root):

    if root:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)


### first root, left and right node        
def preOrder(root):
    tr = []

    if root:
        tr.append(root.data)
        tr.extend(preOrder(root.left))
        tr.extend(preOrder(root.right))
    return tr

### Left, right and root node
def postOrder(root):

    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data,end=" ")

## Created a Tree
tree = BinaryTree()

arr = [2,4,6,3,1,8,4]

for i in range(len(arr)):
    tree.insertLeaf(arr[i])


print("InOrder : ")
inOrder(tree.root)
print("PreOrder : ",preOrder(tree.root))

print("PostOrder : ")
postOrder(tree.root)