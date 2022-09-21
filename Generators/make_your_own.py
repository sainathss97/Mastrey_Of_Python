class MyGen():
    current=0
    def __init__(self,first,last) -> None:
        self._first = first
        self._last =last
    
    def __iter__(self): # to be able iterate
        return self

    def __next__(self): # next for iteration to loop
        if MyGen.current < self._last:
            num = MyGen.current
            MyGen.current+=1
            return num
        raise StopIteration    

gen= MyGen(0,100)

for i in gen:
    print(i,end=' ')
    