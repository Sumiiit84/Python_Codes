# Find max , Second max , min , second_min
arr = [10 , 3 , 45 , 6, 8, 23 , 42, 56 , 30]
max = min = arr[0]
smax = smin = arr[0]

for num in arr:
    if num > max:
        smax = max
        max = num
    elif(num > smax and num != max):
        smax = num
    if num < min:
        smin = min
        min = num
    elif(num > smax and num != max):
            smax = num
        
print("Largest Element :- " , max)
print("Second Largest Elmenet : -" , smax)
print("Smallest Element :- " , min)
print("Second Smallest Elment :- " , smin)