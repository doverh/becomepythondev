#Global and local variable
#Global
f1 = "global"

def someMethod():
    #declare global inside method
    global f2
    print("local"+str(123))
#convert to string

print (f1)
someMethod()
#Delete 
del f1
print (f1) #exception
print (f2)
