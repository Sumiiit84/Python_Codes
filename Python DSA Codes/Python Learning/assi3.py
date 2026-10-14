
for i in range(1 , 5):
    for j in range(i):
        if(i == 1 or i == 3):
            print('*' , end='')
        elif(i == 2 or i == 4):
            print('#' , end='')
    print()