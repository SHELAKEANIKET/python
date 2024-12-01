import time

# decorator
def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"{func.__name__} function takes {end_time-start_time} time to execute")
        return result
    return wrapper

@timer
def track_time(n):
    time.sleep(n)

track_time(2)