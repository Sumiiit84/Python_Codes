# 5
# 1 + 2 + 3 + 4 + 5 = 15

n = int(input("Enter a Size :- "))
arr = []
sum = 0
print(f"Enter a {n} size elements")
for i in range(n):
    num = int(input())
    arr.append(num)

for i in arr:
    sum += i 
    
    
print(f"sum of is :- {sum}")
