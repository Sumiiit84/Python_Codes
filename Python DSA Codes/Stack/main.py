class Stack:
    def __init__(self):
        self.s = []
        
    def push(self , data):
        self.s.append(data)
    
    def length_of_stack(self):
        print('Length of Stack :- ' , len(self.s))
    
    def peek(self):
        print(self.s[-1])
        
    def pop(self):
        return self.s.pop(-1)
        
    def print(self):
        print(self.s)
        
obj = Stack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.print()
obj.length_of_stack()
obj.peek()
obj.pop()
obj.print()