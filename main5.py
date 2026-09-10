role = str(input("Enter a Role :- "))
age = int(input("Enter a Age :- "))

print(f"Eligible : {role == 'student' and age < 21}")