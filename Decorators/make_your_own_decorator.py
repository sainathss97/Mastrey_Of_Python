from time import time

def performance(fun):
    def wrapper_fun(*args,**kwargs):
        t1 = time()
        result = fun(*args,**kwargs)
        t2=time()
        print(f"Time taken { round(t2-t1,5)} s")
    

    return wrapper_fun

@performance
def long_time():
    for i in range(100000):
        i*5

long_time()
