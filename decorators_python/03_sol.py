import time

# decorator
def cache(func):
    cache_value = {} # dictionary to store cached value
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args] # return that cached value
        result = func(*args)
        cache_value[args] = result # store that value inside cache
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(4, 3))