class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def enQueue(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock 
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = newBlock
    return head
 
def deQueue(head):
    if head == None:
        print("Queue is empty, nothing to delete")
        return None
 
    print("Deleting", head.data)
    secondNode = head.next 
    head.next = None 
    return secondNode
 
def printQueue(head):
    if head == None:
        print("Queue is empty")
        return 
    curr = head 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
head = None 
head = enQueue(head, 10)
head = enQueue(head, 20)
head = enQueue(head, 100)
 
printQueue(head)

 
head = deQueue(head)

 
printQueue(head)
 
head = deQueue(head)
printQueue(head)
head = deQueue(head)
printQueue(head)
head = deQueue(head)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
