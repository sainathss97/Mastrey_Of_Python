## WHAT is I/O in File IO?

Input and  Output streams

## How to open a file?
`open()` is used for opening a file, by default it opens in read mode unless it is explicitly specified.

> 📝 **Note:**  `open()` has a concept of cursor so once executed it only executes once as cursor traverse through one end to another

## What is `seek()` ?
this helps the cursor to point to a certain location in the memory. with `seek(0)` this points to the beginning of the file

## How to read a file?
1. `my_file.read()` - all lines
2. `my_file.readline()`  - next line after the current cursor position
3. `my_file.readlines()` - returns all lines as a list

## How to close a file?
`my_file.close()`

## How to avoid the both seek, close 

```python
with open('test.txt') as my_file:
    print(my_file.readlines())
```
## how to change modes 

```python
with open('test.txt',mode='r') as my_file:
    print(my_file.readlines())
```
there are 2 modes 
read - `mode='r'`
write - `mode='r+'`
