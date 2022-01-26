class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def iab(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def ian(self,pos,data):
        if self.head == None:
            self.head = Node(data)
            return
        pos = pos - 2
        temp = self.head
        newNode = Node(data)
        while(pos!=0):
            temp = temp.next
            pos = pos - 1
        newNode.next = temp.next
        temp.next  = newNode
    def iae(self,data):
        newNode = Node(data)
        temp =self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next = newNode
    def print(self):
        temp = self.head
        while(temp!=None):
            print(temp.data,"->",end=" ")
            temp = temp.next
        print()
    def delete(self,data):
        if self.head==None:
            return
        temp = self.head
        if temp.data==data:
            self.head = temp.next
            temp.next = None
            return
        while(temp.next.data!=data):
            temp = temp.next
        if temp.next.next==None:
            temp.next = None
            return
        temp.next = temp.next.next
        
ll = LinkedList()
ll.iab(4)
ll.iab(2)
ll.iab(1)
ll.print()
ll.ian(3,3)
ll.iae(5)
ll.print()
ll.delete(3)
ll.print()
        
            
      