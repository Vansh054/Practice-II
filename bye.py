import os 
os.system("cls")

def displayalldigits():
    user_input = int(input("ENTER THE NUMBER : "))
    while user_input > 0:
        rem = user_input%10
        print(rem)
        user_input = user_input//10

#displayalldigits()

def sumofalldigits():
    user_input = int(input("ENTER THE NUMBER : "))
    sum = 0
    while user_input > 0:
        rem = user_input%10
        sum = sum + rem
        user_input = user_input//10
    print(sum)

#sumofalldigits()

def armstrongnumber():
    user_input = int(input("ENTER THE NUMBER : "))
    copy = user_input
    sum = 0
    while user_input > 0:
        rem = user_input%10
        cube = rem**3
        sum = sum + cube
        user_input = user_input//10
    #print(sum)
    if copy == sum :
        print(copy,"is an armstrong number")
    else : 
        print(copy,"is not an armstrong number")

#armstrongnumber()

def paliandromenumber():
    user_input = int(input("ENTER THE NUMBER : "))
    copy = user_input
    rev = 0
    while user_input > 0:
        rem = user_input%10
        rev = (rev*10) + rem
        user_input=user_input//10
    #print(rev)
    if copy == rev :
        print(copy,"is a paliandrome number")
    else : 
        print(copy,"is not a paliandrome number")

#paliandromenumber()

def neonnumber():
    user_input = int(input("ENTER THE NUMBER : "))
    main = user_input**2
    sum = 0
    while main > 0:
        rem = main%10
        sum = sum + rem
        main=main//10
    #print(sum)
    if user_input == sum :
        print(user_input,"is a neon number")
    else : 
        print(user_input,"is not a neon number")

#neonnumber()

def ducknumber():
    user_input = int(input("ENTER THE NUMBER : "))
    copy = user_input
    flag = 0
    while user_input > 0:
        rem = user_input%10
        if rem == 0:
           flag = 1
           break
        user_input=user_input//10
    #print(sum)
    if flag == 1 :
        print(copy,"is a duck number")
    else : 
        print(copy,"is not a duck number")

ducknumber()


