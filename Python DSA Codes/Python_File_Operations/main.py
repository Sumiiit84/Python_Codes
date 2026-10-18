'''
with open('sample.txt', 'r') as f:
    print(f.readline())
    
'''
'''
with open('sample.txt', 'w') as f:
    f.write('Welcome to the magical world')
with open('sample.txt', 'r') as f:
    print(f.read())
'''
'''
with open('sample.txt', 'r') as f:
    count = 0
    content = f.read()
    content.split()
    for i in range(len(content)):
        count += 1
    print('Total characters are :- ' , count)
'''


