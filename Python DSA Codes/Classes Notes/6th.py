
n = int(input("Enter a Size :- "))
arr = []

print(f"Enter a {n} size elements")
for i in range(n):
    num = int(input())
    arr.append(num)
    
ans = set()
for i in range(len(arr)):
    ans.add(arr[i])
print(ans)
