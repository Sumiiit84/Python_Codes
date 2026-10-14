
n = int(input("Enter a Size :- "))
arr = []

print(f"Enter a {n} size elements")
for i in range(n):
    num = int(input())
    arr.append(num)

result = []

for i in arr:
    if i != 0:
        result.append(i)

for i in arr:
    if i == 0:
        result.append(i)

print(result)