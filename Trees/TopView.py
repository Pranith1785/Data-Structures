class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.hd = 0

### Method 1 
def topView(root):
    if root is None:
        return 
    val,hd,q = dict(), 0 ,[]
    q.append(root)

    while(len(q)):
        root = q[0]
        hd = root.hd
        if hd not in val:
            val[hd] = root.data
        if root.left :
            root.left.hd = hd -1
            q.append(root.left)
        if root.right :
            root.right.hd = hd + 1
            q.append(root.right)
        q.pop(0)

    for i in sorted(val):
        print(val[i],end=" ")


## Method 2
def addTopNode(root,l,r,val):
    
    if root == None:
        return
    if l not in val:
        val[l] = [root.data,r]
    elif val[l][1] > r:
        val[l] = [root.data,r]
    addTopNode(root.left,l-1,r+1,val)
    addTopNode(root.right,l+1,r+1,val)


def topView2(root):

    val = {}
    addTopNode(root,0,0,val)
    for i in sorted(val):
        print(val[i][0],end=" ")
    print(" ")

### create a Tree

root =  Node(4)
root.left = Node(3)
root.left.right = Node(2)
root.left.left = Node(5)

root.right = Node(7)
root.right.left = Node(1)
root.right.right = Node(8)

#####
print("First method : ")
topView(root)

print("Second Method :")
topView2(root)
