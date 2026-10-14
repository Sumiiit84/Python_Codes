n = 7

for i in range(0 , n):
    for j in range(0 , n ):
        if(j == 3 or i == 3):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()