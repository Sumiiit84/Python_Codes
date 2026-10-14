with open('myfile.txt' , 'r') as f:
    lines = f.readlines()
    print('Total number of lines :- ' , len(lines))
    print('2nd line :- ' , lines[1])
    print('3rd line :- ' , lines[2])