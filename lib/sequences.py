#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        fib = [0, 1]
        n = 2
        while n < length:
            next = fib[-1] + fib[-2]
            fib.append(next)
            n += 1
        print(fib)
    



# print_fibonacci(9)
