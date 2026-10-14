n = 9
mid = n // 2

for i in range(n):
    for j in range(n):
        if abs(i - mid) + abs(j - mid) == mid:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()