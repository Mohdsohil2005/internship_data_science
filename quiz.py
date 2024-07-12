# Integer Pattern Program

i = 0
while i<6 :
    for j in range(0,i+1) :
        print(j+1, '', end="")
    print()
    i += 1


# Star Pattern program

for i in range(0,6) :
    for j in range(0,i+1) :
        print('* ', end="")
    print()


# Program to find max & min item in a list

ls = [45, -6, 67, -15, 61, 25, 43, 85]

max = ls[0]
min = ls[0]
for i in ls :
    if i<=min :
        min = i
    if i>=max :
        max = i
    
print('max item:', max, 'present at index:', ls.index(max))
print('min item:', min, 'present at index:', ls.index(min))
    