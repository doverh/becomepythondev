#Recursion

def countdown(x):
    if x==0:
        print("Done!")
    else:
        print(x,"...")
        #recursion
        countdown(x-1)

countdown(10)


#power
def power(num,pwr):
    #bracking condition
    if pwr == 0:
        return 1
    else:
       return num * power(num,pwr-1)

print(power(2,5))


#factorial
