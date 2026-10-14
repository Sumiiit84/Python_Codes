
n = int(input("Enter a Size :- "))
arr = []

print(f"Enter a {n} size elements")
for i in range(n):
    num = int(input())
    arr.append(num)
    
even_sum = 0
odd_sum = 0
for i in arr:
    if(i % 2 == 0):
        even_sum += 1
    else:
        odd_sum += 1
        
print("Even Count :- " , even_sum)
print("odd Count :- " , odd_sum)