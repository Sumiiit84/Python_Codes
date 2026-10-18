text =  'my name is sumit'
print('original test :- ' , text)
print('\n')
print('Capitalize function converts the first character to uppercase')
print(text.capitalize())
print('\n')
print('casefold() converts string into lowercase')
print(text.casefold())
print('\n')

print('center() returns a centered string')
print(text.center(60))
print('\n')

print('count() returns the number of times a specifies value occurs in a string')
print(text.count('s'))
print('\n')

print('encode() returns a encoded version of the string :- ')
print(text.encode())
print('\n')

print('endswith() returns true if the string ends with the specifies value')
print(text.endswith('mit'))
print('\n')

print('expandtabs() sets the tab size of the string')
print(text.expandtabs())
print('\n')

print('find() searches the string for a specified value and returns the position of where it was found')
print(text.find('s'))
print('\n')

print('format() format specifies values in a string')
print('format_map() format specifies value from dictionary in a string')