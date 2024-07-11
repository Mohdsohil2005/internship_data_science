#<<<<<<<<<<< ARITHMETIC operators >>>>>>>>>>>>>>

#---------- Addition operator ----------

num1 = int(input("Enter 1st number : "))
num2 = int(input("Entre 2nd number : "))

sum = num1 + num2
print("sum is : ",sum)                            # a + b

#---------- Subtraction operator ---------

num1 = int(input("Enter 1st name : "))
num2 = int(input("Entre 2nd number : "))

subtraction = num1 - num2
print("Subtraction is : " ,subtraction)           # a - b 

#---------- Multiplication operator ---------

num1 = int(input("Enter 1st name : "))
num2 = int(input("Entre 2nd number : "))

multiply = num1 * num2
print("Multiplication is : " ,multiply)            # a * b

#---------- Division operator ---------

num1 = int(input("Enter 1st name : "))
num2 = int(input("Entre 2nd number : "))

division = num1 / num2
print("Division is : " ,division)                  # a / b

#---------- Modulus operator ---------

num1 = int(input("Enter 1st name : "))
num2 = int(input("Entre 2nd number : "))

mod = num1 % num2
print("Modulus is : " ,mod)                        # a / b (output = remender)

#---------- Exponentiation operator  ---------

num1 = int(input("Enter 1st name : "))
num2 = int(input("Entre 2nd number : "))

exponnetiatio = num1 ** num2
print("Exponentiation is : " ,exponnetiatio)       # a ^ b (power)

#---------- Floor division operator ---------

num1 = int(input("Enter 1st name : "))
num2 = int(input("Entre 2nd number : "))

floor_division = num1 // num2
print("Floor_division is : " ,floor_division)       # a / b (output = int value)



#<<<<<<<<<< COMPARISON OPERATORS >>>>>>>>>>>>

#------------- Equal operator ---------------

num1 = int(input("Entre 1st number : "))
num2 = int (input("Entre 2nd number : "))

print( num1 == num2 )                              # output = Ture / False

#------------ Not Equal operator ---------------

num1 = int(input("Entre 1st number : "))
num2 = int (input("Entre 2nd number : "))

print( num1 != num2 )                              # output = Ture / False

#------------- Greater then operator ---------------

num1 = int(input("Entre 1st number : "))
num2 = int (input("Entre 2nd number : "))

print( num1 > num2 )                              # output = Ture / False

#------------- Less then operator ---------------

num1 = int(input("Entre 1st number : "))
num2 = int (input("Entre 2nd number : "))

print( num1 < num2 )                              # output = Ture / False

#------------- Greater then or equal to operator ---------------

num1 = int(input("Entre 1st number : "))
num2 = int (input("Entre 2nd number : "))

print( num1 >= num2 )                              # output = Ture / False

#------------- Less then or equal to operator ---------------

num1 = int(input("Entre 1st number : "))
num2 = int (input("Entre 2nd number : "))

print( num1 <= num2 )                              # output = Ture / False


#<<<<<<<<<<<<<<<< if , else , elif >>>>>>>>>>>>>>>>>

num1 = int(input("Entre 1st number : "))  #10
num2 = int (input("Entre 2nd number : ")) #20
num3 = int (input("Entre 3th number : ")) #25

if num1 > num2 :
    print( num1 ,": num 1 is gerater then")

elif num2 > num3 :
     print(num2 ,": num2 is gerater then")

else:
    print(num3 , ": num 3 is gerater then ")     #Ture



#<<<<<<<<<<<< Logical operators >>>>>>>>>>>

#----------- AND operators ---------------

num1 = int(input("Entre 1st number : "))    #25
num2 = int (input("Entre 2nd number : "))   #20
num3 = int (input("Entre 3th number : "))   #30

if num1 > num2 and num1 > num3 :
    print(num1 ,": num1 is gerater then ")

elif num2 > num1 and num2 > num3 :
    print(num2 ,": num2 is gerater then")

else:
    print(num3 ,": num3 is gerater then")   #Ture

age = int (input("Entre your age : "))      # 28
if age > 18 and age < 100 :
    print("you can vote")             #Ture

else:
    print("you cant vote")


#----------- OR operators ---------------

num1 = int(input("Entre 1st number : "))    #10
num2 = int (input("Entre 2nd number : "))   #20
num3 = int (input("Entre 3th number : "))   #25

if num1 > num2 or num1 > num3 :
    print(num1 ,": num1 is gerater then ")

elif num2 > num1 or num2 > num3 :
    print(num2 ,": num2 is gerater then")     #Ture

else:
    print(num3 ,": num3 is gerater then")   



#<<<<<<<<<<<<<<< Membership operators >>>>>>>>>>>>>

#--------------- in operator ---------------

student_list = ["sohil","harsh","keshav","manvik","lekh"]
if "harsh" in student_list :
    print("present")            #Ture
else:
    print("absent")

#---------------- not  in operator -------------

student_list = ["sohil","harsh","keshav","manvik","lekh"]
if "harsh" not in student_list :
    print("outside")            
else:
    print("inside")             #ture 

