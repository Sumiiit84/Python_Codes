#Double Lincked List
#Create a Node where 3 Cloumns we want prev, data , next
class Node:
    def __init__(self, data = None):
        self.prev = None
        self.data = data
        self.next = None
        
# after creating a Node create a Doubly LL
class DoublyLL:
    def __init__(self):
        self.head = None
        
    def insertAtEnd(self, data):
        temp = Node(data)
        if(self.head == None):
            self.head = temp
            return
        else:
            t = self.head
            while(t.next != None):
                t = t.next
                
            t.next = temp
            temp.prev = t 
            
    def insertAtBeg(self, data):
        temp = Node(data)
        if(self.head == None):
            self.head = temp
            return
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
    
    def insertAtmid(self, data, x):
        t = self.head
        while(t.next != None):
            if(t.data == x):
                break
            else:
                t = t.next
        temp = Node(data)
        n = t.next   #30
        temp.next = n
        t.next = temp
        
    def delete(self, data):
        # check LL is empty or not
        if(self.head == None):
            print("DLL is Emplty")
            return
        temp = self.head
        # check for a data in first node
        if(temp.data == data):
            self.head = temp.next
            self.head.prev = None
            return
            
        while(temp.next != None):
            if(temp.data == data):
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                return
            else:
                temp = temp.next
        if(temp.data == data):
            temp.prev.next = None
            
                
    def printDLL(self):
        t = self.head
        while(t.next != None):
            print(t.data , end=" <--> ")
            t = t.next
        print(t.data)  
        
  
        
obj = DoublyLL() 
obj.insertAtEnd(1)
obj.insertAtEnd(2)
obj.insertAtEnd(3)
obj.insertAtEnd(4)
obj.insertAtEnd(5)
obj.delete(5)
obj.printDLL()   