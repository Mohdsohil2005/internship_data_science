#------ user input ------

# a = 10
# b= 20
# sum = a+b
# print(sum)

# name = input("entre your name :")
# print("wellcom",name)

# num1 = int(input("enter 1st number"))
# num2 = int(input("enter 2nd number"))
# sum = num1 + num2
# print( "sum is :",sum)

# name = input("Entre your name :")
# age = int(input("Entre your age :"))
# marks = float(input("Enter your marks :"))
# print("Name is :-",name)
# print("age is :-",age)
# print("Marks is :-",marks)


#___________ boolean , list _____________

# var = True
# ver1 = False
# print(type(var))    #bool
# print(type(ver1))   #bool

#______LIST_______

# ls = [23,45,64,53,2,43,78.56,"sohik" , True]
# print(ls)
# print(type(ls))

# ls = [10,12,13,14,15,"upflair",100]    #indexing --->  0,1,2,3,4      -5,-4,-3,-2,-1
# print(ls[5][4:7])
# # print(ls[1:3])

# mutable --> changable (list)
# imutable --> unchangable (Taple)

# student_name = ["taniya","yash","prerna","aditya","kalik"]

# print(student_name[0])
# student_name[0] = "Taniya"
# student_name.append("sohil")  #add data in the last position
# student_name.append("harsh")
# student_name.pop()      # it remove from the last position
# student_name.insert(1,"punit")
# student_name.remove("taniya")
# del student_name[2]

# print(student_name)
# print(student_name.count('yash'))

# ls1 = ['A','B','C','F','E']
# ls2 = [1,2,3,4,5,12,7,8,9]
# ls2.reverse()
#ls1.sort()                #ascending oder
# ls2.sort(reverse=True)  #disending oder
# print(min(ls2))
# print(max(ls2))
# print(sum(ls2))
# print(ls1)


# ls1 = ['A','B','C','D','E']
# ls2 = ['F','G']
# full_list = ls1 + ls2
# print(full_list)

# ls1.append(ls2)         #['A', 'B', 'C', 'D', 'E', ['F', 'G']]
# ls1.extend(ls2)         #['A', 'B', 'C', 'D', 'E', 'F', 'G']
# ls1.clear()
# print(ls1.index('C'))
# print(ls1)


# ls1 = [10,20,3.1,'upflairs pvt ltd',500,400]
# # ls1[2]=100
# # print(ls1[3][0:9])
# ls1[3]= 'flipcard pvt ltd'
# print(ls1)

#_______________ TUPLE _________

tpl =(25,42,53,'upflair',True,23.4)
# print(tpl)
# print(tpl[4])
# del tpl[4]
# print(tpl)
# print(type(tpl))
