# todo 0: Import
import random,sys

start = int(sys.argv[1])
stop = int(sys.argv[2])
# todo 1: Generate a Number
rand_num = random.randint(start,stop)
while True: # todo 4: while loop
    try: # todo 5: error case
        # todo 2: Guess the number
        num = int(input("Enter the Guessed number: "))
        # todo 3: Check the random number
        if rand_num == num:
            print("genius")
            break
        else:
            print("try again \n\n")
    except BaseException:
        print("Enter a valid number and try again!!")
        continue
