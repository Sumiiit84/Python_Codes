with open('myfile.txt' , 'r') as f:
    content = f.read()
    count = 0
    for ch in content:
        if ch.lower() in 'aeiou':
            count += 1
            
    print('Total Vowels :- ' , count)