# elif condition
marks=int(input("Enter marks scored:"))
if marks >=0 and marks<=100:
 if marks>=90:
    print("Excellent")
 elif marks>=80:
    print("very good")
 elif marks>=60:
    print("well done")
 elif marks >=50:
    print("Good")
 else:
    print("Fail")
else:
 print("invalid score.")

