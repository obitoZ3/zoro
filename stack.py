class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
 
 
 
def push(top, value):
    print(value, " is getting inserted")
    newBlock = Node(value)
    if top == None:
        return newBlock
 
    newBlock.next = top 
    return newBlock
 
 
def pop(top):
    if top == None:
        print("Nothing to delete")
        return
 
    print(top.data, " is getting deleted")
    secondNode = top.next 
    top.next = None 
    return secondNode
 
 
def printStack(top):
    if top == None:
        print("Stack is empty")
        return 
    curr = top 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
 
top = None 
top = push(top, 12)
top = push(top, 15)
top = push(top, 16)
top = push(top, 22)
top = push(top, 234)
top = push(top, 10)
 
printStack(top)
 
top = pop(top)
printStack(top)
 
top = pop(top)
printStack(top)
 
top = pop(top)
printStack(top)
 
top = pop(top)
printStack(top)
 
top = pop(top)
printStack(top)
 
top = pop(top)
printStack(top)
 
top = pop(top)
printStack(top)
 
# 10 --> 234 --> 22 --> 16 --> 15 --> 12 --> None  
 
 
 
 
 
 