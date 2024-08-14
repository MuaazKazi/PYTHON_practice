# 14aug
#         * * * * *
#       * * * * *
#     * * * * *
#   * * * * *
# * * * * *


# num=5
# for row in range (1,num+1):
#     print(" "*(num-1),"*"*num)
    

num = 5
for row in range (1,num+1):
    for col in range(num-row+1,0,-1):
        print("", end=" ")
    for col in range(1,num+1):
        print("*",end='')
    print()    


