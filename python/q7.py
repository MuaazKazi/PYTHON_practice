#Nested if..else Condition

age = int(input("Enter your age: "))
if age > 18 and age <= 40:
    weight = float(input("Enter your weight: "))
    
    if weight >= 50:
        print("You're eligible for a  fight.")
    else:
        print("You're not eligible for a  fight.")
else:
    print("You are too old/young for this  fight.")
