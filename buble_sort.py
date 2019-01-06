#Buble sort
#num[1,2]
# if num[1] > num[2]
# temp = num[1]
# num[1] = num[2]
# num[2] = temp

num_to_order = [20,32,8,2,9,10,55,1]
num_order = []

#start with the number of elements
#range (start,stop,step)
#range(n) = 0..n-1
for i in range(len(num_to_order) -1, 0, -1):
    for j in range(i):
        if num_to_order[j] > num_to_order[j+1]:
            temp = num_to_order[j]
            num_to_order[j] = num_to_order[j+1]
            num_to_order[j+1] = temp
       
    print(num_to_order)



    