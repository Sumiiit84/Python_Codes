# creating a node
class Node:
    def __init__(self, data , next = None):
        self.data = data
        self.next = next
        
class SLL:
    def __init__(self, head = None):
        self.head = head
        
    def append(self , data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            return
        t1 = self.head
        while(t1.next != None):
            t1 = t1.next
        
        t1.next = temp
        
            
    def prints(self):
        temp = self.head
        while(temp != None):
            print(temp.data , end=' -> ')
            temp = temp.next
        print('NONE')
            
obj = SLL()
obj.append(1)
obj.append(2)
obj.append(3)
obj.prints()