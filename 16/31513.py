from sys import *

set_int_max_str_digits(0)
setrecursionlimit(10000)


def f(n):
    if n == 1: return 1
    else:
        return n * f(n-1)
    
print((f(3038) + 5 * f(3037)) // f(3036))
