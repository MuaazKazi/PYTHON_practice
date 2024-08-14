# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
num1=int(input("Enter number 1:"))
num2=int(input("Enter number2:"))
num3=int(input("Enter number3:"))
total=num1+num2+num3
if num1 == num3 or num1==num2 or num3==num2:
    print(sum=0)
else:
        print(total)