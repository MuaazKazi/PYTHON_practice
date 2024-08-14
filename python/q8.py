#Nested if..else Condition
marks=int(input("Enter your marks:"))

if marks>=50 and marks<=100:
    attendance=int(input("Enter your attendance:"))
    if attendance>=70:
        print("You're pass.")
    else:
        print("Not having attendance more than 70.")
else:
    print("Fail")

