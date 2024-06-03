class Node:
     #node creation
    def __init__(self,data):
        self.data=data
        self.pointer= None

class LinkedList:
     #head node cretion
    def __init__(self):
        self.head=None
     #by add() adding each node to the head node   
    def add(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head= newNode
        else:
            cur = self.head
            while(cur.pointer is not None):
                cur = cur.pointer
            cur.pointer = newNode
    #print()
    def print(self):
        cur = self.head
        while(cur is not None):
            print(cur.data,end=" ")
            cur = cur.pointer
        print()#newline
    #remove()
    def remove(self,data):
        if(self.head is not None):
            if(self.head.data==data):
                self.head=self.head.pointer
            else:
                cur = self.head
                while(cur.pointer is not None and cur.pointer.data != data):
                    cur = cur.pointer
                if cur.pointer is not None:
                    cur.pointer = cur.pointer.pointer
                else:
                    print(data,"is not present in the Linkedlist")
        else:
            print("Linked list is empty")

linkedList= LinkedList()
linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.print()
linkedList.remove(3)
linkedList.print()

    
