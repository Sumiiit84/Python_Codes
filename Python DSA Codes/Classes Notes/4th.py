
n = int(input("Enter a Size :- "))
arr = []

print(f"Enter a {n} size elements")
for i in range(n):
    num = int(input())
    arr.append(num)
    
target = int(input("WHich Number you want to search :- "))
msg = 'Not available eroor'
pos = -1
for i in range(len(arr)):
    if(target == arr[i]):
        pos = i


if(pos == -1):
    print(msg)
else:
    print(pos)
    