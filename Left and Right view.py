class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
 
 
def printPreOrder(root):
    if root == None:
        return
 
    print(root.data, end = " ")
    printPreOrder(root.left)
    printPreOrder(root.right)
 
def printInOrder(root):
    if root == None:
        return
 
 
    printInOrder(root.left)
    print(root.data, end = " ")
    printInOrder(root.right) 
 
def printPostOrder(root):
    if root == None:
        return

 
    printPostOrder(root.left)
    printPostOrder(root.right) 
    print(root.data, end = " ")
 
 
def printLevelOrder(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
    
            curr = Q.pop(0)
            subResult.append(curr.data)
 
            if curr.left != None:
                Q.append(curr.left)
 
            if curr.right != None:
                Q.append(curr.right)
 
        result.append(subResult)
 
    for subLevel in result:
        print(*subLevel)
 
def printZigZagLevelOrder(root):
    result = []
    Q = [root]
    level = 0 
 
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            curr = Q.pop(0)
            subResult.append(curr.data)
 
            if curr.left != None:
                Q.append(curr.left)
 
            if curr.right != None:
                Q.append(curr.right)
 
        if level % 2 == 1:
            subResult = subResult[::-1]
 
        result.append(subResult)
        level += 1 
 
    for subLevel in result:
        print(*subLevel) 
 
 
def leftViewOfBinaryTree(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            curr = Q.pop(0)
            if i == 0:
                result.append(curr.data)
 
            if curr.left != None:
                Q.append(curr.left)
 
            if curr.right != None:
                Q.append(curr.right)
 
    print("Left view is:")
    print(result)
 
 
 
def rightViewOfBinaryTree(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            curr = Q.pop(0)
            if i == n - 1:
                result.append(curr.data)
 
            if curr.left != None:
                Q.append(curr.left)
 
            if curr.right != None:
                Q.append(curr.right)
 
    print("Right view is:")
    print(result)
 
root = TreeNode(18)
obj2 = TreeNode(15)
obj3 = TreeNode(20)
obj4 = TreeNode(25)
obj5 = TreeNode(30)
obj6 = TreeNode(45)
obj7 = TreeNode(80)
 
root.left = obj2 
root.right = obj3 
 
obj2.left = obj4 
obj2.right = obj5 
 
obj3.left = obj6 
obj3.right = obj7
leftViewOfBinaryTree(root)
rightViewOfBinaryTree(root)
