student = {
    101 : {"Name" : 'Sumit' , 'Scores' : [73 , 82 , 92]},
    102 : {"Name" : 'Ashutosh' , 'Scores' : [3 , 2 , 2]},
    103 : {"Name" : 'Abhishek' , 'Scores' : [13 , 12 , 12]},
    104 : {"Name" : 'Kartik' , 'Scores' : [63 , 72 , 17]},
    105 : {"Name" : 'Mahesh' , 'Scores' : [73 , 83, 82]}
}
for key , value in student.items():
    avg = sum(value['Scores']) / len(value['Scores'])
    value['Average'] = avg
    value['Passed'] = avg >= 30
print("Student Who Passed :- ")
for key, value in student.items():
    if(value['Passed']):
        print(value['Name'])

# HW create a Library management check book is available or not