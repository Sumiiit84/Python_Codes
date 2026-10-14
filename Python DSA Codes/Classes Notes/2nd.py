
n = int(input("Enter a Size :- "))
arr = []

print(f"Enter a {n} size elements")
for i in range(n):
    num = int(input())
    arr.append(num)
    
large = arr[0]
second_large = arr[0]

small = arr[0]
second_small = arr[0]

for num in arr:
    if num > large:
        second_large = large
        large = num

    elif num > second_large and num != large:
        second_large = num

    if num < small:
        second_small = small
        small = num

    elif num < second_small and num != small:
        second_small = num
    
        
    

    
print(f"Large Element :- {large}")
print(f"Second Large Elment :- {second_large}")
print(f"SMallest Element :- {small}")
print(f"Second Smallest Element :- {second_small}")

    