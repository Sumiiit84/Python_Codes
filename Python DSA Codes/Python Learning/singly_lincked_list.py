class Node:
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
        
class LinckedList:
    def __init__(self, head = None):
        self.head = head
        
    def insert_end(self, data):
        temp = Node(data)
        
        if(self.head == None):
            self.head = temp
            return
            
        t1 = self.head

        while(t1.next != None):
            t1 = t1.next
        t1.next = temp
    
    def insertAtBeg(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp
    
    def printLL(self):
        t1 = self.head
        
        while(t1 != None):
            print(t1.data)
            t1 = t1.next
            
obj = LinckedList()
obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)
obj.insertAtBeg(5)
obj.printLL()
                   
        
        