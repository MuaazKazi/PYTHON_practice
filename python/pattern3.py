# * * * * *
# * * * *
# * * *
# * *
# *

num = 5
for row in range (1,num+1):
    for col in range(num-row+1,0,-1):
        print("*", end=" ")
    print()

    