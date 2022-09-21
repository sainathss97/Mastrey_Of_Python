import random  # builtin Methods that are available with installed python

print(random)
#
# print(random.seed(42))
#
# print(help(random))
#
# print(dir(random))
print(random.randint(0,50))
print(random.choice([1,2,3,4]))
a = [2,4,5,67,8]
random.shuffle(a)
print(a)
if __name__ =='__main__':
    print(f"Builtin Method Random imported")