
for i in range(1 , 11):
    if(i % 2 != 0 ):
        j = 1
        while(j <= 10):
            print(f"{i} * {j} = {i * j}" , end = '\t')
            j += 1
        print()
    j = 0