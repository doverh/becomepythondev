#Quick sort
#Pick a “pivot” element.
#“Partition” the array into 3 parts:
#First part: all elements in this part is less than the pivot.
#Second part: the pivot itself (only one element!)
#Third part: all elements in this part is greater than or equal to the pivot.



#Pick the first element as pivot
quick_to_order = [20,32,8,2,9,10,55,1]

pivot = quick_to_order[0]

for i in range(len(quick_to_order)-1, 0, -1):
    for j in range(i):
        if quick_to_order[j] < pivot:
            temp = quick_to_order[j]
            quick_to_order[j] = pivot
            pivot = temp
    print(quick_to_order)