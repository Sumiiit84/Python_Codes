list = [10, "Sumit" ,  "Rahul", 25, "Amit,  "Raj", 40, 60, 35]

max = 0
max_index = 0
first = []
sec = []

for i in range(len(list)):
    if type(list[i]) is int and list[i] > max:
        max = list[i]
        max_index = i

    else:
        continue

for i in range(max_index):
    first.append(list[i])
    
for j in range(max +1 , len(list)):
    sec.append(list[j])

print(first)
print(sec)