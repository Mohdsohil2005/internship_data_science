name = input("plz Enter your name : ")
print("Hello",name,"!")

massage = """
may can hepl you sir 

Task 1 >>>> check balance
Task 2 >>>> Diposit amount
Task 3 >>>> widero amount 
"""
print(massage)
task = int(input("Entre your task : "))
total_balance = 5000
if task >= 1 and task <=3 :
    print("Welcome to you in virtual bank program")

if task == 1 :
    #check balance program
    print("your balance is : ""INR",total_balance)
    print("Thanks for visiting !")

elif task == 2:
    #deposit amount
    deposit_amount = int(input("Plz entre Deposit amount : "))
    if deposit_amount > 0 :
       total_balance += deposit_amount
       print("You have successfully Deposit your amount",deposit_amount)
       print("your balance is : ""INR",total_balance)
       print("Thanks for visiting !")
    else :
        print("Plz enter valid amount !")

elif task == 3 :
    #Withrawl amount
    withrawl = int(input("Enter Withrawl amount : "))
    if withrawl <= total_balance :
        total_balance -= withrawl
        print("You have successfully Withrawl your amount",withrawl)
        print("your balance is : ""INR",total_balance)
        print("Thanks for visiting !")
    else:
        print("you dont have sufficint amount in your account !")
        print("your balance is : ""INR",total_balance)
else :
        print("Plz choose valid option in between 1 to 3 !")
        print("Thanks for visiting !")

    