minutes = int(input("Enter minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{minutes} is {hours} hours {remaining_minutes} minutes")