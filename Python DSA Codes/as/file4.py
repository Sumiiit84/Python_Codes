user = str(input('Enter a String :- '))
word = user.split()
longest = word[0]

for words in word:
    if len(words) > len(longest):
        longest = words
print('longest word :- ' , longest)
