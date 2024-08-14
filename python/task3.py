# * * * * * * * * *
#     *   *   *   *
#         *   *   *   
#         *   *   *
#             *   *   
#             *   *   
#             *   *   
#                 *
#                 *


num = 9
for row in range(1,num+1):
    for col in range(1,row):
        print(" ",end=' ')
    for col in range(num-row+1,0,-1):
        if row == 1:
             print("*",end=' ')
             continue
        if col % 2!=0:
        
                print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

