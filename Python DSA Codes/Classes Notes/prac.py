
n = int(input("Enter a Size :- "))
arr = []

print(f"Enter a {n} size elements")
for i in range(n):
    num = int(input())
    arr.append(num)

for i in range(len(arr)):
    if(arr[i] == 0 and arr[i+1] != 0):
        ans = [arr[i+1] , arr[i] ]

print(ans)