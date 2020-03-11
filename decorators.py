# https://realpython.com/primer-on-python-decorators/

import functools

# ###### BROILERPLATE ######
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
# ##########################

def document_it(func):
    print(f'...running document_it...')
    @functools.wraps(func)
    def wrapper_document_it(*args, **kwargs):
        print(f'...running document_it_inner...')
        print('###### INFO ######')
        print(f'calling function: {func.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'result: {result}')
        print('##################')
        return result
    return wrapper_document_it

def print_runtime(func):
    print(f'...running print_runtime...')
    import time
    @functools.wraps(func)
    def wrapper_print_runtime(*args, **kwargs):
        print(f'...running print_runtime_inner...')
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Debug: Runtime of {func.__name__}: {time.time()-start}s')
        return result
    return wrapper_print_runtime

def run_n_times(n):
    print(f'...running run_n_times...')
    def wrapper_outer_run_n_times(func):
        print(f'...running wrapper_outer_run_n_times...')
        @functools.wraps(func)
        def wrapper_inner_run_n_times_inner(*args, **kwargs):
            print(f'...running wrapper_inner_run_n_times_inner...')
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper_inner_run_n_times_inner
    return wrapper_outer_run_n_times

def memoize(func):
    print(f'...running memoize...')
    cache = {}
    @functools.wraps(func)
    def wrapper_memoize(*args):
        print(f'...running wrapper_memoize...')
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper_memoize

# ####### BELOW SOME TESTS ########

@document_it
@run_n_times(n=5)
def add(sum1, sum2):
    print(f'...running add...')
    return sum1 + sum2

sum = add(sum1=1, sum2=3)
print(sum)

@print_runtime
@run_n_times(n=2)
def waste_some_time(num_times):
    for _ in range(num_times):
        long_list = [i**2 for i in range(1000)]

waste_some_time(10000)
