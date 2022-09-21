from collections import Counter,defaultdict,OrderedDict

# Counter
li = [1,2,3,4,5,6,7,7,5,3,1,9]
sentence ="Hello there Buddy!"
print(Counter(li)) # gives count of elements in a list.
# Counter({1: 2, 3: 2, 5: 2, 7: 2, 2: 1, 4: 1, 6: 1, 9: 1})
print(Counter(sentence))
# Counter({'e': 3, 'l': 2, ' ': 2, 'd': 2, 'H': 1, 'o': 1, 't': 1, 'h': 1, 'r': 1, 'B': 1, 'u': 1, 'y': 1, '!': 1})

# defaultdict
dictionary = {'a': 1, 'b': 2}
print(dictionary['a'])
# print(dictionary['c']) ##will recive an error

dictionary_1 = defaultdict(int, {'a': 1, 'b': 2})
print(dictionary_1['a'])
print(dictionary_1['c'])


dictionary_2 = defaultdict(lambda:5, {'a': 1, 'b': 2})
print(dictionary_2['a'])
print(dictionary_2['c'])

# OrderedDict No more in use normal dictionary took over

#__________________________________________________________________#

import datetime

print(datetime.datetime.now()) # displays current time
print(datetime.time(5,45,22)) # displays time entered
print(datetime.date.today())

#______________________________________________________________________#

import time
t1 = time.time()
for i in range(0,50000):
    pass
t2 = time.time()
print(f"Time took to run is {t2-t1} seconds")

#_______________________________________________________________________#
from array import array

new_array = array('i', [1, 23, 44, 55, 66])
print(new_array[0])

