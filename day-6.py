# <<<<<<<<<<<<<< LOOP >>>>>>>>>>>>>>


#----------- For Loop --------------

for i in range(10): 
   print("Hello world")     #10 time print
   print("hello sohil")


for i in range(10): 
    print("Hello world" , i)    #indexing  0 : 9

for i in range(0,10,1): 
    print("Hello world" , i)        #indexing  [stating : stoping : jump]

# ----------- break and continue ------------

for i in range(10) :
    if i == 5 :
      continue
    print(i)

for i in range(10) :
    print(i)
    if i == 5 :
      break
    
ls = [12,34,23,54,6,78,45,63,79,98,34,11,48,93,85]

#is 85 present is ls , if it is prente then tell me the position on which 85 is present

if 85 in ls :
    print("present")
else :
    print("not present")

count = 0
for item in ls :
    if item == 85 :
        print("present",count)
        break
    count +=1    

print("final count ", count)   

size = int(input("Entre size of pattern : ")) 
for i in range(size) :
    for j in range(i+1) :
        print("*",end='')
    print("")

#----------- while Loop --------------

# i = 0
# while(i<=10) :
#     print("hello world",i)

# condition = Ture
# while condition :
#     user_input = input("Do you want to quiet this program press Y/N")
#     if user_input == "Y" or user_input == "y"
#     condition = False
#     print("Welcome")