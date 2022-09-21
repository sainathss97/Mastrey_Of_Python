#fibonaci numbers with generators


def fib_seq(num):
    a=0
    b=1
    for i in range(20):
        yield a
        temp =a
        a=b
        b= temp+b


for x in fib_seq(20):
   
    print(x)