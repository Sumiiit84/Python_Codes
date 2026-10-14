f = open('myfile.txt', "r")

content = f.read()

words = content.split()

print("Total number of words:", len(words))

unique_words = set(words)

print("Unique words:")

for word in unique_words:
    print(word)

f.close()