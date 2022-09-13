#Given the below class:

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat_1 = Cat('Bhoori',6)
cat_2 = Cat(name='Skyee',age=5)
cat_3 =Cat('Shori',16)
# 2 Create a function that finds the oldest cat

def age_finder(cats_obj):
    '''Pass cats as an object a list'''
    cat_names=[]
    ages=[]

    for cat in cats_obj:
        cat_names.append(cat.name)
        ages.append(int(cat.age))
    print(f"{cat_names[ages.index(max(ages))]} is the oldest cat with {max(ages)} years")


# 3 Print out: "The oldest cat is x years old.". x will be the oldest \
# cat age by using the function in #2
age_finder([cat_1,cat_2,cat_3])
