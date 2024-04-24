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
    tail=head
    while tail.next!=None:
        tail=tail.next
    curr = tail
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.prev 
    print()

def addNodeAtTailOfLinkedList(head,val):
     newBlock=Node(val)
     if head==newBlock:
         return newBlock
     tail=head
     while tail.next!=None:
         tail=tail.next
         tail.next=newBlock
         newBlock.prev=tail
         return head
         
obj1 = Node(121)
obj2 = Node(145)
obj3 = Node(678)
obj4 = Node(89)
obj5 = Node(12)

# links establishments
obj1.next = obj2 
obj2.prev = obj1 
 
obj2.next = obj3 
obj3.prev = obj2 
 
obj3.next = obj4 
obj4.prev = obj3 
 
obj4.next = obj5 
obj5.prev = obj4 
 
printLeftToRightManner(obj1)
printRightToLeftManner(obj5)