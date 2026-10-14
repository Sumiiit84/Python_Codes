n = int(input("Enter a Number :- "))
flag = 0
for i in range(2 , (n // 2) + 1):
    if n % i == 0:
        flag = 1
        break

if flag == 0:
    print(f"Prime Number {n}")
else:
    print(f"Not Prime Number {n}")
    
    