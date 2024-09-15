
value = int(input("Enter the one number"))
another = int(input("Enter the two number"))
if another > value :
    one_more = int(input("Please enter another numer"))
    while one_more  > another:
        get = int(input("Enter another number"))
        if get < one_more :
            print("Over")
            break
        else:
            one_more = get




