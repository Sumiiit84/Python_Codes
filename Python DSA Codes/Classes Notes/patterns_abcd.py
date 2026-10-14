'''
A 
A B 
A B C 
A B C D 
A B C D E 
'''
'''
n = 5
for i in range(1 , n+1):
    for j in range(i):
        print(chr(65 + j) , end=" ")
    print()
'''

'''
A 
B B 
C C C 
D D D D 
E E E E E 
'''


'''
n = 5
for i in range(1 , n+1):
    for j in range(0 , i):
        print(chr(64 + i) , end= " ")
    print()
'''