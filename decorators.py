import time

def document_it(func):
    print(f'...running document_it...')
    def document_it_inner(*args, **kwargs):
        print(f'...running document_it_inner...')
        print('###### INFO ######')
        print(f'calling function: {func.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        result = func(*args, **kwargs)
        print(f'result: {result}')
        print('##################')
        return result
    return document_it_inner

def print_runtime(func):
    print(f'...running print_runtime...')
    def print_runtime_inner(*args, **kwargs):
        print(f'...running print_runtime_inner...')
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Debug: Runtime of {func.__name__}: {time.time()-start}s')
        return result
    return print_runtime_inner

@print_runtime
@document_it
def add(sum1, sum2):
    print(f'...running add...')
    return sum1 + sum2

sum = add(sum1=1, sum2=3)
print(sum)