class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 
 
def printLeftToRightManner(head):
    print("Left to Right")
    curr = head 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(head):
    print("Right to Left")
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.prev 
    print()
 
def addNodeAtTailOfLinkedList(head, val):
    newBlock = Node(val)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
        tail.next = newBlock 
 
    newBlock.prev = tail 
    return head
 
 
def addNodeAtHeadOfLinkedList(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    newBlock.next = head 
    head.prev = newBlock 
    return newBlock
 
def insertAtSpecificPosition(head, val, position):
    newBlock = Node(val)
    if head == None:
        return newBlock
 
    index = 1 
    curr = head 
 
    while index != position - 1:
        index += 1 
        curr = curr.next 
    nextNode = curr.next 
   
    newBlock.next = nextNode 
    nextNode.prev = newBlock 
    curr.next = newBlock 
    newBlock.prev = curr 
    return head 
l = [11, 22, 33, 44, 55, 66, 77]
head = None 
for ele in l:
    head = addNodeAtHeadOfLinkedList(head, ele)
 
printLeftToRightManner(head)
printRightToLeftManner(head)   
 
head = insertAtSpecificPosition(head, 12222, 3)
 
printLeftToRightManner(head)
printRightToLeftManner(head)    

