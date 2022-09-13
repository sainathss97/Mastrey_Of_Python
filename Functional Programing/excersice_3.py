some_list = ['a','b','c','b','d','m','n','n']

print(list({item for item in some_list if some_list.count(item) >1}))

