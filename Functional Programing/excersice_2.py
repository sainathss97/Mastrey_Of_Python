# squaring of a list
my_list=[5,4,3]

print(list(map(lambda x:x*x,my_list)))

# lsit sorting based on second value
my_list_1 = [(0,2), (4,3), (10,-1),(9,9)]
my_list_1.sort(key=lambda x:x[1])
print(my_list_1)