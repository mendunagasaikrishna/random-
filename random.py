top_range = input("enter the top range of the number")
guess =0
if top_range.isdigit():
    while True:
        random_number = ra.randint(1,int(top_range))
        guess_number=input("enter the number for gusses")
        if int(guess_number) == int(random_number):
            print("you got the gusses right")
            print("total it took {0} guess".format(guess))
            break
        else:
            print("u r guess was incorrect try again")
            guess+=1
        
else:
    print("enter number only")
