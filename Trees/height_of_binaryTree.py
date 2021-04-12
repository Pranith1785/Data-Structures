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


### Height of binary Tree
## Number of nodes connected in longest chain => n-1 will be height of a tree

def heightBinaryTree(root):

    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return max(heightBinaryTree(root.left) + 1,heightBinaryTree(root.right)+1)
    

## number of nodes in longest chain
def height(root):

    if root is None:
        return 0
    else:
        return max(height(root.left),height(root.right)) + 1

## Created a Tree
tree = BinaryTree()

arr = [1,2,3]

for i in range(len(arr)):
    tree.insertLeaf(arr[i])


print(height(tree.root))
print(heightBinaryTree(tree.root))
