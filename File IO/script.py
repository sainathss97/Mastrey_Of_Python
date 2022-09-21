my_file = open('test.txt')
print(my_file)
# <_io.TextIOWrapper name='File_IO.md' mode='r' encoding='cp1252'>
print(my_file.read())
print(my_file.read()) # notice how this is missing in print

my_file.seek(0)
print(my_file.read())

my_file.seek(0)
print(my_file.readline()) # reads the next line

my_file.seek(0)
print(my_file.readlines()) # returns as a list

my_file.close()

with open('test.txt', 'r+') as my_file:
    my_file.write('Hello from otherside!!')
    print(my_file.readlines())