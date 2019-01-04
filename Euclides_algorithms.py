# Euclides 
# GCD - is the largest integer number that divides two number without leaving a remainder
# Steps 
# a & b, where a > b, divide a by b
# if remainder r = 0 then stop 
# otherwise set a to b  and b to r and repeat step 1 until r is 0

#a = input("Insert an integer: ")
#type(a)
#b = input("Insert another integer: ")
#type(b)

def gdc(a,b):
    while (b != 0):
        r = a % b
        a = b
        b = r 
    
    return a

print(gdc(20,8))  #4
print(gdc(21,7))  #7
print(gdc(50,20)) #10
print(gdc(1424, 3084)) # correct answer is 4