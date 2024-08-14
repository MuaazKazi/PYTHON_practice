# 14aug
#         *****
#       *   *
#     *   *
#   *   *
# *****

num = 5
for row in range(1, num + 1):
    for col in range(num - row):
        print(" ", end=" ")
    for col in range(1, num + 1):
        if row == 1 or row == 5 or col == 1 or col == 5:
            print("*", end="")
        else:
            print(" ", end="") 
    print()
