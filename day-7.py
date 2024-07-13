# <<<<<<<<< Function in programing language >>>>>>>>>>

#---------- Add tow number -----------

# defination
def add_tow(num1 , num2):           #parameters
    output = (num1 + num2)
    return output

a = int(input("Entre first number : "))
b = int(input("Entre secend number : "))

# calling
output = add_tow(num1=a,num2=b)
output = add_tow(a,b)               # positional arguments
print("sum is : ",output)


ls = [12,34,87,65,43,98,76,54,72,13,87]

def my_len(count) :
    output = count
    return output
output = my_len(count=len(ls))
print("lenth is : ",output)         #count lenth

def my_len(ls):
    count = 0
    for item in ls : 
        count += 1 
    return count
print(my_len(ls))                   #count lenth


def total_price(ls):
    total_sum = 0
    for item in ls : 
        total_sum += item 
    return total_sum
print(total_price(ls))              #sum total 
    