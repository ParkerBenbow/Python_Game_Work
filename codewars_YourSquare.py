import math

def square(n):
    print(n)
    if n >= 1:
        a = math.isqrt(n)
        print(a)
        print(a**a)
        if a * a == n:
            print(True)
        else:
            print(False)

square(25)