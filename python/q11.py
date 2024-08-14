#match
user=int(input("Enter user number:"))
match user:
    case 1:
        print("Hello user 1")
    case 2:
        print("Hello user 2")
    case 3:
        print("Hello user 3")
    case 4:
        print("Hello user 4")
    case _:
        print("invalid user")