def remove_duplicate(list):

    new_list= [ ]

    for item in list:
        if item not in new_list:
            new_list.append(item)
    return new_list
numbers= [22, 22, 20, 21, 26, 37, 20, 1, 2,3,1,2,3]

print (remove_duplicate(numbers))
#print(input(str("write your list:")))
        
