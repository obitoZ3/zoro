class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

obj1=Node(20)
obj2=Node(30)
obj3=Node(40)
obj4=Node(50)
obj5=Node(60)
obj6=Node(70)
obj7=Node(80)
obj8=Node(90)
obj9=Node(100)
obj10=Node(110)


obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
obj7.next=obj8
obj8.next=obj9
obj9.next=obj10


curr=obj1
while curr!=None:
    print(curr.data,end="-->")
    curr=curr.next
