import time

def timer(func):
    def wrapper(*arg, **kw):
        t1 = time.perf_counter()
        res = func(*arg, **kw)
        t2 = time.perf_counter()
        print(f'{func.__name__} took {((t2 - t1) * 1000):.3f}ms')
        return res
    
    return wrapper