'''
li = [1,2,3,4,5]
print(li[0])

'''
# This is a o(1) time complexity because accessing one element by index takes constant time.
'''
li = [1,2,3,4,5]
print(li)
'''
# this is a O(n) time complexity because it is iterate each elements

n = 5
m = 10
print(n + m)  # this is O(1)
for i in range(1 , n):
    for j in range(1, n):
        print(j , end= ' ')

# THIS is a O(n^2) time complexity