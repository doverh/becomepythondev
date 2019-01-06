##Verify if list is sorted

list1 = [10,20,30,40,50,60,70,80,90,100]
list2 = [10,20,30,40,90,60,70]

def isSorted(itemList):
    for i in range((itemList) -1 , 0, -1):
        if intemList[i] > intemList[i+1]:
            return False
    return True


isSorted(list1)
isSorted(list2)
