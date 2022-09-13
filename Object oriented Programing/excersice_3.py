class SuperList(list):
   
    def __len__(self):
        return 1000


my_l1 = SuperList()

print(len(my_l1))

my_l1.append(5)
print(my_l1[0])
print(issubclass(SuperList,list))
