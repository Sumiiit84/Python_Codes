#create a Queue 
class Queue:
    def __init__(self):
        self.data = []     #make a empty list first assign
        
    def isEmpty(self):
        if(len(self.data) == 0):
            print('Queue is Empty')   #Chefck if Queue is Empty
            return
            
    def insert(self, val):
        self.data.append(val)
    
    def delete(self):
        if(self.isEmpty()):
            print('Queue is Empty')
        else:
            return self.data.pop(0)
    

obj = Queue()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.isEmpty()
print(obj.delete())
print(obj.delete())