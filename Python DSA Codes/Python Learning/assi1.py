name = input('Enter a name :- ')
ans = name[::-1]

if name == ans:
    print('Palindrome')
else:
    print('Not Palindrome')