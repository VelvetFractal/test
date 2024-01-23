from functools import lru_cache

    """recursive implementation"""
@lru_cache
def calc_fibonacci(n: int) -> int:
    try:
        if n < 2:
            return 1
        return calc_fibonacci(n-1) + calc_fibonacci(n-2)
    except RecursionError:
        print("n is too big")
        return -1

"""non-recursive implementation"""
def calc_fibonacci(n: int) -> int:
    a, b = 1, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a
    
"""Generator function, produces mulriple returns"""    
def fibo() -> int:
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def calc_fibo():
    f = fibo()
    a = next(f)
    for _ in range(n):
        a = next(f)
    return a

if __name__ == '__main__':
    number = int(input('enter a number:'))
    print(calc_fibonacci(number))