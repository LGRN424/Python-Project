print "Data Lists Drill"
print
numbers1_list =  [67, 45, 2, 13, 1, 998]

new_list = []

while numbers1_list:
    minimum = numbers1_list[0]  # arbitrary number in list 
    for x in numbers1_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    numbers1_list.remove(minimum)    

print new_list
print
print

numbers2_list =  [89, 23, 33, 45, 10, 12, 45, 45, 45]

new_list2 = []

while numbers2_list:
    minimum = numbers2_list[0]  # arbitrary number in list 
    for x in numbers2_list: 
        if x < minimum:
            minimum = x
    new_list2.append(minimum)
    numbers2_list.remove(minimum)    

print new_list2
print
print "End of Lists"
