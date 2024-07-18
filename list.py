list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list1[19:0:-1]) 


for element in list1[::-1]:
    print(element)



my_list = [1, 2, 3, 4, 5]
sequence = ['a', 'b', 'c']
index = 2
for i, element in enumerate(sequence):
     my_list.insert(index + i, element)
 print(my_list)
