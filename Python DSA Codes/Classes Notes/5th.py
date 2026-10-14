
n = int(input("Enter a Size :- "))
arr = []

print(f"Enter a {n} size elements")
for i in range(n):
    num = int(input())
    arr.append(num)
    
reversed = arr[::-1]
print(reversed)